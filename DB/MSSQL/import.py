import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("Successfully connected to SQL Server")

        # Restore database
        restore_query = """
        RESTORE DATABASE YourDatabaseName
        FROM DISK = '/home/abdennacer/Documents/GitHub/Data_Sciences/DB/MSSQL/sources/VolAvion_2005.bak'
        WITH MOVE 'YourLogicalDataFileName' TO '/var/opt/mssql/data/YourDataFile.mdf',
        MOVE 'YourLogicalLogFileName' TO '/var/opt/mssql/data/YourLogFile.ldf',
        REPLACE;
        """
        conn.execute(restore_query)
        print("Database restored successfully")

except Exception as e:
    print("Error: ", e)