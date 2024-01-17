# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:39:04 2023

@author: sharm
"""

import tkinter as tk
import mysql.connector
from tkinter import Menu
from tkinter import *
from tkinter import messagebox

config ={
    "host":"localhost",
    "user":"shree",
    "password":"Shree_123",
    "database":"bookstore_application",
    }

connection = mysql.connector.connect(**config)

cursor = connection.cursor()


def fetch_books():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT Name, book_author FROM book_details;"
        cursor.execute(query)
        Names = [row[0] for row in cursor.fetchall()] # Fetch the book names

        cursor.close()
        connection.close()

        return Names  # Return the list of book names

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch Names"]  # Handle the error
    

            
def fetch_authors():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_author FROM book_details;"
        cursor.execute(query)
        Author = [row[0] for row in cursor.fetchall()]# Fetch the book names

        cursor.close()
        connection.close()

        return Author # Return the list of book names

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch Names"]
    
def fetch_prices():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_price FROM book_details;"
        cursor.execute(query)
        Price = [row[0] for row in cursor.fetchall()]

        cursor.close()
        connection.close()

        return Price 

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch Names"]
    
def fetch_publisher():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT Publisher FROM book_details;"
        cursor.execute(query)
        publisher = [row[0] for row in cursor.fetchall()]# Fetch the book names

        cursor.close()
        connection.close()

        return publisher # Return the list of book names

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch Names"]

def fetch_language():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT Language FROM book_details;"
        cursor.execute(query)
        language = [row[0] for row in cursor.fetchall()]# Fetch the book names

        cursor.close()
        connection.close()

        return language # Return the list of book names

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch Names"]
    
def fetch_bookisbn():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_isbn FROM book_details;"
        cursor.execute(query)
        bookisb = [row[0] for row in cursor.fetchall()]# Fetch the book names

        cursor.close()
        connection.close()

        return bookisb # Return the list of book names

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch Names"]

def search_title(search_text):
    #search_text = title_text.get()
    connection = mysql.connector.connect(**config)  # Connect to the database
    cursor = connection.cursor()
    query = "SELECT * FROM book_details WHERE Name LIKE %s;"
    search_term = f"%{search_text}%"

    cursor.execute(query, (search_term,))
    results = cursor.fetchall()
  
    for result in results:
            return result
        
    cursor.close()
    connection.close()
    
def open_new_window():
    root=tk.Tk()
    new_window = tk.Toplevel(root)
    new_window.title("new window")
    label = tk.Label(new_window, text="new window open")
    label.grid(row=8, column=9)
    
def insert_to_cart(isbn, book_name, price, user_id):
   connection = mysql.connector.connect(**config)  # Connect to the database
   cursor = connection.cursor()
   insert_query = "INSERT INTO cart_details (book_isbn_c, Name_of_book, price, user_id) VALUES (%s, %s, %s, %s);"

   data = (isbn, book_name, price, user_id)
   cursor.execute(insert_query, data)
   connection.commit()
   messagebox.showinfo("Success", f"{book_name} added to cart")
   cursor.close()
  
   connection.close()
 
def place_order(userid, amounttot, quantity):
   connection = mysql.connector.connect(**config)  # Connect to the database
   cursor = connection.cursor()
   insert_query = "INSERT INTO orders(user_id, total_amount, quantity) VALUES (%s, %s, %s);"

   data = (userid, amounttot, quantity)
   cursor.execute(insert_query, data)
   connection.commit()
    
   messagebox.showinfo("Success", f"order placed")
   cursor.close()
  
   
   connection.close()
def delete_from_cart(isbn, book_name, user_id):
   connection = mysql.connector.connect(**config)  # Connect to the database
   cursor = connection.cursor()
   query = "DELETE FROM cart_details WHERE book_isbn_c = %s AND Name_of_book = %s AND user_id = %s;"
   data = (isbn, book_name, user_id)
   cursor.execute(query, data)
   #data = (isbn, book_name, price, user_id)
   #cursor.execute(insert_query, data)
   connection.commit()
    
  
   messagebox.showinfo("Book deleted from cart")
   # messagebox.showinfo("Success", f"{book_name} deleted from cart")
   cursor.close()
   connection.close()
   
def fetch_booktitle_cart():
       try:
           connection = mysql.connector.connect(**config)  # Connect to the database
           cursor = connection.cursor()
           query = "SELECT distinct Name_of_book FROM cart_details;"
           cursor.execute(query)
           name_ob = [row[0] for row in cursor.fetchall()]# Fetch the book names

           cursor.close()
           connection.close()

           return name_ob # Return the list of book names

       except mysql.connector.Error as err:
           print(f"Error: {err}")
           return ["Error: Cannot fetch Names"]

def fetch_bookprice_cart():
              try:
                  connection = mysql.connector.connect(**config)  # Connect to the database
                  cursor = connection.cursor()
                  query = "SELECT distinct price FROM cart_details;"
                  cursor.execute(query)
                  price_ob = [row[0] for row in cursor.fetchall()]# Fetch the book names

                  cursor.close()
                  connection.close()

                  return price_ob # Return the list of book names

              except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return ["Error: Cannot fetch Names"]

def fetch_bookprice_car():
              try:
                  connection = mysql.connector.connect(**config)  # Connect to the database
                  cursor = connection.cursor()
                  query = "SELECT price FROM cart_details;"
                  cursor.execute(query)
                  price_ob1 = [row[0] for row in cursor.fetchall()]# Fetch the book names

                  cursor.close()
                  connection.close()

                  return price_ob1 # Return the list of book names

              except mysql.connector.Error as err:
                  print(f"Error: {err}")
                  return ["Error: Cannot fetch Names"]
              
def get_book_quantity(book_name):
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT Name_of_book, count(*) FROM cart_details WHERE Name_of_book = %s GROUP BY Name_of_book;"
        # 
        cursor.execute(query, (book_name,))
        book_quantity = cursor.fetchone()  # Fetch the quantity for the specified book
        
        # Close the cursor and the database connection
        cursor.close()
        connection.close()
        
        if book_quantity:
            return book_quantity[1]  # Return the quantity of the specified book
        else:
            return 0 
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return -1  # Handle the error by returning -1 or any other suitable value
            
def get_cart_details_count():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_isbn_c, Name_of_book, user_id FROM cart_details;"
        
        cursor.execute(query)
        count = cursor.fetchall()  # Fetch the count
        
        cursor.close()
        connection.close()
        return count  # Return the number of tuples in cart_details
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return -1  # Handle the error by returning -1 or any other suitable value

def fetch_username():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_name FROM user;"
        cursor.execute(query)
        username = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return username  # Return the username

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch username"]  # Handle the error
    
def fetch_fullname():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_fullname FROM user;"
        cursor.execute(query)
        fullname = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return fullname  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch fullname"]  # Handle the error
    
    
def fetch_dob():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_dob FROM user;"
        cursor.execute(query)
        dob = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return dob  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch date of birth"]  # Handle the error
    
def fetch_address():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_address FROM user;"
        cursor.execute(query)
        address = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return address  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch address"]  # Handle the error
    
def fetch_phonenumber():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_contact FROM user;"
        cursor.execute(query)
        phonenumber = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return phonenumber  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch phone number"]  # Handle the error
    
    
def fetch_email_id():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_email FROM user;"
        cursor.execute(query)
        email_id = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return email_id  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch email id"]  # Handle the error
    
def fetch_user_id():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT user_id FROM user;"
        cursor.execute(query)
        user_id = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return user_id  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch user id"]  # Handle the error
    
def open_new_window():
    root=tk.Tk()
    new_window = tk.Toplevel(root)
    new_window.title("new window")
    label = tk.Label(new_window, text="new window open")
    label.grid(row=8, column=9)
    
def fetch_name():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT name FROM book_details;"
        cursor.execute(query)
        name = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return name  # Return the username

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch book title"]  # Handle the error
    
def fetch_book_author():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_author FROM book_details;"
        cursor.execute(query)
        author = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return author  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch author"]  # Handle the error
    
    
def fetch_publisher():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT publisher FROM book_details;"
        cursor.execute(query)
        publisher = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return publisher  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch publisher"]  # Handle the error
    
def fetch_language():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT language FROM book_details;"
        cursor.execute(query)
        language = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return language  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch language"]  # Handle the error
    
def fetch_book_price():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_price FROM book_details;"
        cursor.execute(query)
        bookprice = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return bookprice  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch book price"]  # Handle the error
    
    
def fetch_book_isbn():
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()
        query = "SELECT book_isbn FROM book_details;"
        cursor.execute(query)
        bookisbn = [row[0] for row in cursor.fetchall()] # Fetch the username

        cursor.close()
        connection.close()

        return bookisbn  # Return the fullname

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return ["Error: Cannot fetch book isbn"]  # Handle the error
    

def book_details_update():
     try:
         connection = mysql.connector.connect(**config)  # Connect to the database
         cursor = connection.cursor()
         query = "SELECT book_isbn FROM book_details;"
         cursor.execute(query)
         bookisbn = [row[0] for row in cursor.fetchall()] # Fetch the username
    
         cursor.close()
         connection.close()
    
         return bookisbn  # Return the fullname
    
     except mysql.connector.Error as err:
         print(f"Error: {err}")
         return ["Error: Cannot fetch book isbn"]  # Handle the error
  

#def place_order():           