# antes de iniciarse el proyecto en flask deben instalarse:
- flask_mail --> pip install flask_mail
- requests --> pip install requests
- flask-cors --> pip install flask-cors

**variable cabins recibe lo obtenido del endpoint /api/cabanas por lo tanto guarda toda la información de la tabla alojamientos**
**variable experiencias recibe lo obtenido del endpoint /api/servicios por lo tanto guarda toda la información de la tabla servicios_extras**

# Endpoints del frontend: 
1. **/ :** <mark>(se usa en el template index.html)</mark> a través de la funcion index pasa la información que recibe del backend de los alojamientos(la variable cabins), de los servicios extra(variables experiencias) y de las opiniones de los huespedes(variable ...) para ser usados en el frontend de el template index.html, además de renderizarlo usando la librería render_template
2. **/cabañas :** <mark>(se usa en el template nuestras_cabañas.html)</mark> a través de la función **cabañas** pasa la información que recibe del backend de los alojamientos(la variable cabins), para ser usados en el frontend del template nuestras_cabañas.html además de renderizarlo usando la librería render_template
3. **/reservar/<cabin_slug> :** <mark>(se usa en el template reservar_cabaña.html)</mark> a través de la función reservar_cabaña
4. **/mis_reservas :** <mark>(se usa en el template mis_reservas.html)</mark>
5. **/cancelar_reserva :** <mark>(se usa en el template mis_reservas.html)</mark>a través de la función cancelar_reserva va a obtener el id_reserva del form, manda ese id al backend e intenta cancelar con endpoint del backend
6. **/datos_reserva :** <mark>(se usa en el template reservar_cabaña.html)</mark>a través de la funcion datos_reserva va a validar si todos los campos del form están completos 
7. **/procesar_reserva :** <mark>(se usa en confirmacion_reserva_email.html)</mark>
8. **/pagar_reserva :** <mark>(se usa en el template mis_reservas.html)</mark> se comunica con /api/reservas/pagar/<int:id_reserva>, cambia el estado de la reserva a confirmado 

