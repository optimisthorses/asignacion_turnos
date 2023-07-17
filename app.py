from flask import Flask, request
import pymysql
from flask import Flask, request, render_template

app = Flask(__name__)

# Ruta para guardar el turno
@app.route("/guardar_turno", methods=["POST"])
def guardar_turno():
    tipo = request.form.get("tipo")

    # Establecer la conexión a la base de datos
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="w83aJSWWfVLzE6",
        db="turnos_con_prioridad"
    )

    try:
        # Crear un cursor para ejecutar las consultas
        cursor = connection.cursor()

        # Ejecutar la consulta de inserción
        sql = "INSERT INTO usuarios (prioridad) VALUES (%s)"
        values = (tipo,)
        cursor.execute(sql, values)

        # Confirmar los cambios en la base de datos
        connection.commit()

        # Obtener el turno insertado
        turno = cursor.lastrowid

        # Cerrar el cursor
        cursor.close()

        # Devolver el turno como respuesta a la solicitud
        return str(turno)
    except Exception as e:
        # En caso de error, deshacer los cambios
        connection.rollback()
        print("Error durante la inserción:", str(e))
    finally:
        # Cerrar la conexión a la base de datos
        connection.close()

    return "Error durante la inserción"
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()