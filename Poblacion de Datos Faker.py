from faker import Faker
import random
import psycopg2

fake = Faker()

# Número de registros para cada tabla
num_clientes = 1000
num_destinos = 1000
num_empleados = 50
num_vehiculos = 20
num_envios = 1000
num_facturas = 1000

# Generar datos para la tabla Clientes
clientes = []
for i in range(1, num_clientes + 1):
    clientes.append((i, fake.name(), fake.address(), str(fake.random_number(digits=10)), fake.email()))

# Generar datos para la tabla Destinos
destinos = []
for i in range(1, num_destinos + 1):
    destinos.append((i, fake.address(), fake.city(), fake.country(), fake.postcode()))

# Generar datos para la tabla Empleados
empleados = []
for i in range(1, num_empleados + 1):
    empleados.append((i, fake.name(), fake.word(ext_word_list=['Gerente', 'Repartidor', 'Despachador', 'Recepcionista']), str(fake.random_number(digits=10)), fake.email()))

# Generar datos para la tabla Vehiculos
vehiculos = []
for i in range(1, num_vehiculos + 1):
    vehiculos.append((i, fake.word(ext_word_list=['Camion', 'Moto']),
                      fake.word(ext_word_list=['Freightliner', 'Kenworth', 'Peterbilt', 'Volvo Trucks', 'Mack Trucks', 'Scania', 'Mercedes-Benz Trucks', 'MAN', 'DAF', 'Iveco', 'Harley-Davidson', 'Yamaha', 'Honda', 'Kawasaki', 'Suzuki', 'Ducati', 'BMW Motorrad', 'Triumph', 'KTM', 'Aprilia']),
                      fake.word(ext_word_list=['Cascadia', 'T680', '579', 'VNL', 'Anthem', 'R Series', 'Actros', 'TGX', 'XF', 'Stralis', 'Sportster', 'YZF-R1', 'CBR600RR', 'Ninja ZX-10R', 'GSX-R750', 'Panigale V4', 'R1250GS', 'Bonneville', 'Duke 390', 'RSV4']),
                      fake.license_plate()))

# Generar datos para la tabla Envios
envios = []
for i in range(1, num_envios + 1):
    envios.append((i, random.randint(1, num_clientes),
                   random.randint(1, num_empleados),
                   random.randint(1, num_destinos),
                   random.randint(1, num_vehiculos),
                   round(random.uniform(0, 100), 2),
                   fake.date_this_year(),
                   fake.word(ext_word_list=['Pendiente', 'En tránsito', 'Entregado', 'Cancelado'])))

# Generar datos para la tabla Facturas
facturas = []
for i in range(1, num_facturas + 1):
    facturas.append((i, fake.date_this_year(), random.randint(1, num_clientes), round(random.uniform(100.00, 1000.00), 2), fake.word(ext_word_list=['Efectivo', 'Tarjeta de crédito', 'Transferencia bancaria'])))

# Generar datos para la tabla DetallesFacturacion
detalles_facturacion = []

for i in range(1, num_envios + 1):
    detalles_facturacion.append((i, random.randint(1, num_facturas), random.randint(1, num_envios), round(random.uniform(50.00, 500.00), 2)))

# Conexión a la BD
try:
    connection = psycopg2.connect(
        host='192.168.200.23',
        port=1029,
        user='postgres',
        password='postgres',
        dbname='PryAdminAGL'
    )
    cursor = connection.cursor()

    # Insertar datos en la tabla Clientes
    cursor.executemany("INSERT INTO Clientes (ClienteID, Nombre, Direccion, Telefono, Email) VALUES (%s, %s, %s, %s, %s)", clientes)

    # Insertar datos en la tabla Destinos
    cursor.executemany("INSERT INTO Destinos (DestinoID, Direccion, Ciudad, Pais, CodigoPostal) VALUES (%s, %s, %s, %s, %s)", destinos)

    # Insertar datos en la tabla Empleados
    cursor.executemany("INSERT INTO Empleados (EmpleadoID, Nombre, Cargo, Telefono, Email) VALUES (%s, %s, %s, %s, %s)", empleados)

    # Insertar datos en la tabla Vehiculos
    cursor.executemany("INSERT INTO Vehiculos (VehiculoID, Tipo, Marca, Modelo, Matricula) VALUES (%s, %s, %s, %s, %s)", vehiculos)

    # Insertar datos en la tabla Envios
    cursor.executemany("INSERT INTO Envios (EnvioID, ClienteID, EmpleadoID, DestinoID, VehiculoID, Peso, FechaEnvio, EstadoEnvio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", envios)

    # Insertar datos en la tabla Facturas
    cursor.executemany("INSERT INTO Facturas (FacturaID, FechaFactura, ClienteID, MontoTotal, MetodoPago) VALUES (%s, %s, %s, %s, %s)", facturas)

    # Insertar datos en la tabla DetallesFacturacion
    cursor.executemany("INSERT INTO DetallesFacturacion (DetalleID, FacturaID, EnvioID, Monto) VALUES (%s, %s, %s, %s)",
                       detalles_facturacion)

    # Confirmar los cambios
    connection.commit()
    print("Datos insertados correctamente.")

except (Exception, psycopg2.Error) as error:
    print("Error al insertar datos en PostgreSQL:", error)

finally:
    # Cerrar la conexión
    if connection:
        cursor.close()
        connection.close()
        print("Conexión PostgreSQL cerrada.")
