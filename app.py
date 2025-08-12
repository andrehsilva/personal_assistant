from flask import Flask, render_template

# Inicializa o aplicativo Flask
app = Flask(__name__)

@app.route('/')
def index():
    """ Rota principal que renderiza a página do assistente. """
    return render_template('index.html')

if __name__ == '__main__':
    # Executa o aplicativo em modo de depuração para facilitar o desenvolvimento
    app.run(debug=True)