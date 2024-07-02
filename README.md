----------------------------Proyecto Curier Plus S.A-----------------------------------

#Integrantes: Maria Jose LLano, Christian Andrade, Diego Garcia

#Proyecto de Curier
Este proyecto se basa en la ejecución de un contenedor utilizando la imagen de Postgres para almacenar la información pertinente de las operaciones de las reparticiones y distribuciones de los encargos. Se crea una base de datos y se configuran usuarios con diferentes permisos para acceder y manipular los datos almacenados.

#Generación de Datos Aleatorios
Para generar datos aleatorios de prueba, se incluye un archivo con el nombre "Poblacion de Datos Faker.py" de ejecución en Python (.py). Estos archivos utilizan el módulo "Faker" de Python para crear datos ficticios. Puedes ejecutar estos scripts para generar datos de prueba antes de utilizar la base de datos en producción.

#Diagrama de la Base de Datos
Se adjunta los diagramas tanto lógico como físico de la base de datos que muestra la estructura y las relaciones entre las tablas, y se proporciona un diccionario de datos para comprender la información almacenada en cada tabla.

#Scripts SQL
Se incluyen los scripts SQL necesarios para crear la base de datos y configurar los usuarios con los permisos adecuados. Estos scripts aseguran que la base de datos esté correctamente configurada y los usuarios tengan los privilegios necesarios para realizar las operaciones requeridas.
CREACIÓN TABLAS.sql: Crea la estructura de la base de datos y las tablas necesarias.
CREACIÓN ROLES.sql: Crea los roles con permisos de lectura y manipulación de los datos según sea necesarios.
CREACIÓN USUARIOS.sql: Crea los usuarios otorgándoles los roles que sean necesarios.

#Persistencia de Datos con Volúmenes
Para garantizar la persistencia de los datos almacenados en la base de datos, se utiliza un volumen al contenedor de Postgres. El volumen permite que los datos persistan incluso si el contenedor se detiene o se elimina, lo que es fundamental para mantener la integridad de los datos.
