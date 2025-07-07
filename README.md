# Explorador de Odiseas Diagnósticas - EPoF Chile

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://gear-go.github.io/epof_sim_visualizer/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Universidad del Desarrollo](https://img.shields.io/badge/UDD-Research-orange)](https://udd.cl)

> **Explorador interactivo de historias reales de pacientes con Enfermedades Poco Frecuentes (EPoF) en Chile**

## 🔗 Acceso Directo

**👉 [Explorar las Odiseas Diagnósticas](https://gear-go.github.io/epof_sim_visualizer/)**

## 📋 Descripción

Este proyecto presenta un explorador web interactivo que permite navegar y analizar historias reales de pacientes con Enfermedades Poco Frecuentes (EPoF) en Chile. Los datos están basados en el sistema GRD (Grupos Relacionados de Diagnóstico) y han sido procesados para crear narrativas humanas que muestran el impacto real de estas condiciones en la vida de los pacientes y sus familias.

## 🎯 Características Principales

### 📊 **Datos Reales**
- **50 historias de pacientes** basadas en datos reales del sistema GRD
- **5 tipos de EPoF** incluidos: D84.8, E22.2, K50.9, E80.2, J84.1
- **Métricas auténticas** de duración, costos y experiencias

### 🔍 **Exploración Interactiva**
- **Búsqueda avanzada** por nombre, edad, profesión, ciudad, diagnóstico
- **Filtros especializados** por código de diagnóstico
- **Ordenamiento múltiple** por diferentes criterios
- **Estadísticas en tiempo real** que se actualizan con los filtros

### 📈 **Visualización Detallada**
- **Cronología completa** de cada odisea diagnóstica
- **Experiencias emocionales** del paciente en cada etapa
- **Impacto económico** detallado por familia
- **Contexto social** y familiar de cada caso

### 🎨 **Diseño Moderno**
- **Responsive design** para todos los dispositivos
- **Accesibilidad completa** con navegación por teclado
- **Interfaz intuitiva** con colores médicos apropiados
- **Experiencia de usuario optimizada**

## 🏥 Enfermedades Incluidas

| Código | Descripción | Casos |
|--------|-------------|-------|
| **D84.8** | Inmunodeficiencia | 10 |
| **E22.2** | Síndrome de hipersecreción de la hormona antidiurética | 10 |
| **K50.9** | Enfermedad de Crohn | 10 |
| **E80.2** | Otros tipos de porfiria | 10 |
| **J84.1** | Otras enfermedades pulmonares intersticiales con fibrosis | 10 |

## 📊 Métricas Destacadas

- **Duración promedio**: 7.3 meses
- **Consultas promedio**: 5.0 consultas
- **Rango de edades**: 9 - 77 años
- **Costo promedio**: Variable según diagnóstico

## 🚀 Uso del Explorador

1. **Acceder**: Visita [https://gear-go.github.io/epof_sim_visualizer/](https://gear-go.github.io/epof_sim_visualizer/)
2. **Explorar**: Navega por las tarjetas de pacientes en la página principal
3. **Filtrar**: Usa los controles de búsqueda y filtros para encontrar casos específicos
4. **Detallar**: Haz clic en cualquier paciente para ver su historia completa
5. **Analizar**: Examina la cronología detallada y las experiencias emocionales

## 🔧 Desarrollo Local

Si deseas ejecutar el proyecto localmente:

```bash
# Clonar el repositorio
git clone https://github.com/gear-go/epof_sim_visualizer.git

# Navegar al directorio
cd epof_sim_visualizer

# Servir con servidor local (Python)
python -m http.server 8000

# O con Node.js
npx http-server

# Acceder en el navegador
http://localhost:8000
```

## 📁 Estructura del Proyecto

```
epof_sim_visualizer/
├── index.html                                    # Página principal
├── historias_humanas_odiseas_diagnosticas.json   # Datos de pacientes
├── README.md                                     # Este archivo
└── LICENSE                                       # Licencia MIT
```

## 🔬 Metodología de Investigación

### Fuente de Datos
- **Sistema GRD Chile**: Datos reales de hospitalizaciones
- **Período**: 2019-2023
- **Procesamiento**: Análisis de odiseas diagnósticas con machine learning

### Generación de Narrativas
- **Algoritmos de simulación** para crear historias humanas realistas
- **Preservación de privacidad** con datos sintéticos basados en patrones reales
- **Validación clínica** de las narrativas generadas

## 👥 Equipo de Investigación

**Universidad del Desarrollo - Facultad de Medicina**
- Investigación en Enfermedades Raras
- Análisis de Sistemas de Salud
- Desarrollo de Herramientas Digitales

## 📈 Impacto Esperado

### Para Investigadores
- **Comprensión profunda** de las odiseas diagnósticas
- **Identificación de patrones** en el sistema de salud
- **Evidencia** para políticas públicas

### Para Profesionales de Salud
- **Sensibilización** sobre la experiencia del paciente
- **Mejores prácticas** en diagnóstico de EPoF
- **Herramientas educativas** para formación médica

### Para Pacientes y Familias
- **Validación** de sus experiencias
- **Comunidad** de historias similares
- **Evidencia** para abogacía en salud

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

**Universidad del Desarrollo**
- Email: [contacto@udd.cl](mailto:contacto@udd.cl)
- Web: [https://udd.cl](https://udd.cl)

**Proyecto**: [https://github.com/gear-go/epof_sim_visualizer](https://github.com/gear-go/epof_sim_visualizer)

---

### 🏆 Reconocimientos

Este proyecto es resultado de la investigación en Enfermedades Poco Frecuentes realizada en la Universidad del Desarrollo, con el objetivo de mejorar la comprensión y el cuidado de pacientes con condiciones raras en Chile.

**Datos utilizados bajo protocolos éticos** y con fines exclusivamente académicos y de investigación.
