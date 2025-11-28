# 🤖 Gemini AI Web Chat

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![Security](https://img.shields.io/badge/Security-SSL%2FjTLS-red)

Una interfaz web minimalista para interactuar con los modelos de Inteligencia Artificial **Google Gemini**. Desarrollada con **Flask** (Backend) y **Vanilla JS** (Frontend), implementando comunicación asíncrona y gestión de estados de carga.

## 📋 Características

* **Integración API:** Conexión directa con `gemini-2.0-flash-lite` (o modelos compatibles) usando la SDK de Google.
* **Interfaz Reactiva:** Chat fluido sin recargas de página (AJAX/Fetch API).
* **Diseño Profesional:** CSS moderno con modo oscuro, animaciones de entrada y estados de carga.
* **Seguridad:** Gestión de credenciales mediante variables de entorno y soporte para HTTPS local.

## 🛠️ Stack Tecnológico

* **Backend:** Python, Flask.
* **Frontend:** HTML5, CSS3, JavaScript (ES6+).
* **IA:** Google Generative AI (Gemini API).

## 🚀 Instalación y Despliegue Local

Sigue estos pasos para ejecutar el proyecto en tu máquina:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/ToniSureda/gemini-flask-chat.git
    cd gemini-flask-chat
    ```

2.  **Crear entorno virtual (Recomendado):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar API Key:**
    * Crea un archivo llamado `.env` en la raíz del proyecto.
    * Añade tu clave de Google AI Studio:
      ```env
      geminiApi="TU_API_KEY_AQUI"
      ```

## 🔒 Configuración SSL (HTTPS Local)

Para habilitar características modernas del navegador o simular un entorno de producción, puedes generar certificados autofirmados.

1.  **Generar certificados (Requiere OpenSSL):**
    Ejecuta este comando en la raíz del proyecto:
    ```bash
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    ```
    *(Presiona Enter a todas las preguntas para dejarlas en blanco si es solo para desarrollo).*

2.  **Modo Automático:**
    La aplicación detectará automáticamente si existen `cert.pem` y `key.pem`.
    * **Si existen:** Arranca en `https://127.0.0.1:5000`.
    * **Si NO existen:** Arranca en `http://127.0.0.1:5000`.

## ⚙️ Ejecución

```bash
python app.py