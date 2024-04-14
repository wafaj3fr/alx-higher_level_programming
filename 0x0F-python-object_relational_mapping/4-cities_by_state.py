#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    username, password, database = sys.argv[1:4]

    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password,
                                     db=database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Construct SQL query to select cities along with their respective states
        query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC
                """
        cursor.execute(query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
