from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__,template_folder='src/templates',static_folder='src/static')

#Variáveis de ambiente 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidatos.db'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 *1024 * 1024
ALLOWED_EXTENSIONS = {'pdf'}

@app.route('/')
def home():
    return render_template('index.html') 
#Inicialização do banco de dados
db = SQLAlchemy(app)

#Função Auxiliar para validar o arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#Modelo de banco de dados
class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    arquivo_curriculo = db.Column(db.String(200))


#ENDPOINT
@app.route('/trabalhe-conosco')
def trabalhe_conosco():
    return render_template('cadastro.html')

#Rota para processar o envio do formulário
@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']


    if 'curriculo' not in request.files:
        return "Nenhum arquivo encontrado", 400
    
    file = request.files['curriculo']

    if file.filename == '':
        return "Nenhum arquivo selecionado",400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(caminho)

        #Salvar o banco de dados
        candidato = Candidato(nome=nome, email=email, arquivo_curriculo=caminho)
        db.session.add(candidato)
        db.session.commit()

        return"Curriculo enviado com sucesso!"
    else:
        return "Arquivo inválido, enviei um PDF",400 
    


#Inicializar o app   
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

    



    
    




