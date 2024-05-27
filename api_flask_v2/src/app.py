from flask import Flask, jsonify, request
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

@app.route('/cursos/<idAsignaturas>', methods=['GET'])    
def leer_curso(idAsignaturas):
    try:
        cursor= mysql.connection.cursor()
        sql = "SELECT idAsignaturas, claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles FROM asignaturas WHERE idAsignaturas = '{0}'".format(idAsignaturas)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            curso = {'idAsignaturas': datos[0], 'claveAsignatura': datos[1], 'nombreAsignatura':datos[2], 'grupo': datos[3], 'profesor': datos[4], 'salon': datos[5], 'dia': datos[6], 'hora': datos[7], 'lugaresDisponibles': datos[8]}
            return jsonify({'Asignatura': curso, 'mensaje': "Curso encontrado"})
        else:
            return jsonify({'mensaje': "Curso no encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/cursos/idAsignaturas', methods=['POST'])
def registrar_curso():
    try: 
        #print(request.json)
        cursor= mysql.connection.cursor()
        sql="""INSERT INTO asignaturas(claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')""".format(request.json['claveAsignatura'], request.json['nombreAsignatura'],
                request.json['grupo'], request.json['profesor'], request.json['salon'], request.json['dia'], request.json['hora'], request.json['lugaresDisponibles'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la asersión.
        return jsonify({'mensaje': "Curso registrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})
 
#Metodo PUT (Actualizar)
@app.route('/cursos/<idAsignaturas>', methods=['PUT'])
def actualizar_curso():
    try:
        cursor = mysql.connection.cursor()
        sql = """UPDATE asignaturas SET nombre = ´{0}´, WHERE idAsignaturas = '{1}'""".format(request.json['nombre'],codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'mensaje': "Se ha actualizado."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR"})

#Metodo DELETE (Eliminar)
@app.route('/cursos/<idAsignaturas>', methods=['DELETE'])
def eliminar_curso(idAsignaturas):
    try:
        cursor = mysql.connection.cursor()
        sql = "DELETE FROM asignaturas WHERE idAsignaturas = '{}'".format(idAsignaturas)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'mensaje': "Se ha eliminado."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR"})

#Pagina no encontrada
def pagina_no_encontrada(error):
    return "<h1>Lo sentimos, esta página no existe... :(</h1>"

if __name__ == '__main__':
    
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()