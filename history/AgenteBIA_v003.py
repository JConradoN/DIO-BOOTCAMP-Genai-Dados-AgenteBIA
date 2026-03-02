from openai import OpenAI
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# 1. Configuração do Cliente
client = OpenAI(api_key="SUA_CHAVE_AQUI")

# 2. Contexto e Palavras de Saída
SYSTEM_PROMPT = """
Você é um Consultor de Investimentos sênior do Bradesco, especializado na filosofia de Benjamin Graham.
Seu objetivo é ajudar o cliente a construir uma carteira sólida e segura.
Diretrizes: Foco em Margem de Segurança, CDBs/LCI/LCA Bradesco e Corretora Ágora.
"""

# Lista de frases que farão o programa fechar
PALAVRAS_SAIDA = ["sair", "encerrar atendimento", "obrigado e até mais", "tchau", "encerrar", "finalizar"]

historico_conversa = [{"role": "system", "content": SYSTEM_PROMPT}]

def ouvir_microfone():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True 

    with sr.Microphone() as source:
        print("\n>>> Consultor Bradesco ouvindo... (Diga 'Sair' para encerrar)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            print(">>> Processando fala...")
            
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            
            with open("temp_audio.wav", "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
            return transcript.text

        except Exception as e:
            return None

def pensar_com_gpt(texto_entrada):
    global historico_conversa
    historico_conversa.append({"role": "user", "content": texto_entrada})
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=historico_conversa,
        temperature=0.5
    )
    
    resposta_texto = response.choices[0].message.content
    historico_conversa.append({"role": "assistant", "content": resposta_texto})
    return resposta_texto

def falar(texto_resposta):
    try:
        tts = gTTS(text=texto_resposta, lang='pt-br')
        arquivo_audio = "resposta_consultor.mp3"
        tts.save(arquivo_audio)
        print(f"\nCONSULTOR BRADESCO: {texto_resposta}")
        playsound.playsound(arquivo_audio)
        os.remove(arquivo_audio)
    except Exception as e:
        print(f"Erro de áudio: {e}")

# --- Fluxo de Execução com Verificação de Saída ---
if __name__ == "__main__":
    print("="*50)
    print("SISTEMA DE CONSULTORIA BRADESCO INICIADO")
    print("="*50)
    
    while True:
        pergunta = ouvir_microfone()
        
        if pergunta:
            print(f"VOCÊ DISSE: {pergunta}")
            
            # VERIFICAÇÃO DE SAÍDA:
            # Transformamos em minúsculo e removemos o ponto final para comparar
            if pergunta.lower().strip().replace(".", "") in PALAVRAS_SAIDA:
                despedida = "O Bradesco agradece o seu contato. Tenha ótimos investimentos e até a próxima!"
                falar(despedida)
                print("\n>>> Atendimento finalizado com sucesso.")
                break # Sai do loop While
            
            # Se não for saída, segue o fluxo normal
            resposta = pensar_com_gpt(pergunta)
            falar(resposta)