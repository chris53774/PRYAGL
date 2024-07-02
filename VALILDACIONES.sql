
--- Validaciones
Verificar si tienen permisos 

SELECT * FROM clientes where clienteid =2;

SELECT * FROM envios;

DELETE FROM envios where envioid = 1  ;
UPDATE clientes SET nombre = 'Majo' where clienteid =1000 ;

DROP DELETE ON clientes TO usuario2;
CREATE TABLE vehiculospesados (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    año INT,
    capacidad_kg INT
);


SELECT grantee, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'readonly';


DROP TABLE clientes;
