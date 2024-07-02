-- Crear tabla Clientes
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Direccion VARCHAR(255),
    Telefono VARCHAR(20),
    Email VARCHAR(100)
);

-- Crear tabla Destinos
CREATE TABLE Destinos (
    DestinoID INT PRIMARY KEY,
    Direccion VARCHAR(255),
    Ciudad VARCHAR(100),
    Pais VARCHAR(100),
    CodigoPostal VARCHAR(20)
);

-- Crear tabla Empleados
CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Cargo VARCHAR(50),
    Telefono VARCHAR(20),
    Email VARCHAR(100)
);

-- Crear tabla Vehículos
CREATE TABLE Vehiculos (
    VehiculoID INT PRIMARY KEY,
    Tipo VARCHAR(50),
    Marca VARCHAR(50),
    Modelo VARCHAR(50),
    Matricula VARCHAR(20)
);

-- Crear tabla Envíos
CREATE TABLE Envios (
    EnvioID INT PRIMARY KEY,
    ClienteID INT,
    EmpleadoID INT,
    DestinoID INT,
    VehiculoID INT,
    Peso DECIMAL(10, 2),
    FechaEnvio DATE,
    EstadoEnvio VARCHAR(50),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (EmpleadoID) REFERENCES Empleados(EmpleadoID),
    FOREIGN KEY (DestinoID) REFERENCES Destinos(DestinoID),
    FOREIGN KEY (VehiculoID) REFERENCES Vehiculos(VehiculoID)
);

-- Crear tabla Facturas
CREATE TABLE Facturas (
    FacturaID INT PRIMARY KEY,
    FechaFactura DATE,
    ClienteID INT,
    MontoTotal DECIMAL(10, 2),
    MetodoPago VARCHAR(50),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

-- Crear tabla DetallesFacturacion
CREATE TABLE DetallesFacturacion (
    DetalleID INT PRIMARY KEY,
    FacturaID INT,
    EnvioID INT,
    Monto DECIMAL(10, 2),
    FOREIGN KEY (FacturaID) REFERENCES Facturas(FacturaID),
    FOREIGN KEY (EnvioID) REFERENCES Envios(EnvioID)
);
