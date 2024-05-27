
-- Crear un usuario par ingresar con "System Assidned Managed Identity"

CREATE USER [demo-data-factory-ed] FROM EXTERNAL PROVIDER;

DROP USER [demo-data-factory-ed];
EXEC sp_addrolemember 'db_datareader', 'demo-data-factory-ed';


GRANT INSERT ON dbo.Cars TO [demo-data-factory-ed];
