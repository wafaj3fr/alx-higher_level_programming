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

        # Construct SQL query to select all cities and execute it
        query = "SELECT * FROM cities ORDER BY cities.id ASC"
        cursor.execute(query)

        # Fetch one row at a time and display results
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
