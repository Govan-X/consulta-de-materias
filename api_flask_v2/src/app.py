from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
#conexion = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'asignaturasdb'

mysql = MySQL(app)

@app.route('/cursos')
def listar_cursos():
    try:
        cursor = mysql.connection.cursor()
        #cursor.execute("SELECT * FROM asignaturas")
        sql = "SELECT claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles FROM asignaturas"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos=[]
        for fila in datos:
            curso={'claveAsignatura': fila[0], 'nombreAsignatura': fila[1], 'grupo': fila[2], 'profesor': fila[3], 'salon': fila[4], 'dia': fila[5], 'hora': fila[6], 'lugaresDisponibles': fila[7]}
            cursos.append(curso)
        #print(datos)
        #cursor.close()
        #return "Cursos listados"
        return jsonify({'cursos': cursos, 'mensaje':"Cursos listados."})
    except Exception as ex: 
        return "Error"
    
def pagina_no_encontrada(error):
    return "<h1>Lo sentimos, esta página no existe... :(</h1>"

if __name__ == '__main__':
    
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
    
