from openai import OpenAI
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# 1. Configuração do Cliente
# Lembre-se de manter sua chave em segurança!
client = OpenAI(api_key="SUA_CHAVE_AQUI")

# 2. Definição do Contexto (Role-play)
SYSTEM_PROMPT = """
Você é um Consultor de Investimentos sênior do Bradesco, especializado na filosofia de Benjamin Graham.
Seu objetivo é ajudar o cliente a construir uma carteira sólida e segura.

Diretrizes:
1. Use os princípios de 'Margem de Segurança' e diferencie preço de valor.
2. Recomende produtos Bradesco: Para conservadores, foque em CDBs, LCI e LCA do banco. 
3. Para renda variável, mencione a corretora Ágora (do grupo Bradesco) e análise de dividendos.
4. Linguagem: Seja extremamente cordial, profissional e use termos bancários brasileiros adequados.
5. Sempre comece a primeira resposta saudando o cliente como consultor Bradesco.
"""

# Inicializa o histórico com a instrução do sistema
historico_conversa = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def ouvir_microfone():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True 

    with sr.Microphone() as source:
        print("\n>>> Consultor Bradesco ouvindo... (Pode falar)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=12)
            print(">>> Gravado! Analisando sua fala...")
            
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            
            with open("temp_audio.wav", "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
            return transcript.text

        except Exception as e:
            print(f"Erro na captação: {e}")
            return None

def pensar_com_gpt(texto_entrada):
    global historico_conversa
    
    # Adiciona a fala do usuário ao histórico
    historico_conversa.append({"role": "user", "content": texto_entrada})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=historico_conversa,
            temperature=0.5 # Equilíbrio entre criatividade e rigor técnico
        )
        
        resposta_texto = response.choices[0].message.content
        
        # Adiciona a resposta da IA ao histórico para manter o contexto
        historico_conversa.append({"role": "assistant", "content": resposta_texto})
        
        return resposta_texto
    except Exception as e:
        return f"Desculpe, tive um problema ao acessar meus sistemas bancários: {e}"

def falar(texto_resposta):
    try:
        tts = gTTS(text=texto_resposta, lang='pt-br')
        arquivo_audio = "resposta_consultor.mp3"
        tts.save(arquivo_audio)
        
        print(f"\nCONSULTOR BRADESCO: {texto_resposta}")
        playsound.playsound(arquivo_audio)
        
        os.remove(arquivo_audio)
    except Exception as e:
        print(f"Erro ao reproduzir áudio: {e}")

# --- Fluxo de Execução ---
if __name__ == "__main__":
    print("="*50)
    print("SISTEMA DE CONSULTORIA BRADESCO - FILOSOFIA GRAHAM")
    print("="*50)
    
    try:
        while True:
            pergunta = ouvir_microfone()
            
            if pergunta:
                print(f"VOCÊ: {pergunta}")
                
                # O GPT agora usa o histórico completo
                resposta = pensar_com_gpt(pergunta)
                falar(resposta)
                
    except KeyboardInterrupt:
        print("\nAtendimento encerrado pelo usuário. Tenha um ótimo dia de investimentos!")