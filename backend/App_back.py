from flask import Flask, jsonify
from flask_cors import CORS
from db import get_conexion 
#Se debe instalar Flask-CORS 
#para permitir llamadas desde el puerto 5002
#Comando en bash: pip install flask-cors

app = Flask(__name__)
CORS(app) 
#Habilitar CORS para permitir que el Frontend (puerto 5002) llame a este Backend (puerto 5003)

#ENDPOINT 
@app.route('/api/cabanas', methods=['GET'])
def get_cabanas():
    conn = get_conexion()      # Crea la conexión a MYSQL
    cursor = conn.cursor(dictionary=True)  # Crea un “cursor” para ejecutar consultas sql
    cursor.execute("""
        SELECT 
            id_alojamiento AS id,
            nombre,
            direccion,
            ciudad,
            pais,
            precio_noche,
            capacidad,
            descripcion
        FROM alojamientos;
    """)
    alojamientos = cursor.fetchall()  # Obtiene todos los resultados de la consulta
    cursor.close()                   # Cierra el cursor
    conn.close()                     # Cierra la conexión a la base de datos

    return jsonify(alojamientos)     # Devuelve los resultados como JSON

@app.route('/api/reservas/<int:id_alojamiento>', methods=['GET']) #captura un entero desde la URL y lo pasa a la función como id_alojamiento
def obtener_reservas_alojamiento(id_alojamiento):

    conn = get_conexion()
    cursor = conn.cursor(dictionary=True) #hace que los resultados salgan como diccionario

    cursor.execute("""                             
        SELECT fecha_entrada, fecha_salida 
        FROM reservas
        WHERE id_alojamiento = %s
          AND estado <> 'cancelada';
    """, (id_alojamiento,))    #Busca todas las reservas del alojamiento indicado. solo trae fecha_entrada y fecha_salida y filtra para no traer las canceladas

    reservas = cursor.fetchall() # lee todas las filas que devolvio el sql

    cursor.close()
    conn.close() # cierra el cursor y la conexion 

    # Convertimos al formato FullCalendar
    eventos = []
    for r in reservas:
        eventos.append({
            "title": "Reservado",
            "start": r["fecha_entrada"].strftime("%Y-%m-%d"),
            "end": r["fecha_salida"].strftime("%Y-%m-%d"),
            "display": "block",
            "color": "#FF5252",
            "className": "reserved-event"
        })  # Convierte fecha_entrada y fecha_salida a texto con formato YYYY-MM-DD

    return jsonify(eventos)

@app.route('/api/reservas/cancelar/<int:id_reserva>', methods=['POST'])
def cancelar_reserva(id_reserva):

    conn = get_conexion()
    cursor = conn.cursor(dictionary=True)

    # verificar que exista
    cursor.execute("""
        SELECT estado 
        FROM reservas 
        WHERE id_reserva = %s;
    """, (id_reserva,))  # Consulta la columna estado de la fila con id_reserva dado. Se usa placeholder %s para seguridad.
    
    reserva = cursor.fetchone() #devuelve el primer resultado o none si no hay nada

    if not reserva:
        cursor.close()
        conn.closey 
        return jsonify({"error": "Reserva no encontrada"}), 404
                            #si no encuentra nada se cierra el cursor y la conexion y devuelve "error" reserva no encontrada y ponemos un error 404
    
    # actualizar estado
    cursor.execute("""
        UPDATE reservas
        SET estado = 'cancelada'
        WHERE id_reserva = %s;
    """, (id_reserva,))   #usamos la sentencia UPDATE para modificar el estado a "cancelada" 
    
    conn.commit() #confirmamos el cambia a la base de datos, sin esto no se agregaria

    cursor.close()
    conn.close()

    return jsonify({"message": "Reserva cancelada correctamente"}), 200 #Devuelve un JSON con mensaje de confirmación y código HTTP 200 (OK).



if __name__ == '__main__':

    app.run(port=5003, debug=True)

