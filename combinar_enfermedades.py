#!/usr/bin/env python3
"""
Script para combinar enfermedades del archivo principal con enfermedades pediátricas
y generar el archivo JSON que usa la aplicación web.
"""

import json
import os
from datetime import datetime

def load_json_file(filepath):
    """Cargar un archivo JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data, filepath):
    """Guardar datos en un archivo JSON"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def convert_claude_to_web_format(claude_patient_id, claude_patient_data, diagnosis_info=None, is_pediatric=False):
    """
    Convertir el formato de Claude al formato que espera la web
    """
    if is_pediatric:
        # Para casos pediátricos, la estructura es diferente
        family_profile = claude_patient_data.get('perfil_familia', {})
        patient_info = family_profile.get('paciente', {})
        odyssey = claude_patient_data.get('odisea_diagnostica_familiar', {})
        narrative = claude_patient_data.get('narrativa_cronologica_padres', [])
        
        # Obtener información del contexto familiar
        family_situation = family_profile.get('situacion_familiar', '')
        city = family_profile.get('ciudad_residencia', '')
        
        profile = {
            'nombre': patient_info.get('nombre', ''),
            'edad': patient_info.get('edad', 0),
            'sexo': patient_info.get('sexo', ''),
            'profesion': 'Estudiante' if patient_info.get('edad', 0) < 18 else '',
            'estado_civil': 'Soltero/a' if patient_info.get('edad', 0) < 18 else '',
            'situacion_familiar': family_situation,
            'personalidad': patient_info.get('personalidad', []),
            'ciudad_residencia': city
        }
        
        # Si hay información de diagnóstico adicional, usarla
        if diagnosis_info:
            diagnosis_name = diagnosis_info.get('nombre', odyssey.get('diagnostico_final', ''))
        else:
            diagnosis_name = odyssey.get('diagnostico_final', '')
            
        odyssey_summary = {
            'duracion_meses': odyssey.get('duracion_meses', 0),
            'numero_consultas': odyssey.get('numero_consultas', 0),
            'diagnostico_final': diagnosis_name,
            'costo_total_familia': odyssey.get('costo_estimado_familia', '')
        }
        
    else:
        # Para casos no pediátricos (adultos), usar la estructura original
        profile_data = claude_patient_data.get('perfil_paciente', {})
        odyssey = claude_patient_data.get('resumen_odisea_personal', {})
        narrative = claude_patient_data.get('narrativa_cronologica', [])
        
        profile = {
            'nombre': profile_data.get('nombre', ''),
            'edad': profile_data.get('edad', 0),
            'sexo': profile_data.get('sexo', ''),
            'profesion': profile_data.get('profesion', ''),
            'estado_civil': profile_data.get('estado_civil', ''),
            'situacion_familiar': profile_data.get('situacion_familiar', ''),
            'personalidad': profile_data.get('personalidad', []),
            'ciudad_residencia': profile_data.get('ciudad_residencia', '')
        }
        
        # Si hay información de diagnóstico adicional, usarla
        if diagnosis_info:
            diagnosis_name = diagnosis_info.get('nombre', odyssey.get('diagnostico_final', ''))
        else:
            diagnosis_name = odyssey.get('diagnostico_final', '')
            
        odyssey_summary = {
            'duracion_meses': odyssey.get('duracion_meses', 0),
            'numero_consultas': odyssey.get('numero_consultas', 0),
            'diagnostico_final': diagnosis_name,
            'costo_total_familia': odyssey.get('costo_total_familia', '')
        }
    
    web_format = {
        'perfil_paciente': profile,
        'resumen_odisea_personal': odyssey_summary,
        'narrativa_cronologica': narrative
    }
    
    # Agregar datos específicos de casos pediátricos si existen
    if 'perspectiva_cuidador' in claude_patient_data:
        web_format['perspectiva_cuidador'] = claude_patient_data['perspectiva_cuidador']
    
    return web_format

