import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("Successfully connected to SQL Server")
        cursor = conn.cursor()

        while True:
            query_lines = []
            print("Enter your SQL query. Type 'GO' on a new line to execute, or 'EXIT' to quit:")
            
            while True:
                line = input()
                if line.lower() == 'go':
                    break
                elif line.lower() == 'exit':
                    query_lines = ['exit']
                    break
                else:
                    query_lines.append(line)
            
            # Check if the user wants to exit
            if query_lines and query_lines[0].lower() == 'exit':
                break

            query = ' '.join(query_lines)
            try:
                cursor.execute(query)
                
                # Check if the command was a SELECT statement:
                if cursor.description is not None:
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    # If it wasn't a SELECT, it might have been an INSERT/UPDATE/DELETE
                    conn.commit()
                    print("Query executed successfully.")

            except Exception as query_error:
                print("Error executing query: ", query_error)

except Exception as e:
    print("Error: ", e)
