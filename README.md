# 🧠 AI Interview Simulator

This Python project simulates a job interview experience using AI technologies. It helps users practice their spoken English, structure better answers, and receive automatic feedback for improvement.

## 🎯 Features

- 🎤 **Spoken Questions**: Randomly selects and reads out common interview questions.
- 🎙️ **Voice Recording**: Captures your spoken answer using the microphone.
- ✍️ **Transcription**: Converts your voice into text using OpenAI’s Whisper.
- ✅ **Correction**: Fixes grammar and style issues in your response.
- 💡 **Improvement Suggestions**: Suggests a more professional and polished version using ChatGPT.
- 🔊 **Voice Feedback**: Reads the improved version aloud.

## 🛠️ Requirements

- Python 3.8 or higher  
- An OpenAI API key with GPT-3.5 or GPT-4 access  
- Required libraries:


## 📂 Archivos

- `interviewer.py`: script principal
- `interview_questions.txt`: lista de preguntas
- `.env`: contiene tu clave API (no subir este archivo a GitHub)

## ▶️ Uso

1. Ejecuta el script:
2. Escucha la pregunta, responde en voz alta.
3. El sistema:
- Transcribe tu voz
- Corrige errores
- Mejora tu respuesta
- Reproduce en voz alta la versión mejorada

Presiona `Enter` para seguir o `1` para salir.

## 🧠 Tecnologías

- OpenAI Whisper (transcripción)
- ChatGPT (corrección y mejora)
- Pyttsx3 (voz sintética)
- SoundDevice (grabación)

---

👨‍💻 Hecho con Python para ayudarte a practicar entrevistas en inglés de forma inteligente.
