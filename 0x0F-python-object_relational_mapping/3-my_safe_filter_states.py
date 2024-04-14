#!/usr/bin/python3
"""Script to display values in the states table based on a search argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters and state name from command line arguments
    username, password, database, state_name = sys.argv[1:5]

    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password,
                                     db=database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Construct SQL query with parameterized query and execute it
        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
        cursor.execute(query, (state_name,))

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
