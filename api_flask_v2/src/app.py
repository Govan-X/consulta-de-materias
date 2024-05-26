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

@app.route('/cursos', methods=['GET'])    
def leer curso(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT idAsignaturas, claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0], 'claveAsignatura': claveAsignatura[1], 'nombreAsignatura': nombreAsignatura[2], 'grupo': grupo[3], 'profesor': grupo[4], 'salon': salon, 'dia': dia[5], 'hora': hora[6], 'lugaresDisponibles': lugaresDisponibles[7]}
            return jsonify({'curso': Curso, 'mensaje': "Curso encontrado"})
        else:
            return jsonify({'mensaje': "Curso no encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': error})

@app.route('/cursos', methods=['POST'])
def registrar_curso():
    try: 
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO curso(idAsignaturas, claveAsignatura, nombreAsignatura, grupo, profesor, salon, dia, hora, lugaresDisponibles) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}')""".format(request.json['codigo'],
        request.json['nombreAsignatura'], request.json['creditos'])
        cursor.execute(sql)
        conexion.connection.commit() #confirma la asersión.
        return jsonify({'mensaje': "Curso registrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


    
#Metodo PUT (Actualizar)
@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    try:
        cursor = mysql.connection.cursor()
        sql = """UPDATE curso SET nombre = ´{0}´, WHERE codigo = '{1}'""".format(request.json['nombre'],codigo)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'mensaje': "Se ha actualizado."})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR"})

#Metodo DELETE (Eliminar)
@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        cursor = mysql.connection.cursor()
        sql = "DELETE FROM curso WHERE codigo = '{}'".format(codigo)
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