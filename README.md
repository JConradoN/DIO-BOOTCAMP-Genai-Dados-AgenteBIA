# DIO-BOOTCAMP-Genai-Dados-AgenteBIA
🏦 Agente BIA: Inteligência Artificial de Investimentos (Bradesco & Graham)
Este repositório apresenta o desenvolvimento da BIA, uma assistente de voz inteligente criada como projeto prático para o Bootcamp de GenAI da DIO. O agente simula uma consultora de investimentos do Bradesco, operando sob as diretrizes da filosofia de Value Investing de Benjamin Graham.

🎯 Objetivo do Projeto
O objetivo principal foi construir um pipeline completo de IA conversacional (Voz-para-Texto e Texto-para-Voz) que não apenas transcreve áudio, mas aplica um contexto de negócio rígido e especializado para oferecer recomendações de investimentos seguras e fundamentadas em análise fundamentalista.

🚀 Evolução e Arquitetura do Código
O projeto está estruturado em versões que demonstram o amadurecimento da lógica e da experiência do usuário:

AgenteBIA_v001.py: Implementação do ciclo básico de STT (Speech-to-Text) via OpenAI Whisper e TTS (Text-to-Speech) via gTTS.

AgenteBIA_v002.py: Introdução da persona "Consultor Bradesco" e implementação de memória de curto prazo para manter o contexto da conversa.

AgenteBIA_v003.py: Adição de comandos de voz para encerramento de sessão e melhorias na captação de áudio ambiente.

AgenteBIA_v004.py (Versão Final): Refinamento de UX com saudação vocal inicial da BIA, restrição de verbosidade para respostas diretas e otimização de tokens.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.10+

Modelos de IA: OpenAI GPT-4o-mini (Processamento) e Whisper-1 (Transcrição).

Voz: gTTS (Google Text-to-Speech) para síntese e SpeechRecognition para captura.

Reprodução: Playsound para saída de áudio em tempo real.

📦 Como Executar
Clone o repositório:

Bash
git clone https://github.com/JConradoN/DIO-BOOTCAMP-Genai-Dados-AgenteBIA/
Instale as dependências:

Bash
pip install openai speechrecognition gtts playsound==1.2.2 pyaudio
Configure sua variável de ambiente OPENAI_API_KEY.

Execute a versão final:

Bash
python AgenteBIA_v004.py
👨‍💻 Autor
João Conrado V. Nogueira

LinkedIn: Conrado Nogueira

Bootcamp: Geração de IA e Dados - DIO

Nota: Este projeto possui fins estritamente educacionais e não constitui recomendação financeira real.

💡 Próximo Desafio: Interface Web
Com o motor Python finalizado, o próximo passo é a criação de um Dashboard em JavaScript para exibir o histórico de investimentos sugerido pela BIA visualmente.
