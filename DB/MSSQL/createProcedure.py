import pyodbc
import conf

def main():
    try:
        # Connect to the database
        with pyodbc.connect(conf.conn_str) as conn:
            print("Successfully connected to SQL Server.")
            cursor = conn.cursor()

            while True:
                # Prompt the user for input to create the stored procedure
                print("\nEnter the SQL statements for your stored procedure. Type 'doz' to finish, or type 'exit' to quit:")
                user_input_lines = []
                while True:
                    line = input()
                    if line.lower() == 'doz':
                        break
                    elif line.lower() == 'exit':
                        return  # Exit the main function
                    user_input_lines.append(line)

                create_procedure_sql = '\n'.join(user_input_lines)

                if create_procedure_sql.strip():  # Check if there is something to execute
                    print("Creating stored procedure...")
                    cursor.execute(create_procedure_sql)
                    conn.commit()
                    print("Stored procedure created successfully.")

    except pyodbc.Error as e:
        print("SQL error: ", e)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
