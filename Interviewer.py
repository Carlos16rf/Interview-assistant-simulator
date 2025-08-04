import random
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
# Cargar clave de API

def question_choice():
    with open("C:/Users/crf16/Downloads/interview_questions.txt", "r", encoding="utf-8") as file:
        questions = [line.strip("- ").strip() for line in file if line.startswith("-")]
    return random.choice(questions)

def speak_text():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "ZIRA" in voice.id:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', engine.getProperty('rate') - 40)
    question = question_choice()
    print("❓", question)
    engine.say(question)
    engine.runAndWait()
    return question
def grabar_con_sounddevice(nombre_archivo="respuesta.wav", segundos=15, fs=44100):
    print(f"🎙️ Grabando durante {segundos} segundos...")
    audio = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(nombre_archivo, fs, audio)
    print("✅ Grabación finalizada:", nombre_archivo)
    return nombre_archivo

def transcribir_whisper(nombre_archivo="respuesta.wav"):
    model = whisper.load_model("small")
    result = model.transcribe(nombre_archivo, language="en")
    print("📝 Transcripción:", result["text"])
    return result["text"]

def corregir_y_mejorar_con_chatgpt(texto,pregunta):
    prompt = f"""You are an English expert helping someone improve their interview answers.
    Interview question: "{pregunta}"

    Original answer: "{texto}"
1. First, correct any grammar or language issues.
2. Then, provide a better and more professional version.
3. If their answer is wrong, vague, or shows misunderstanding, generate an ideal, high-quality model answer to that question instead.


Original answer: "{texto}"

Respond in this format:
✅ Corrected: ...
💡 Improved: ...
"""
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response =client.chat.completions.create(
        model="gpt-3.5-turbo",  # usa "gpt-4" si tienes acceso
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    output = response.choices[0].message.content
    print(output)
    # Buscar la respuesta ideal si existe
    if "💡 Improved:" in output:
        respuesta_ideal = output.split("💡 Improved:")[1].strip()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            if "ZIRA" in voice.id:
                engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', engine.getProperty('rate') - 40)
        engine.say(respuesta_ideal)
        engine.runAndWait()
    return output

# Loop principal
if __name__ == "__main__":
    while True:
        pregunta=speak_text()
        grabar_con_sounddevice("respuesta.wav", 15)
        texto = transcribir_whisper("respuesta.wav")
        if texto:
            corregir_y_mejorar_con_chatgpt(texto,pregunta)

        seguir = input("Presiona [Enter] para continuar o 1 para salir: ")
        if seguir.strip() == "1":
            print("👋 Fin del simulador.")
            break
