import sys
import pyodbc
import conf

def execute_procedure(cursor, procedure_name, *parameters):
    # Create the SQL command
    sql_command = f"EXEC {procedure_name}"
    if parameters:
        params = ', '.join(f"'{param}'" for param in parameters)
        sql_command += f" {params}"

    # Execute the stored procedure
    cursor.execute(sql_command)

    # Loop through each result set
    more_results = True
    while more_results:
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        # Check for more result sets
        more_results = cursor.nextset()

def main():
    try:
        with pyodbc.connect(conf.conn_str) as conn:
            print("Successfully connected to SQL Server")
            cursor = conn.cursor()

            while True:
                # Get stored procedure name from user input
                procedure_name = input("Enter the stored procedure name (or type 'exit' to quit): ")
                if procedure_name.lower() == 'exit':
                    break

                # Get parameters for the stored procedure
                parameters = input("Enter the parameters separated by spaces (if any): ").split()

                # Execute the stored procedure
                execute_procedure(cursor, procedure_name, *parameters)

    except pyodbc.Error as e:
        print("SQL error: ", e)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
