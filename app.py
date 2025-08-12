# app.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)

# IMPORTANTE: Chave secreta para gerenciar as sessões de login.
# O Flask usa isso para manter os dados da sessão seguros.
# Troque esta string por qualquer outra combinação de caracteres aleatórios.
app.secret_key = os.urandom(24) 

# --- ROTAS DE AUTENTICAÇÃO ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se o formulário for enviado (método POST)
    if request.method == 'POST':
        # Pega a senha digitada no formulário
        password = request.form.get('password')
        
        # Verifica se a senha está correta
        if password == 'hugoeisis':
            # Se correta, marca o usuário como 'logado' na sessão
            session['logged_in'] = True
            # Redireciona para a página principal
            return redirect(url_for('home'))
        else:
            # Se incorreta, mostra uma mensagem de erro
            flash('Senha incorreta. Tente novamente.')
            
    # Se for o primeiro acesso (método GET) ou se a senha estiver errada,
    # apenas mostra a página de login.
    return render_template('login.html')


@app.route('/logout')
def logout():
    # Remove a marcação de 'logado' da sessão
    session.pop('logged_in', None)
    # Redireciona para a página de login
    return redirect(url_for('login'))


# --- ROTA PRINCIPAL PROTEGIDA ---

@app.route('/')
def home():
    # Verifica se o usuário está marcado como 'logado' na sessão
    if 'logged_in' in session:
        # Se estiver logado, mostra a página principal
        return render_template('index.html')
    else:
        # Se não estiver logado, redireciona para a tela de login
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)