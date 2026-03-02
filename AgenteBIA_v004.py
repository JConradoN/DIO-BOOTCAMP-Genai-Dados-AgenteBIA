from openai import OpenAI
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time

# 1. Configuração do Cliente
client = OpenAI(api_key="SUA_CHAVE_AQUI")

# 2. Contexto Restritivo
SYSTEM_PROMPT = """
Você é a BIA, assistente do Bradesco e especialista em Benjamin Graham.
REGRAS CRÍTICAS DE RESPOSTA:
1. Seja extremamente concisa e direta. 
2. Suas respostas devem ter no máximo 6 frases.
3. Não dê explicações históricas a menos que solicitado.
4. Vá direto à recomendação de ativos Bradesco/Ágora.
5. Use linguagem objetiva e evite saudações repetitivas em cada resposta.
"""

PALAVRAS_SAIDA = ["sair", "encerrar atendimento", "obrigado e até mais", "tchau", "encerrar", "finalizar", "obrigado"]

historico_conversa = [{"role": "system", "content": SYSTEM_PROMPT}]

def falar(texto_resposta, nome_arquivo="resposta.mp3"):
    """Transforma texto em fala e reproduz o áudio"""
    try:
        tts = gTTS(text=texto_resposta, lang='pt-br')
        tts.save(nome_arquivo)
        print(f"\nBIA: {texto_resposta}")
        playsound.playsound(nome_arquivo)
        os.remove(nome_arquivo)
    except Exception as e:
        print(f"Erro de áudio: {e}")

def boas_vindas():
    """Saudação inicial da BIA"""
    mensagem = "Olá, eu sou a atendente BIA do Bradesco, em que posso te ajudar hoje?"
    falar(mensagem, "boas_vindas.mp3")

def ouvir_microfone():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True 

    with sr.Microphone() as source:
        print("\n[BIA está ouvindo...]")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        
        try:
            # Tempo de espera ligeiramente menor para ser mais dinâmico
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=12)
            
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            
            with open("temp_audio.wav", "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
            return transcript.text
        except Exception:
            return None

def pensar_com_gpt(texto_entrada):
    global historico_conversa
    historico_conversa.append({"role": "user", "content": texto_entrada})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=historico_conversa,
            temperature=0.5, # Reduzi para 0.3 para ser ainda mais objetiva
            max_tokens=250   # Limite físico de palavras para evitar textos longos
        )
        
        resposta_texto = response.choices[0].message.content
        historico_conversa.append({"role": "assistant", "content": resposta_texto})
        return resposta_texto
    except Exception as e:
        return "Erro de conexão com o sistema financeiro."

# --- Fluxo Principal ---
if __name__ == "__main__":
    print("="*50)
    print("INICIALIZANDO ATENDIMENTO BIA BRADESCO")
    print("="*50)
    
    # Passo 1: BIA se apresenta
    boas_vindas()
    
    # Passo 2: Entra no loop de conversação
    while True:
        pergunta = ouvir_microfone()
        
        if pergunta:
            print(f"VOCÊ: {pergunta}")
            
            # Verificação de Saída
            if any(palavra in pergunta.lower() for palavra in PALAVRAS_SAIDA):
                despedida = "O Bradesco e a BIA agradecem. Invista com segurança e até logo!"
                falar(despedida)
                break
            
            # Processamento normal
            resposta = pensar_com_gpt(pergunta)
            falar(resposta)
        else:
            # Caso o usuário fique em silêncio por muito tempo
            print("... (Aguardando interação)")