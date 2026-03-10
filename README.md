# 🧠 VisageID — Biometric Authentication System
### Computer Vision & Security Infrastructure

O **VisageID** é um sistema de alta integridade focado em autenticação biométrica facial. Diferente de sistemas de login convencionais, ele utiliza **Deep Learning** para transformar características fisiológicas em vetores numéricos únicos, garantindo uma camada de segurança baseada em **Identidade Biométrica**.

---

### 🚀 Diferenciais Técnicos

Diferente de uma simples captura de imagem, o VisageID implementa um pipeline de visão computacional robusto:

* **Extração de Encodings 128D:** Utiliza redes neurais residuais (**ResNet**) para converter faces em vetores matemáticos, permitindo comparações baseadas em Distância Euclidiana.
* **Threshold de Precisão:** Calibragem de sensibilidade para equilíbrio entre Falsos Positivos e Falsos Negativos (FAR/FRR).
* **Processamento em Tempo Real:** Integração direta com **OpenCV** para buffer de vídeo e captura de frames otimizada.
* **Arquitetura Segura:** Controle de sessão via **Flask-Login** com persistência em banco de dados relacional.

---

### 🛠️ Stack Tecnológica

* **Engine de IA:** `face_recognition` (Dlib/C++) — Reconhecimento facial de alta precisão.
* **Processamento de Imagem:** `OpenCV` — Manipulação de frames e streams de vídeo.
* **Backend:** `Python 3.10` + `Flask` — Micro-framework de alta performance.
* **ORM/Banco de Dados:** `SQLAlchemy` + `SQLite` — Integridade de dados e mapeamento relacional.
* **Ambiente:** `Anaconda` — Gestão isolada de dependências de Visão Computacional.

---

### 🗂️ Estrutura de Diretórios

```text
visageid/
├── captured_images/        # Imagens capturadas durante o registro
├── instance/
│   └── tasks.db            # Banco de dados SQLite
├── static/
│   ├── css/                # Design System customizado
│   └── js/                 # Handlers de captura (login.js, register_capture.js)
├── templates/              # Camada de visualização (base, login, register, tasks)
├── app.py                  # Core Engine e rotas da aplicação Flask
└── README.md
⚙️ Instalação e Deploy (Ambiente Conda)
1️⃣ Provisionamento do Ambiente:

Bash
conda create -n visageid python=3.10
conda activate visageid
2️⃣ Instalação de Dependências:

Bash
pip install -r requirements.txt
3️⃣ Inicialização da Engine:

Bash
python app.py
🔐 Fluxo de Autenticação
Captura: O sistema detecta landmarks faciais via OpenCV.

Vetorização: A face é convertida em um array numérico de 128 dimensões.

Comparação: O motor calcula a distância matemática entre o encoding atual e o armazenado.

Verificação: Se a distância for inferior ao threshold de segurança (0.6), o acesso é concedido.

👤 Autor
Ricardo Nogueira — Computer Engineer
Especialista em Integração de Visão Computacional e Arquiteturas Full Stack.

📄 Licença
Este projeto está sob a Licença MIT. Sinta-se à vontade para utilizar, modificar e distribuir, mantendo a atribuição original de autoria.
