import utilities
import sqlite3

def data_fetch(urls):
    with utilities.cursor_handler(utilities.con) as cur:
        print("Random message") 
        utilities.db_select(cur, "select * from STACKEXCHANGE_USER")
        print("Random message") 

if __name__ == "__main__":
    data_fetch("www.google.com")