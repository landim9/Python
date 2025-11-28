from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Lista para armazenar as tarefas em memória
tarefas = []
contador_id = 1

@app.route('/')
def index():
    total = len(tarefas)
    concluidas = len([t for t in tarefas if t['concluida']])
    pendentes = total - concluidas
    
    return render_template(
        'index.html', 
        tarefas=tarefas,
        total=total,
        concluidas=concluidas,
        pendentes=pendentes
    )

@app.route('/adicionar', methods=['POST'])
def adicionar():
    global contador_id
    titulo = request.form.get('titulo')
    
    if titulo:
        tarefa = {
            'id': contador_id,
            'titulo': titulo,
            'concluida': False,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        tarefas.append(tarefa)
        contador_id += 1
    
    return redirect(url_for('index'))

@app.route('/concluir/<int:tarefa_id>', methods=['POST'])
def concluir(tarefa_id):
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['concluida'] = True
            break
    
    return redirect(url_for('index'))

@app.route('/deletar/<int:tarefa_id>', methods=['POST'])
def deletar(tarefa_id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != tarefa_id]
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)