from openai import OpenAI  # Nova forma de importar
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# 1. Inicialize o Cliente (Coloque sua chave aqui ou use variável de ambiente)
client = OpenAI(api_key=("SUA_CHAVE_AQUI"))")

def ouvir_microfone():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True 

    with sr.Microphone() as source:
        print(">>> Ajustando ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print(">>> Pode falar agora!")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print(">>> Gravado! Processando...")
            
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            
            # --- NOVA SINTAXE WHISPER ---
            with open("temp_audio.wav", "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
            return transcript.text # Agora é um atributo .text

        except Exception as e:
            print(f"Erro no STT: {e}")
            return None

def pensar_com_gpt(texto_entrada):
    # --- NOVA SINTAXE CHAT ---
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Sugestão: mais rápido e barato
        messages=[{"role": "user", "content": texto_entrada}]
    )
    return response.choices[0].message.content

# O restante da função falar() e o loop principal permanecem quase iguais

def falar(texto_resposta):
    tts = gTTS(text=texto_resposta, lang='pt-br')
    tts.save("resposta.mp3")
    print(f"IA: {texto_resposta}")
    playsound.playsound("resposta.mp3")
    os.remove("resposta.mp3")

# Loop Principal
if __name__ == "__main__":
    while True:
        pergunta = ouvir_microfone()
        if pergunta:
            print(f"Você disse: {pergunta}")
            resposta = pensar_com_gpt(pergunta)
            falar(resposta)