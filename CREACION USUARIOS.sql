--Creacion Usuarios

CREATE USER usuario1 WITH PASSWORD 'udla1111';
CREATE USER usuario2 WITH PASSWORD 'udla2222';
CREATE USER usuario3 WITH PASSWORD 'udla3333';
-----------------------------
--Asignacion roles


GRANT superdba to usuario1;
GRANT readwrite to usuario2;
GRANT readonly to usuario3;