🧠 VisageID — Sistema de Autenticação Facial

Um projeto acadêmico de Ricardo nogueira

Seja bem-vindo(a) ao repositório do VisageID, um sistema web desenvolvido como Trabalho de Conclusão de Curso (TCC), focado em autenticação de usuários por reconhecimento facial, unindo visão computacional, segurança e desenvolvimento web.

🎯 Objetivo do Projeto

O VisageID tem como objetivo demonstrar a aplicação prática de reconhecimento facial em sistemas web, permitindo:

Cadastro de usuários com captura facial

Autenticação segura por comparação de rostos

Controle de acesso a funcionalidades protegidas

Gerenciamento simples de tarefas após login

O projeto explora conceitos de visão computacional, processamento de imagens, segurança e engenharia de software.

```
🗂️ Estrutura de Diretórios
visageid/
├── captured_images/        # Imagens capturadas durante o registro
├── instance/
│   └── tasks.db            # Banco de dados SQLite
├── static/
│   ├── css/
│   │   └── styles/         # Estilos da aplicação
│   └── js/
│       ├── login.js
│       └── register_capture.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create_task.html
│   ├── login.html
│   ├── login_capture.html
│   ├── register.html
│   └── register_capture.html
├── app.py                  # Arquivo principal da aplicação Flask
└── README.md
```
🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando:

🐍 Python

🌐 Flask — Framework web

🗄️ Flask-SQLAlchemy — ORM para banco de dados

🔐 Flask-Login — Autenticação de usuários

📝 Flask-WTF / WTForms — Formulários e validação

👁️ face_recognition — Reconhecimento facial

📷 OpenCV — Manipulação de imagens

🔢 NumPy — Processamento numérico

🗃️ SQLite — Banco de dados local

🧪 Anaconda (ambiente de desenvolvimento)

🧪 Ambiente de Desenvolvimento

O projeto foi desenvolvido utilizando Anaconda, devido à facilidade no gerenciamento
de dependências relacionadas à visão computacional.

⚠️ Observação:
O uso do Anaconda não é obrigatório. O projeto também pode ser executado com venv e pip,
desde que todas as dependências estejam corretamente instaladas.

▶️ Como Executar o Projeto
🔹 Usando Anaconda (recomendado)

1️⃣ Clone o repositório:
```
git clone <URL_DO_REPOSITORIO>
```

2️⃣ Acesse o diretório:
```
cd visageid
```

3️⃣ Crie o ambiente:
```
conda create -n visageid python=3.10
```

4️⃣ Ative o ambiente:
```
conda activate visageid
```

5️⃣ Instale as dependências:
```
pip install -r requirements.txt
```

6️⃣ Execute a aplicação:
```
python app.py
```

7️⃣ Acesse no navegador:
```
http://127.0.0.1:5000
```
🔐 Funcionalidades

✔️ Registro de usuário com captura facial

✔️ Login por reconhecimento facial

✔️ Comparação de rosto em tempo real

✔️ Controle de sessão com Flask-Login

✔️ CRUD de tarefas protegido por autenticação

✔️ Armazenamento seguro de codificação facial

📚 Contexto Acadêmico

Este projeto foi desenvolvido como Trabalho de Conclusão de Curso (TCC), com foco em:

Visão Computacional

Segurança da Informação

Desenvolvimento Web

Aplicação prática de algoritmos de reconhecimento facial

👨‍💻 Autor

Desenvolvido com dedicação por
Ricardo Nogueira
🔗 GitHub: https://github.com/slepdesenvolve

📄 Licença

Este projeto é de caráter acadêmico e educacional.
Sinta-se à vontade para estudar, adaptar e evoluir o código.
