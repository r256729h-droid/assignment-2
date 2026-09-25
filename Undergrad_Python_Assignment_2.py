"""
UNDERGRADUATE PYTHON ASSIGNMENT 2
Single-file GitHub version
"""

import sqlite3
import socket
import threading
import time
import random
from abc import ABC, abstractmethod


# QUESTION 1: SQLITE DATABASE
def question1_sqlite():
    print("\nQUESTION 1: SQLITE DATABASE")
    print("-" * 40)

    connection = None

    try:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                mark INTEGER NOT NULL
            )
        """)

        cursor.execute("DELETE FROM students")

        students = [
            ("Tariro", 78),
            ("Simba", 85),
            ("Rudo", 91)
        ]

        cursor.executemany(
            "INSERT INTO students (name, mark) VALUES (?, ?)",
            students
        )

        connection.commit()

        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        print("Student Records:")
        for record in records:
            print(record)

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        if connection is not None:
            connection.close()


# QUESTION 2: ENCAPSULATION
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: ${amount:.2f}")

    def display_balance(self):
        print(f"Current balance: ${self.__balance:.2f}")


def question2_encapsulation():
    print("\nQUESTION 2: ENCAPSULATION")
    print("-" * 40)

    account = BankAccount("Sylvester", 1000)
    account.display_balance()
    account.deposit(500)
    account.withdraw(300)
    account.display_balance()

    print(
        "Encapsulation is achieved using the private "
        "attribute __balance and public methods."
    )


# QUESTION 3: CLIENT-SERVER SOCKET PROGRAM
HOST = "127.0.0.1"
PORT = 65432


def socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")

        connection, address = server_socket.accept()

        with connection:
            print("Connected by:", address)
            data = connection.recv(1024)

            if data:
                print("Message received:", data.decode())

    except OSError as error:
        print("Server network error:", error)

    finally:
        server_socket.close()


def socket_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        message = "Hello from client!"
        client_socket.sendall(message.encode())
        print("Client sent:", message)

    except OSError as error:
        print("Client network error:", error)

    finally:
        client_socket.close()


def question3_client_server():
    print("\nQUESTION 3: CLIENT-SERVER SOCKET PROGRAM")
    print("-" * 40)

    server_thread = threading.Thread(target=socket_server)
    server_thread.start()

    time.sleep(0.5)
    socket_client()

    server_thread.join()


# QUESTION 4: RANDOM NUMBERS
def question4_random_numbers():
    print("\nQUESTION 4: RANDOM NUMBERS")
    print("-" * 40)

    numbers = [random.uniform(0, 10) for _ in range(5)]

    print("Generated numbers:")
    for number in numbers:
        print(f"{number:.2f}")

    print(f"Minimum value: {min(numbers):.2f}")
    print(f"Maximum value: {max(numbers):.2f}")


# QUESTION 5: ABSTRACT BASE CLASS
class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

    def write(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(data)


class BinaryFileHandler(FileHandler):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "rb") as file:
            return file.read()

    def write(self, data):
        with open(self.filename, "wb") as file:
            file.write(data)


def question5_abstract_class():
    print("\nQUESTION 5: ABSTRACT BASE CLASS")
    print("-" * 40)

    text_handler = TextFileHandler("example.txt")
    text_handler.write("Hello from the text file handler.")
    print("Text file contents:")
    print(text_handler.read())

    binary_handler = BinaryFileHandler("example.bin")
    binary_handler.write(b"Hello from the binary file handler.")
    print("Binary file contents:")
    print(binary_handler.read())


# QUESTION 6: INHERITANCE AND METHOD OVERRIDING
class Vehicle:

    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):

    def move(self):
        print("The car is driving on the road.")


class Bike(Vehicle):

    def move(self):
        print("The bike is riding on two wheels.")


def question6_inheritance():
    print("\nQUESTION 6: INHERITANCE AND METHOD OVERRIDING")
    print("-" * 40)

    vehicle = Vehicle()
    car = Car()
    bike = Bike()

    vehicle.move()
    car.move()
    bike.move()


def main():
    print("=" * 55)
    print("UNDERGRADUATE PYTHON ASSIGNMENT 2")
    print("=" * 55)

    question1_sqlite()
    question2_encapsulation()
    question3_client_server()
    question4_random_numbers()
    question5_abstract_class()
    question6_inheritance()

    print("\n" + "=" * 55)
    print("ALL QUESTIONS COMPLETED")
    print("=" * 55)


if __name__ == "__main__":
    main()
