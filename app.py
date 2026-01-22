# Importa o módulo Flask e funções relacionadas para criar a aplicação web
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# Importa o módulo SQLAlchemy para gerenciar o banco de dados
from flask_sqlalchemy import SQLAlchemy

# Importa módulos do Flask-Login para gerenciar a autenticação de usuários
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Importa módulos do Flask-WTF para criar e gerenciar formulários
from flask_wtf import FlaskForm

# Importa campos e validadores do WTForms para criar campos de formulário e validações
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Importa o módulo face_recognition para reconhecimento facial
import face_recognition

# Importa o módulo NumPy para manipulação de arrays
import numpy as np

# Importa o módulo base64 para codificação e decodificação de dados em base64
import base64

# Importa o módulo OpenCV para manipulação de imagens
import cv2

# Importa o módulo os para interações com o sistema operacional
import os

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Configura a chave secreta para a segurança da aplicação
app.config['SECRET_KEY'] = 'your_secret_key'

# Configura o URI do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Desativa o rastreamento de modificações do SQLAlchemy para economizar recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão SQLAlchemy com a aplicação Flask
db = SQLAlchemy(app)

# Inicializa o gerenciador de login com a aplicação Flask
login_manager = LoginManager(app)

# Define a rota de login padrão
login_manager.login_view = 'login'

# Diretório onde as imagens capturadas serão temporariamente armazenadas
CAPTURED_IMAGES_DIR = 'captured_images'

# Cria o diretório se ainda não existir
os.makedirs(CAPTURED_IMAGES_DIR, exist_ok=True)

# Modelo de dados para tarefas com campos id, título e descrição.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Modelo de dados para usuários com campos id, email e codificação facial.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    face_encoding = db.Column(db.PickleType, nullable=False)

# Função que busca e retorna um usuário do banco de dados pelo seu ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Formulário de registro com campos para email e botão de envio
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

# Formulário de login com campos para email e botão de envio
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Next')

# Converte uma string base64 em uma imagem para comparação com a imagem registrada
def base64_to_image(base64_str):
    # Decodifica a string base64 em dados binários
    decoded_data = base64.b64decode(base64_str.split(',')[1])
    # Converte os dados binários em um array NumPy
    np_data = np.frombuffer(decoded_data, np.uint8)
    # Decodifica o array NumPy em uma imagem usando OpenCV
    img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    return img

# Rota principal que exibe todas as tarefas para usuários logados
@app.route('/')
@login_required
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Rota para adicionar uma nova tarefa, acessível apenas para usuários logados
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_task.html')

# Rota para atualizar uma tarefa existente, acessível apenas para usuários logados
@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_task.html', task=task)

# Rota para deletar uma tarefa existente, acessível apenas para usuários logados
@app.route('/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Rota para registrar um novo usuário, exibindo o formulário de registro e processando o envio
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            flash('E-mail já registrado.', 'danger')
            return redirect(url_for('login'))
        return render_template('register_capture.html', email=email)
    return render_template('register.html', form=form)

# Rota que processa a captura e o registro do rosto do usuário após o envio do formulário de registro
@app.route('/register_capture', methods=['POST'])
def register_capture():
    data = request.json
    email = data['email']
    face_data = data['face_data']
    face_image = base64_to_image(face_data)
    face_encodings = face_recognition.face_encodings(face_image)
    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]

        # Extrai o nome do usuário e o domínio do email
        username, domain = email.split('@')

        # Define o caminho do diretório específico para o usuário
        user_dir = os.path.join(CAPTURED_IMAGES_DIR, domain, username)
        os.makedirs(user_dir, exist_ok=True)

        # Define o caminho para salvar a imagem capturada
        image_path = os.path.join(user_dir, 'face.jpg')

        # Salva a imagem capturada no arquivo
        cv2.imwrite(image_path, face_image)

        new_user = User(email=email, face_encoding=face_encoding)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Registro realizado com sucesso.', 'image_path': image_path})
    else:
        return jsonify({'status': 'failure', 'message': 'Nenhum rosto detectado.'})

# Rota para login do usuário, exibindo o formulário de login e processando o envio
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('login_capture.html', email=email)
        else:
            flash('Email não encontrado. Por favor, registre-se primeiro.', 'danger')
            return redirect(url_for('register'))
    return render_template('login.html', form=form)

# Rota que processa a captura do rosto durante o login, comparando com o rosto registrado
@app.route('/login_capture', methods=['POST'])
def login_capture():
    try:
        data = request.json
        email = data['email']
        face_data = data['face_data']
        face_image = base64_to_image(face_data)
        face_encodings = face_recognition.face_encodings(face_image)
        
        if len(face_encodings) > 0:
            face_encoding = face_encodings[0]
            user = User.query.filter_by(email=email).first()
            
            if user:
                matches = face_recognition.compare_faces([np.array(user.face_encoding)], face_encoding)
                
                if matches[0]:
                    login_user(user)
                    return jsonify({'status': 'success', 'message': 'Login bem-sucedido.', 'redirect': url_for('index')})
                else:
                    return jsonify({'status': 'failure', 'message': 'Rosto não corresponde.'})
            else:
                return jsonify({'status': 'failure', 'message': 'Usuário não encontrado.'})
        else:
            return jsonify({'status': 'failure', 'message': 'Nenhum rosto detectado.'})
    except Exception as e:
        print(f"Error during login_capture: {str(e)}")
        return jsonify({'status': 'failure', 'message': 'Ocorreu um erro.'})

# Rota para fazer logout do usuário, acessível apenas para usuários logados
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi desconectado.', 'success')
    return redirect(url_for('login'))

# Código para iniciar a aplicação Flask
if __name__ == '__main__':
    # Cria as tabelas no banco de dados se ainda não existirem
    with app.app_context():
        db.create_all()
    # Inicia o servidor Flask em modo de depuração
    app.run(debug=True)