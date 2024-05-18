from flask import Flask
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

@app.route('/cursos')
def listar_cursos():
    try: 
        return "Cursos listados"
    except Exception as ex: 
        return "Error"
    
def pagina_no_encontrada(error):
    return "<h1>Lo sentimos, esta página no existe... :(</h1>"

if __name__ == '__main__':
    
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
    
