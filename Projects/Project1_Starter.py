"""
Group No: 4
Members: Dillon Kelly, Adam Baker, Hannah Wilkinson
Date: 10-12-2023
Project #1.

"""

import DBConnector
import socket
import os
import time
from datetime import datetime


def main():
    """
    Where Magic Happens.
    :return:
    """

    targets = 0
    current_ip = ''
    user_input = input(Method1())
    while user_input.lower() != 'exit':

        if user_input.lower() == 'a':
            current_ip = (Method6())
            print(current_ip)


        elif user_input.lower() == 'b':
            targets = int(input("How many targets would you like to test?"))


        elif user_input.lower() == 'c':
            if targets == 0:
                print('In valid number of target')
            else:
                print("Ok. starting to test {0} targets", targets)
                for n in range(targets):
                    new_ip = Method3(current_ip, str(n))
                    Method2(new_ip)

        elif user_input.lower() == 'n':
            print("Ok. Creating Table")
            Method4()

        elif user_input.lower() == 'x':
            print("Ok. Deleting Table")

        user_input = input(Method1())


def Method1():
    """
    Display all options for this program
    :return: N/A
    """
    print("A\t\t To obtain your current IP Address ")
    print("B\t\t Provide No. of targets to check for")
    print("C\t\t Ping Targets and save data to the DB")
    print("N\t\t Create Table")
    print("X\t\t Delete Table")
    print("Exit\t Exit")


def Method2(current_ip):
    """
    Send a ping message to the targeted IP Address
    :param current_ip: The IP address ti poing
    :return: Responding if the target is alive. Not responding otherwise.
    """
    print("Pinging....")
    print("pinging ", current_ip)
    ping_cmd = f"ping -c 1 -w 2 {current_ip}"
    return "responding" if os.system(ping_cmd) == 0 else "not responding"


def Method3(ip_string, new_last_digit):
    """
    This accepts an IP address and replaces teh last digit with a provided digit
    The idea is to get the IP address for a new host.
    :param ip_string:
    :param new_last_digit:
    :return:
    """
    # Split the IP string into its four parts using dot as the delimiter
    ip_parts = ip_string.split(".")

    # Replace the last part of the IP address (last digit) with the new digit
    ip_parts[-1] = new_last_digit

    # Join the parts back together to form the updated IP address
    new_ip_string = ".".join(ip_parts)

    # Return an IP address with an updated last digit aka. new target
    return new_ip_string


def Method4():
    """
    This creates table ping_test needed to record IP addresses status
    Test your DB to make sure the DB has been created
    :return: N/A
    """
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Ping_Test (IP_ADDRESS  VARCHAR, STATUS  VARCHAR, TIME VARCHAR);'

    # Message to display upon table creation. Not integrated yet.
    sqlMessage = 'Table Test created successfully. Please access pgAdmin to verify table was created successfully'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')
    print("The ping_test table was created.")


def Method5():
    """
    This deletes the ping_test table
    Test your DB to make sure the DB has been created
    :return: N/A
    """
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    # SQL command to create a new table
    sqlCommand = 'DROP TABLE Ping_Test;'

    # Message to display upon table creation. Not integrated yet.
    sqlMessage = 'Table dropped successfully. Please access pgAdmin to verify table was created successfully'

    # Execute the SQL command.
    my_db.query(sqlCommand, sqlMessage)
    print("The ping_test table was created.")


def Method6() -> object:
    """
    Method that obtains the IP address of the machine you are using
    :return: Your current IP Address
    """
    # Get the hostname of the current machine
    hostname = socket.gethostname()

    # Return the IP address associated with the hostname
    return socket.gethostbyname(hostname)


def Method7(ip, status):
    """
       Inserts data (IP address, Status, and Current time) into the table ping_test, assuming the table already exists.
       :param ip: IP Address to record data for
       :param status: Current status
       :return:
    """
    my_db = DBConnector.MyDB()
    my_db.query('INSERT INTO ping_test values (%s,%s,%s);', (ip, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print('Successfully recorded')


if __name__ == "__main__":
    main()