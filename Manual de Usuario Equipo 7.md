Manual de Usuario 
Equipo7
  -Samuel Morán Castro
  -Juan Giovanni Rodríguez Castillo
  -Pérez Lozano Andrés 
  -Pérez Soto Laura

Introducción
La API permite brindar información sobre los cursos que se imparten, así como agregar materias, eliminar y modificar su iformación. 

Endpoints y Funcionalidades

Usuarios

Insertar una nueva materia.
Endpoint: /curso
Método: POST
Descripción: Agrega una nueva materia en la base de datos.
Parámetros JSON:
{
"claveAsignatura": int, 
"nombreAsignatura": String,
"grupo": int, 
"profesor": String, 
"salon": String, 
"dia": int, 
"hora": String, 
"lugaresDisponibles: int"
}
Respuesta Exitosa:
{
  "mensaje": "Curso registrado"
}

Listar todos los cursos
Endpoint: /curso
Método: GET
Descripción: Regresa la lista de todos los cursos.
Respuesta Exitosa:
{
    "mensaje": "Curso encontrado",
    "cursos": [
        {"idAsignaturas": int,
          "claveAsignatura": int, 
          "nombreAsignatura": String,
          "grupo": int, 
          "profesor": String, 
          "salon": String, 
          "dia": int, 
          "hora": String, 
          "lugaresDisponibles: int"}
    ],
}

Actualizar un curso
Endpoint: /curso/<int:codigo>
Método: PUT
Descripción: Actualiza la información de un curso  existente.
Parámetros JSON:
{
  "codigo": int
}
Respuesta Exitosa:
{
  "mensaje": "Se ha actualizado"
}

Eliminar un usuario
Endpoint: /usuarios/<int:codigo>
Método: DELETE
Descripción: Elimina un curso de la base de datos.
Respuesta Exitosa:
{
  "mensaje": "Se ha eliminado"
}
Código de Respuesta: 200 OK

Comandos para la ejecución del Servidor
.\env\Scripts\activate
python .\src\app.py
