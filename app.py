import os
import logging
from typing import Tuple, Dict, Any
from flask import Flask, request, jsonify, render_template, Response
from dotenv import load_dotenv
import google.generativeai as genai

# Configuración del entorno
load_dotenv()

# Cargamos las creedenciales de nuestra API de Gemini
API_KEY = os.getenv("geminiApi")
if not API_KEY:
    raise ValueError("FATAL: No se encontró la variable de entorno 'geminiApi'.")

# Constantes de Configuración
MODEL_NAME = "models/gemini-2.0-flash-lite"
DEBUG_MODE = False

# --- Inicialización de Servicios ---
# Configuración del cliente de Google Generative AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# Inicialización de Flask
app = Flask(__name__)

# Configuración básica de logging para depuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Rutas de la Aplicación ---

@app.route("/")
def index() -> str:
    """
    Ruta raíz. Renderiza la interfaz de usuario principal.
    
    Returns:
        str: HTML renderizado de la plantilla 'index.html'.
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_gemini() -> Tuple[Response, int]:
    """
    Endpoint de API para interactuar con el modelo Gemini.
    Recibe un prompt JSON, consulta al modelo y devuelve la respuesta generada.

    Returns:
        Tuple[Response, int]: Respuesta JSON y código de estado HTTP.
    """
    try:
        # Obtención y validación del payload
        request_data = request.get_json()
        
        if not request_data or "prompt" not in request_data:
            logger.warning("Solicitud recibida sin datos o sin campo 'prompt'.")
            return jsonify({"error": "El cuerpo de la solicitud debe contener un JSON con el campo 'prompt'."}), 400

        user_prompt = request_data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({"error": "El prompt no puede estar vacío."}), 400

        # Inferencia con el modelo (
        logger.info(f"Procesando prompt: {user_prompt[:50]}...") # Log parcial por privacidad
        
        gemini_response = model.generate_content(user_prompt)
        
        # Construcción de la respuesta
        response_text = gemini_response.text
        
        return jsonify({
            "status": "success",
            "model": MODEL_NAME,
            "response": response_text
        }), 200

    except Exception as e:
        logger.error(f"Error interno durante la inferencia: {str(e)}")
        # En producción, evitamos devolver el error crudo al cliente por seguridad
        return jsonify({"error": "Ocurrió un error al procesar su solicitud con la IA."}), 500

# --- Punto de Entrada ---
if __name__ == "__main__":
    # Nota: El contexto SSL es útil para desarrollo local si usamos features como el micrófono del navegador
    # Asegúrate de tener generados 'cert.pem' y 'key.pem' o elimina el parámetro ssl_context
    try:
        logger.info(f"Iniciando servidor Flask con modelo: {MODEL_NAME}")
        app.run(debug=DEBUG_MODE, ssl_context=("cert.pem", "key.pem"))
    except FileNotFoundError:
        logger.warning("Certificados SSL no encontrados. Iniciando en modo HTTP estándar.")
        app.run(debug=DEBUG_MODE)