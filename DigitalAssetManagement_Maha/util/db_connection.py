import pyodbc


class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        """
        Returns the database connection object. If the connection is not yet established,
        it creates a new one using the connection string and returns it.
        """
        if DBConnection.connection is None:
            try:
                # You need to configure the correct connection string based on your SQL Server setup
                server = r'DESKTOP-AAMRPRI\SQLEXPRESS'  # SQL Server instance
                database = 'cstudy'  # Replace with your database name
                connection_string = (
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={server};'
                    f'DATABASE={database};'
                    f'Trusted_Connection=yes;'
                )

                DBConnection.connection = pyodbc.connect(connection_string)
                print("Database connection established successfully.")

            except pyodbc.Error as e:
                print(f"Error establishing database connection: {e}")
                raise
        return DBConnection.connection
