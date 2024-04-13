#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    # Get MySQL connection parameters from command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password,
                                     db=database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute SQL query to select all states, sorted by states.id in ascending order
        cursor.execute("SELECT * FROM states ORDER BY states.id")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        exit(1)

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

