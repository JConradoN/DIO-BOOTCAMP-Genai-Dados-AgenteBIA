# DIO-BOOTCAMP-Genai-Dados-AgenteBIA
🏦 BIA: Inteligência Artificial de Investimentos (Bradesco & Graham)
BIA é uma assistente de voz inteligente inspirada na atendente virtual do Bradesco, mas com um "cérebro" treinado na filosofia de Benjamin Graham (Value Investing). O projeto demonstra a integração de tecnologias de ponta para criar uma experiência de consultoria financeira ágil, segura e vocalizada.

📖 Sobre o Projeto
Este projeto foi desenvolvido como parte de um desafio prático de IA Conversacional. O objetivo é simular um atendimento bancário onde a IA:

Escuta o usuário através do microfone.

Transcreve a fala com alta precisão usando o modelo Whisper.

Processa a intenção baseando-se em um contexto rígido de consultor financeiro.

Responde via voz sintetizada com recomendações diretas de ativos (CDB, LCI, LCA e Ágora).

🛠️ Tecnologias e Dependências
Para rodar este projeto, as seguintes bibliotecas são necessárias:

OpenAI SDK: Interface com os modelos GPT-4o-mini e Whisper.

SpeechRecognition: Captura de áudio do hardware.

PyAudio: Gerenciamento de streams de áudio.

gTTS (Google Text-to-Speech): Conversão de texto em áudio MP3.

Playsound: Reprodução multiplataforma dos arquivos de áudio.

📈 Changelog (Histórico de Evolução)
O projeto está organizado em 4 fases, refletindo o aprendizado e refinamento do código:

v1.0 - Fundação (Projeto 1.py)
Implementação do loop básico de STT (Speech-to-Text) e TTS (Text-to-Speech).

Integração com a nova sintaxe da API OpenAI (v1.0+).

Configuração do reconhecimento de ruído ambiente para melhorar a captura.

v2.0 - Especialização e Memória (Projeto 2.py)
Criação do System Prompt focado em Benjamin Graham e Bradesco.

Implementação de Histórico de Conversa, permitindo que a IA mantenha o contexto de perguntas anteriores na mesma sessão.

v3.0 - Controle de Sessão (Projeto 3.py)
Adição de filtros de saída por voz (Keywords de encerramento).

Aumento do tempo de limite de frase (phrase_time_limit) para permitir perguntas complexas.

Tratamento de exceções para capturas de áudio vazias.

v4.0 - UX e Polimento (Projeto 4.py)
Introdução Vocal: BIA se apresenta formalmente ao iniciar.

Restrição de Verbosidade: Ajuste no prompt para respostas curtas (máx. 6 frases) e diretas.

Ajuste de Temperatura: Redução da temperatura para 0.5, garantindo respostas técnicas e factuais.

Gestão de Arquivos: Nomes dinâmicos para arquivos temporários de áudio para evitar conflitos de leitura/escrita.

🚀 Como Instalar e Rodar
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/bia-investimentos-ia.git
cd bia-investimentos-ia
Instale as dependências:

Bash
pip install openai speechrecognition gtts playsound==1.2.2 pyaudio
Variáveis de Ambiente:
Não exponha sua chave no código. No Windows, configure assim:

DOS
setx OPENAI_API_KEY "sua_chave_aqui"
Execução:

Bash
python "Projeto 4.py"
⚖️ Licença e Créditos
Projeto desenvolvido como desafio para o Bootcamp DIO.

IA: OpenAI (GPT & Whisper).

Voz: Google TTS.

Metodologia: Benjamin Graham (The Intelligent Investor).

💡 Próximo Desafio: Interface Web
Com o motor Python finalizado, o próximo passo é a criação de um Dashboard em JavaScript para exibir o histórico de investimentos sugerido pela BIA visualmente.
