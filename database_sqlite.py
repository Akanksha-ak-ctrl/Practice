import sqlite3


# Main function
def main():
    database = "example.db"


    # Connect to the database
    conn = create_connection(database)
    if conn is not None:

        # DELETE: drop table if exists
        delete_table(conn, "drop table if exists users")



        # CREATE: SQL statements to create table and insert data
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
        """
        create_table(conn, create_table_sql)



        # UPDATE: Insert data into the table

        insert_data_sql = "INSERT INTO users (name, age) VALUES (?, ?)"
        # Sample data
        data = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

        for entry in data:
            insert_data(conn, insert_data_sql, entry)



        # READ: Select and print data from the table
        select_data_sql = "SELECT * FROM users"
        print("\nUsers:")
        select_data(conn, select_data_sql)

        # Close the connection
        conn.close()
    else:
        print("Error! Cannot connect to the database")


# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to database:", sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a new table in the database
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)


# Function to delete a new table in the database
def delete_table(conn, delete_table_sql):
    try:
        c = conn.cursor()
        c.execute(delete_table_sql)
        print("table deleted successfully")
    except sqlite3.Error as e:
        print(e)




# Function to insert data into the table
def insert_data(conn, insert_data_sql, data):
    try:
        c = conn.cursor()
        c.execute(insert_data_sql, data)
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print(e)

# Function to select and print data from the table
def select_data(conn, select_data_sql):
    try:
        c = conn.cursor()
        c.execute(select_data_sql)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
    main()
