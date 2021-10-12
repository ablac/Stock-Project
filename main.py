#!/usr/bin/python

from subprocess import call
import os


def main_menu():
    option = ""
    while True:
        basic.clear_console()
        print("Select Course ---")
        print("1 - Stock Analyzer")
        print("2 - Stock GUI")
        print("E - Exit Program")
        option = input("Enter Menu Option: ")
        if option == "E":
            basic.clear_console()
            print("Goodbye")
            break
        if option == "1":
            basic.clear_console()
            call(["python", "StockMenu/stock_menu.py"])
        if option == "2":
            basic.clear_console()
            call(["python", "StockMenu/stock_GUI.py"])
        else:
            print("Unknown Command Try again")
            basic.clear_console()
            main_menu()


# Begin program
class basic:
    def clear_console():
        os.system('clear')


def main():
    main_menu()


if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
