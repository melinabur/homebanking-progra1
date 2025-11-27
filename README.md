# homebanking-progra1
Proyecto Final – Home Banking en Python

Nuestro proyecto simula un sistema de Home Banking implementando funciones bancarias comunes, gestion de datos a traves de archivos JSON y añadiendo un sistema de seguridad. 

- **Modularización del código** 

Dividimos nuestro codigo en distintos archivos:
  - main.py → menú principal.
  - usuarios.py → registro/login con regex, menu de usuario, bloqueo de cuenta, consulta de saldos y datos, plazos fijos.
  - cuentas.py → depósitos, extracciones, saldo.
  - transferencias.py → transferencias con alias validando el PIN para mas seguridad.
  - historial.py → registro de movimientos, exportar el historial a txt y generacion de notificaciones internas.
  - seguridad.py → validar y modificar passward, cambiar PIN. 
  - utils.py → funciones auxiliares 
  - data/usuarios.json → datos en memoria


**Pasos claves del usuario para interpretar el código**

Lo primero que vera el usuario es el menú principal que le permitirá: 
- Registrarse
- Iniciar sesión 
- Salir del Programa 
Una vez que se registra e inicia sesión, el programa lo llevará al menú del usuario, permitiendole realizar distintas funciones: 
- Consultar datos
- Consultar notificaciones recibidas
- Consultar saldos de cuenta
- Cambiar alias
- Cambiar conttaseña 
- Realizar depositos
- Realizar extracción
- Transferir dinero
- Realizar plazo fijo 
- Modificar PIN
- Exportar historial a TXT
- Cerrar sesión 

**Desafios realizados con algunas funciones**

Nos gusto en este programa realizar distintos desafios con algunas funciones particulares: 
- Realizamos un sistema de seguridad y bloqueo (bloquear al tercer intento, PIN de transferencias, y guardar contraseñas en el historial.)
- Realizamos un módulo de notificaciones 
- Gestion de datos, guardando cada dato del usuario en archivos JSON.

**Documentación**

Realizamos la documentación interna de cada función implementada del código. 