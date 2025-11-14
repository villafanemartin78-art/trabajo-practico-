# trabajo-practico-

# antes de iniciarse el proyecto en flask debe/n instalarse:
flask-cors --> pip install flask-cors

Comentario: para iniciar las paginas se debe inicializar el archivo "iniciar_pagina.sh"

Base de datos:
La base de datos está diseñada siguiendo principios de normalización, permitiendo que un cliente pueda realizar múltiples reservas, gestionar servicios adicionales, y mantener un historial ordenado y seguro. Consta de cuatro tablas principales:
1. alojamientos
Contiene toda la información de las cabañas disponibles en el sistema.
2. clientes
Guarda los datos de cada cliente que realiza reservas.
3. reservas
Registra cada reserva hecha por los clientes.
4. servicios_extras
Catálogo de servicios adicionales que se pueden ofrecer.
5. servicios_reserva
Tabla intermedia que conecta reservas con servicios extras.

El endpoint /api/reservas/<id_alojamiento> recibe un ID de alojamiento, busca en la base de datos todas las reservas de ese alojamiento que no estén canceladas, toma sus fechas de entrada y salida, convierte esas fechas al formato YYYY-MM-DD y devuelve una lista de eventos en formato JSON lista para ser usada por FullCalendar.
