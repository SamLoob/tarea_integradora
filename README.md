# 🧠 TAREA INTEGRADORA  
## 🔐 Sistema de Validación y Diagnóstico Algorítmico

Bienvenido a un entorno interactivo en Python que simula un sistema de verificación, calibración y análisis algorítmico.  
Este programa guía al usuario por un menú de funcionalidades que evalúan la **estabilidad del sistema**, **coordenadas de restauración**, y **anomalías semánticas** en frases ingresadas.

---

## 🚀 Inicio del Sistema

🔸 Al ejecutar el programa:

- Se solicita un **código de seguridad alfanumérico**.
- ✅ Si el código es válido → acceso al menú principal.
- ❌ Si el código es incorrecto → mensaje de error y cierre del sistema.

---

## 📋 MENÚ DE FUNCIONES

Cada opción representa una herramienta de diagnóstico especializada.  
El usuario puede navegar entre ellas según el tipo de análisis que desea realizar.

---

### 🔧 1. Calibrar Núcleo del Sistema

📥 Entrada: número entero  
📊 Diagnóstico:

| Valor | Resultado |
|-------|-----------|
| `> 0` | 🟢 Núcleo estable |
| `< 0` | 🔴 Núcleo inestable: se recomienda recalibración |
| `= 0` | 🟡 Punto neutro: monitoreo requerido |

---

### 🛰️ 2. Validar Coordenadas de Restauración

📥 Entrada: dos números (X, Y)  
📊 Evaluación de paridad:

| Paridad | Resultado |
|---------|-----------|
| Ambos pares | 🟢 Coordenadas óptimas para restauración |
| Ambos impares | 🔴 Coordenadas inestables: riesgo de error |
| Mixtos | 🟡 Coordenadas en zona gris: precaución |

---

### 📈 3. Índice de Estabilidad Algorítmica (IEA)

📥 Entrada: dos números  
🧮 Cálculo del IEA → interpretación:

| IEA | Resultado |
|-----|-----------|
| `< 10` | 🔴 Estabilidad baja: riesgo de colapso inminente |
| `10 ≤ IEA ≤ 50` | 🟡 Estabilidad moderada: ajustes recomendados |
| `> 50` | 🟢 Sistema estable y funcional |

---

### 🧪 4. Análisis de Estabilidad del Sistema

📥 Entrada: número entero  
📊 Evaluación:

| Valor | Resultado |
|-------|-----------|
| `> 100` | 🔴 Sobrecarga: riesgo alto |
| `50 ≤ valor ≤ 100` | 🟢 Estado óptimo |
| `< 50` | 🟡 Bajo rendimiento: optimización recomendada |

---

### 🕵️ 5. Escaneo de Anomalías

📥 Entrada: frase libre  
🔍 Búsqueda de palabras clave:

- Si contiene `"Error"` o `"Corrupto"` → ❌ **Mensaje de error**
- Si no contiene esas palabras → ✅ **El código está limpio**

> ⚠️ *Nota:* El operador `in` se usa para validar si una palabra está contenida en la frase.  
> Es **sensible a mayúsculas y minúsculas**.

---

### 🛑 6. Salir

Finaliza el programa y cierra el entorno de diagnóstico.

---

## 🛠️ REQUISITOS DEL SISTEMA

- 🐍 Python 3.x  
- 🧠 Visual Studio Code (editor recomendado)  
- 🧬 Git (para control de versiones)

---

## 📦 INSTALACIÓN

```bash
git clone https://github.com/SamLoob/tarea_integradora.git
cd tarea_integradora
python sistema_menu.py