def combine_disease_data():
    """
    Combinar datos de enfermedades del archivo principal con enfermedades pediátricas
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Archivos de entrada
    main_file = os.path.join(base_dir, 'historias_claude_odiseas_diagnosticas_20250708_121059.json')
    pediatric_file = os.path.join(base_dir, 'historias_claude_familias_pediatricas_unificadas_20250708_232222.json')
    
    # Archivo de salida
    output_file = os.path.join(base_dir, 'historias_humanas_odiseas_diagnosticas.json')
    
    # Información adicional sobre la enfermedad Q43.8
    q43_8_info = {
        "Q43.8": {
            "nombre": "Otras malformaciones congénitas del intestino, especificadas",
            "descripcion": "Incluye diversas malformaciones congénitas intestinales como diverticulitis congénita del colon, divertículo congénito del intestino, dolicocolon, megaloapéndice, megaloduodeno, microcolon, síndrome de asa ciega congénita, y transposición del colon, intestino o apéndice. Una condición específica es el síndrome de ulceración del cordón umbilical-atresia intestinal.",
            "edad_aparicion": {
                "periodo": "Neonatal - Primera infancia",
                "detalle": "Al nacer o dentro del primero o segundo día de vida. En malrotación intestinal: 30% en el primer mes de vida y 75% en los primeros 5 años."
            },
            "diagnostico": {
                "dificultad": "Relativamente sencillo",
                "metodos": "Sonda nasogástrica para detectar líquido en estómago (especialmente si está teñido de bilis). Radiografías gastrointestinales, seriada gastrointestinal superior y/o enema de bario.",
                "hallazgos_clave": "Obstrucción intestinal, dificultades alimentarias, distensión, vómitos, incapacidad para eliminar gases y heces"
            },
            "tratamiento": {
                "principal": "Reparación quirúrgica en lactantes sintomáticos",
                "tasa_cirugia": "137 de 148 pacientes estudiados requirieron cirugía",
                "urgencia": "Tratamiento quirúrgico temprano es esencial"
            },
            "pronostico": {
                "variable": "Depende de la malformación específica",
                "bueno": "Malrotación tiene muy buen pronóstico",
                "malo": "Hernia diafragmática congénita: mortalidad 10-30%",
                "mortalidad_global": "14.2%, principalmente por malformaciones extraintestinales"
            }
        }
    }
    
    print("🔄 Cargando datos de enfermedades...")
    
    # Cargar datos principales
    main_data = load_json_file(main_file)
    
    # Cargar datos pediátricos
    pediatric_data = load_json_file(pediatric_file)
    
    # Crear estructura de datos combinada
    combined_data = {
        "metadatos": {
            "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_historias": 0,  # Se calculará después
            "descripcion": "Historias combinadas de odiseas diagnósticas: enfermedades generales y pediátricas",
            "enfoque": "Narrativas generadas por IA basadas en trayectorias sintéticas reales",
            "modelo_ia": "claude-3-sonnet-20240229",
            "epof_incluidos": [],  # Se llenará después
            "fuente_datos": "Combinación de historias Claude generales y pediátricas",
            "archivos_origen": [
                "historias_claude_odiseas_diagnosticas_20250708_121059.json",
                "historias_claude_familias_pediatricas_unificadas_20250708_232222.json"
            ]
        },
        "estadisticas_humanas": {
            "total_historias": 0,
            "duracion_promedio_meses": 0,
            "consultas_promedio": 0,
            "distribucion_epof": {},
            "rango_edades": {
                "menor": 999,
                "mayor": 0,
                "promedio": 0
            }
        },
        "historias_pacientes": {},
        "informacion_enfermedades": q43_8_info
    }
    
    print("📋 Procesando historias principales...")
    
    # Agregar historias del archivo principal
    main_histories = main_data.get('historias_pacientes_claude', {})
    total_months = 0
    total_consultations = 0
    total_ages = 0
    count = 0
    
    epof_distribution = {}
    
    for patient_id, patient_data in main_histories.items():
        converted_patient = convert_claude_to_web_format(patient_id, patient_data, is_pediatric=False)
        combined_data["historias_pacientes"][patient_id] = converted_patient
        
        # Actualizar estadísticas
        odyssey = converted_patient["resumen_odisea_personal"]
        profile = converted_patient["perfil_paciente"]
        
        if odyssey.get("duracion_meses"):
            total_months += odyssey["duracion_meses"]
        if odyssey.get("numero_consultas"):
            total_consultations += odyssey["numero_consultas"]
        if profile.get("edad"):
            total_ages += profile["edad"]
            # Actualizar rango de edades
            combined_data["estadisticas_humanas"]["rango_edades"]["menor"] = min(
                combined_data["estadisticas_humanas"]["rango_edades"]["menor"], 
                profile["edad"]
            )
            combined_data["estadisticas_humanas"]["rango_edades"]["mayor"] = max(
                combined_data["estadisticas_humanas"]["rango_edades"]["mayor"], 
                profile["edad"]
            )
        
        # Extraer código de diagnóstico del ID del paciente
        diagnosis_code = patient_id.split('_')[1] if '_' in patient_id else "Unknown"
        epof_distribution[diagnosis_code] = epof_distribution.get(diagnosis_code, 0) + 1
        
        count += 1
    
    print("👶 Procesando historias pediátricas...")
    
    # Agregar historias pediátricas
    pediatric_histories = pediatric_data.get('historias_familias_claude', {})
    
    for patient_id, patient_data in pediatric_histories.items():
        # Para casos pediátricas, usar la información adicional de Q43.8
        diagnosis_code = patient_id.split('_')[1] if '_' in patient_id else "Q43.8"
        diagnosis_info = q43_8_info.get(diagnosis_code, {})
        
        converted_patient = convert_claude_to_web_format(patient_id, patient_data, diagnosis_info, is_pediatric=True)
        combined_data["historias_pacientes"][patient_id] = converted_patient
        
        # Actualizar estadísticas
        odyssey = converted_patient["resumen_odisea_personal"]
        profile = converted_patient["perfil_paciente"]
        
        if odyssey.get("duracion_meses"):
            total_months += odyssey["duracion_meses"]
        if odyssey.get("numero_consultas"):
            total_consultations += odyssey["numero_consultas"]
        if profile.get("edad"):
            total_ages += profile["edad"]
            # Actualizar rango de edades
            combined_data["estadisticas_humanas"]["rango_edades"]["menor"] = min(
                combined_data["estadisticas_humanas"]["rango_edades"]["menor"], 
                profile["edad"]
            )
            combined_data["estadisticas_humanas"]["rango_edades"]["mayor"] = max(
                combined_data["estadisticas_humanas"]["rango_edades"]["mayor"], 
                profile["edad"]
            )
        
        epof_distribution[diagnosis_code] = epof_distribution.get(diagnosis_code, 0) + 1
        
        count += 1
    
    # Finalizar estadísticas
    combined_data["estadisticas_humanas"]["total_historias"] = count
    combined_data["estadisticas_humanas"]["duracion_promedio_meses"] = total_months / count if count > 0 else 0
    combined_data["estadisticas_humanas"]["consultas_promedio"] = total_consultations / count if count > 0 else 0
    combined_data["estadisticas_humanas"]["rango_edades"]["promedio"] = total_ages / count if count > 0 else 0
    combined_data["estadisticas_humanas"]["distribucion_epof"] = epof_distribution
    
    # Actualizar metadatos
    combined_data["metadatos"]["total_historias"] = count
    combined_data["metadatos"]["epof_incluidos"] = list(epof_distribution.keys())
    
    print("💾 Guardando archivo combinado...")
    
    # Guardar archivo combinado
    save_json_file(combined_data, output_file)
    
    print(f"✅ ¡Completado! Archivo guardado en: {output_file}")
    print(f"📊 Resumen:")
    print(f"   - Total de historias: {count}")
    print(f"   - Duración promedio: {combined_data['estadisticas_humanas']['duracion_promedio_meses']:.1f} meses")
    print(f"   - Consultas promedio: {combined_data['estadisticas_humanas']['consultas_promedio']:.1f}")
    print(f"   - Rango de edades: {combined_data['estadisticas_humanas']['rango_edades']['menor']}-{combined_data['estadisticas_humanas']['rango_edades']['mayor']} años")
    print(f"   - EPoF incluidos: {', '.join(combined_data['metadatos']['epof_incluidos'])}")
    print(f"   - Distribución por EPoF: {epof_distribution}")

if __name__ == "__main__":
    combine_disease_data()
