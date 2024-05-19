from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Materias', methods=['POST'])
def Materias():
    if request.method == 'POST':
        cicloEscolar = request.form['Ciclo escolar']
        semestre = request.form['Semestre']
        carrra = request.form['Carrera']
        print(cicloEscolar)
        print(semestre)
        print(carrra)
        return 'Recibido'

if __name__ == '__main__':
    app.run(port= 3000, debug=True)  