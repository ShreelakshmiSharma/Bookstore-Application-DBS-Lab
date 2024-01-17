# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:28:26 2023

@author: sharm
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import backend
from functools import partial
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import ttk

config ={
    "host":"localhost",
    "user":"shree",
    "password":"Shree_123",
    "database":"bookstore_application",
    }

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

root=Tk()
root.geometry("600x450")
root.title("Bookstore")
root.configure(bg="lightblue")


def exit_program():
    root.quit()
    
def show_page1():
    frame2.grid_remove()
    frame3.grid_remove()
    frame11.grid_remove()
    show_frame1()
    frame1.grid()
    
def show_page11():
    frame2.grid_remove()
    frame3.grid_remove()
    frame11.grid()
    
def show_page111():
    frame1.grid_remove()
    frame11.grid()

def show_page2():
    frame11.grid_remove()
    frame1.grid_remove()
    
    frame3.grid(row=0, column=0)
 
def show_page3():   #for cart
    frame1.grid_remove()
    frame4.grid_remove()
    frame2.grid(row=0, column=0)
    
def cancel_page3():
    show_page11()
    
def cancel_page5():
    frame5.grid_remove()
    show_page11()
    
def show_page4():   #for cart
    frame1.grid_remove()
    frame2.grid_remove()
    frame4.grid(row=0, column=0)
    
def show_page5():   #for cart
    frame11.grid_remove()
    frame5.grid(row=0, column=0)
    
def show_page6():   #for admin
    frame11.grid_remove()
    frame6.grid(row=0, column=0)
    
def show_page7():   #for admin
    frame6.grid_remove()
    frame9.grid_remove()
    frame10.grid_remove()
    frame8.grid_remove()
    frame7.grid(row=0, column=0)
    show_frame2()

def show_page8():   #for admin
    frame9.grid_remove()
    frame7.grid_remove()
    frame10.grid_remove()
    frame8.grid(row=0, column=0)

def show_page9():   #for admin
    frame7.grid_remove()
    frame8.grid_remove()
    frame9.grid(row=0, column=0)
    
def show_page10():   #for admin
    frame9.grid_remove()
    frame7.grid_remove()
    frame8.grid_remove()
    frame10.grid(row=0, column=0)    
    
font = ("Arial", 16)
font2 = ("Arial", 11)

frame1 = tk.Frame(root, bg="lightblue")
frame11 = tk.Frame(root, bg="lightblue")
frame2 = tk.Frame(root, bg="lightblue")
frame2.grid(row=0, column=0)
frame3 = tk.Frame(root, bg="lightblue")
frame11.grid(row=0, column=0)
frame4 = tk.Frame(root, bg="lightblue")
frame5 = tk.Frame(root, bg="lightblue")
frame6 = tk.Frame(root, bg="lightblue")
frame7 = tk.Frame(root, bg="lightblue")
frame8 = tk.Frame(root, bg="lightblue")
frame9 = tk.Frame(root, bg="lightblue")
frame10 = tk.Frame(root, bg="lightblue")
show_page11()

menubar = tk.Menu(root)
root.config(menu=menubar)

menu_font = ("Arial", 16) 

label_title = tk.Label(frame3, text="User Registration Form", font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label_full_name = tk.Label(frame3, text="Full Name:")
label_full_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_full_name = tk.Entry(frame3)
entry_full_name.grid(row=2, column=1, padx=10, pady=5)

label_user_contact = tk.Label(frame3, text="Contact:")
label_user_contact.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_user_contact = tk.Entry(frame3)
entry_user_contact.grid(row=4, column=1, padx=10, pady=5)

label_date_of_birth = tk.Label(frame3, text="Date of Birth:")
label_date_of_birth.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_date_of_birth = tk.Entry(frame3)
entry_date_of_birth.grid(row=5, column=1, padx=10, pady=5)

label_address = tk.Label(frame3, text="Address:")
label_address.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_address = tk.Entry(frame3)
entry_address.grid(row=7, column=1, padx=10, pady=5)

label_email = tk.Label(frame3, text="Email:")
label_email.grid(row=8, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(frame3)
entry_email.grid(row=8, column=1, padx=10, pady=5)
       
def submit_registration():
    full_name = entry_full_name.get()
    username = entry_username.get()
    user_contact = entry_user_contact.get()
    date_of_birth = entry_date_of_birth.get()
    password = entry_password.get()
    address = entry_address.get()
    email = entry_email.get()
    user_id = 0 
    
    try:
        connection = mysql.connector.connect(**config)  # Connect to the database
        cursor = connection.cursor()        
        user_status = "active"
        cursor.execute("SELECT MAX(user_id) FROM user")
        max_user_id = cursor.fetchone()[0]
        
        if max_user_id is None:
            user_id = 1
        else:
            # Increment the maximum user_id by one
            user_id = max_user_id + 1  
            # SQL query to insert registration data into user table
            query = "INSERT INTO user (user_id, user_name, user_fullname,  user_contact, password, user_dob, user_address, user_email, user_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

            cursor.execute(query, (user_id, username, full_name, user_contact, password, date_of_birth, address, email, user_status))
            connection.commit()
        
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Registration successful")
            show_page11()
            
    except mysql.connector.Error as err:
        print("Error:", str(err))
        messagebox.showerror("Error", "An error occurred during registration.")
 # Return None when registration fails

label_username = tk.Label(frame3, text="Username:")
label_username.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_username = tk.Entry(frame3)
entry_username.grid(row=3, column=1, padx=10, pady=5)

label_password = tk.Label(frame3, text="Password:")
label_password.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_password = tk.Entry(frame3)
entry_password.grid(row=6, column=1, padx=10, pady=5)


cursor.execute("SELECT MAX(user_id) FROM user")
max_user_id2 = cursor.fetchone()[0]

if max_user_id2 is None:
    user_id1 = 1
else:
    user_id1 = max_user_id2 + 1

button_signup = tk.Button(frame11, text="Sign Up", command=show_page2)
button_signup.grid(row=3, column=0, padx=10, pady=5)

label_generated_user_id = tk.Label(frame3, text=str(user_id1))
label_generated_user_id.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(frame3, text="Submit", command=submit_registration)
submit_button.grid(row=9, column=0, columnspan=2, pady=10)

cancel_button = tk.Button(frame3, text="Cancel", command=cancel_page3)
cancel_button.grid(row=10, column=0, columnspan=2, pady=10)  
     
label_user_id = tk.Label(frame3, text="User ID:")
label_user_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")


def insert_logged_in_record(user_id, username):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(prepared=True)  # Use prepared statements for security

        # Define the INSERT query to insert a record into the "logged_in" table
        query = "INSERT INTO logged_in (user_id, user_username, time_stamp) VALUES (%s, %s, %s)"
        timestamp = datetime.now()  # Get the current timestamp
        cursor.execute(query, (user_id, username, timestamp))

        # Commit the transaction
        connection.commit()

    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
        messagebox.showinfo("Error", "An error occurred while logging in.")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showinfo("Error", "An error occurred while logging in.")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
def latest_log():           
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
    
        get_timestamp = "SELECT user_id FROM logged_in WHERE time_stamp = (SELECT MAX(time_stamp) FROM logged_in)"
        cursor.execute(get_timestamp)
    
        record = cursor.fetchone()
    
        return record
    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
    except Exception as e:
        print("Error:", str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
query_res = latest_log()
logged_acc = query_res[0]

def login():
    username1 = entry_username2.get()
    password1 = entry_password2.get()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(prepared=True)  

        query = "SELECT user_id FROM user WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username1, password1))

        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful")
            login_username = username1  # Store the successful username
            login_user_id = result[0]
            logged_in_label.config(text=f"Logged in as: {username1}")
            
            insert_logged_in_record(login_user_id, login_username)
            show_page1()
            
        else:
            messagebox.showinfo("Error", "Invalid username/password\nPlease try again!")

    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
        messagebox.showinfo("Error", "An error occurred while logging in.")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showinfo("Error", "An error occurred while logging in.")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            

logged_in_label = tk.Label(frame1, text="")
print(logged_in_label)

login_label = tk.Label(frame11, text="Manipal Online Bookstore", font=("Arial", 16, "bold"))
login_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
label_username1 = tk.Label(frame11, text="Username:", font=("Arial", 14, "bold"))
label_password1 = tk.Label(frame11, text="Password:", font=("Arial", 14, "bold"))
entry_username2 = tk.Entry(frame11)
entry_password2 = tk.Entry(frame11, show="*")

button_forgot_password = tk.Button(frame11, text="Forgot Password", command=show_page5)
button_admin_login = tk.Button(frame11, text="Admin Login", command=show_page6)

button_submit = tk.Button(frame11, text="Login", command=login)

label_username1.grid(row=1, column=0, padx=10, pady=10, sticky="e")
label_password1.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_username2.grid(row=1, column=1, padx=10, pady=5)
entry_password2.grid(row=2, column=1, padx=10, pady=5)
button_submit.grid(row=3, columnspan=2, pady=10)


button_forgot_password.grid(row=3, column=1, padx=10, pady=5)
button_admin_login.grid(row=5, columnspan=2, pady=10)

def submit_id():
    result = login()
    login_username, login_user_id = result
    print("Username:", login_username)
    print("id:", login_user_id)
    global account_id
    account_id = login_user_id
    
def show_frame1():
    file_menu = Menu(menubar, tearoff=0, font=menu_font)
    account_menu = Menu(menubar, tearoff=0)
    orders_menu = Menu(menubar, tearoff=0)
    cart_menu = Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label="Home", menu=file_menu)
    menubar.add_cascade(label="Account", menu=account_menu)
    menubar.add_cascade(label="My Orders", menu=orders_menu)
    menubar.add_cascade(label="My Cart", menu=cart_menu)
    
    file_menu.add_command(label="ID", command=submit_id, font=font2)
    file_menu.add_command(label="Homepage", command=show_page1, font=font2)
    
    account_menu.add_command(label="Orders", command=show_page4, font=font2)
    account_menu.add_command(label="Logout", command=submit_id, font=font2)
    
    cart_menu.add_command(label="View my cart", command=show_page3,font=font2)
    
def show_frame2():
    menubar2 = tk.Menu(root)
    root.config(menu=menubar2)
    
    edit_menu = tk.Menu(menubar2, tearoff=0)
    menubar2.add_cascade(label="Edit", menu=edit_menu)
    
    edit_menu.add_command(label="Add Book", command=show_page9)
    edit_menu.add_command(label="Edit book", command=show_page10)
    edit_menu.add_command(label="View inventory", command=show_page8)
    edit_menu.add_command(label="View Users", command=show_page7)
    
l1 = Label(frame1, text="Search for Title", font=font2)
l1.grid(row=0, column=0)

title_text = tk.StringVar()
e1 = tk.Entry(frame1, textvariable=title_text, width=20)
e1.grid(row=0, column=1, sticky="w")

result_text = tk.Text(frame1, wrap=tk.WORD, height=5, width=50)
result_text.grid(row=1, column=0, columnspan=3)

# Make the Text widget read-only
result_text.config(state=tk.DISABLED)

 
def perform_search():
    # Clear any previous results
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    search_text = title_text.get()

    results = backend.search_title(search_text)
    print("Search Results:", results)
    if results:
        # insert into widget
        for result in results:
            result_text.insert(tk.END, result)
            result_text.insert(tk.END, "\n")
    else:
        # Handle the case where there are no results
        result_text.insert(tk.END, "No results found")
        
search_button = tk.Button(frame1, text="Go", command=perform_search, bg="lightblue")
search_button.grid(row=0, column=2)


book_titles = backend.fetch_books()
book_authors = backend.fetch_authors()
book_publisher = backend.fetch_publisher()
book_language = backend.fetch_language()
book_prices = backend.fetch_prices()
book_isbns = backend.fetch_bookisbn()

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)


label1 = Label(frame1, text="Book", font=font2)
label2 = Label(frame1, text="Authors", font=font2)
label6 = Label(frame1, text="Publisher", font=font2)
label7 = Label(frame1, text="Language", font=font2)
label9 = Label(frame1, text="Price", font=font2)
label10 = Label(frame1, text="ISBN", font=font2)
label8 = Label(frame1, text="       ")

label1.grid(row=3, column=1, sticky="w")
label2.grid(row=3, column=2, sticky="w")
label6.grid(row=3, column=3, sticky="w")
label7.grid(row=3, column=4, sticky="w")
label8.grid(row=3, column=6, sticky="w")
label9.grid(row=3, column=5, sticky="w")
label10.grid(row=3, column=0, sticky="w")


for i, Name in enumerate(book_titles, start=4):
    label3 = Label(frame1, text=Name, font=font2)
    label3.grid(row=i, column=1, sticky="w")  


for i, authors in enumerate(book_authors, start=4):
    label4 = Label(frame1, text=authors, font=font2)
    label4.grid(row=i, column=2, sticky="w")
    
for i, publishers in enumerate(book_publisher, start=4):
    label4 = Label(frame1, text=publishers, font=font2)
    label4.grid(row=i, column=3, sticky="w")

for i, languages in enumerate(book_language, start=4):
    label4 = Label(frame1, text=languages, font=font2)
    label4.grid(row=i, column=4, sticky="w")

for i, prices in enumerate(book_prices, start=4):
        label4 = Label(frame1, text=prices, font=font2)
        label4.grid(row=i, column=5, sticky="w")

for i, booki in enumerate(book_isbns, start=4):
        label4 = Label(frame1, text=booki, font=font2)
        label4.grid(row=i, column=0, sticky="w")
  
for i in range(4, len(book_titles) + 4):
    for j in range(4, len(book_titles) + 4):
        book_isbn = book_isbns[i - 4]
        book_name = book_titles[i - 4]
        price = book_prices[i - 4]
        user_id = 1
    
        button = Button(frame1, text="Add to Cart", command=lambda: backend.insert_to_cart( book_isbn, book_name, price, logged_acc), font=font2, bg="lightblue", fg="black")
        button.grid(row=i, column=6, sticky="w")

"""frame 2"""

frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=2)

book_cart_title = backend.fetch_booktitle_cart()
book_cart_price = backend.fetch_bookprice_cart()
book_cart_price2 = backend.fetch_bookprice_car()
total_price = sum(book_cart_price2)
#book_quantity = backend.get_book_quantity()

label11 = Label(frame2, text="Book Name", font=font2)
label12 = Label(frame2, text="Price", font=font2)
label13 = Label(frame2, text="Quantity", font=font2)

label11.grid(row=1, column=1, sticky="w")
label12.grid(row=1, column=2, sticky="w")
label13.grid(row=1, column=3, sticky="w")


total_label = Label(frame2, text=f"Total Price: {total_price}", font=font2)
total_label.grid(row=5, column=7, sticky="w")


for i, b_isbns in enumerate(book_cart_title, start=4):
    label3 = Label(frame2, text=b_isbns, font=font2)
    label3.grid(row=i, column=1, sticky="w") 


for i, b_price_cart in enumerate(book_cart_price, start=4):
    label3 = Label(frame2, text=b_price_cart, font=font2)
    label3.grid(row=i, column=2, sticky="w")
    
cart_details = len(backend.get_cart_details_count())
    
for i in range(4, cart_details + 4):
    for j in range(4, cart_details + 4):
       # book_isbn = book_isbns[i - 4]
        book_name = book_titles[i - 4]
        book_quantity = backend.get_book_quantity(book_name)
        #price = book_prices[i - 4]
        user_id = 1
        label3 = Label(frame2, text=book_quantity, font=font2)
        label3.grid(row=i, column=3, sticky="w")

# Loop delete buttons
cart_details = len(backend.get_cart_details_count())

# buttons for each cart item
for i in range(4, cart_details + 4):
    # You can create buttons here
    button = Button(frame2, text="Delete", command=lambda: backend.delete_from_cart( book_isbn, book_name, logged_acc), font=font2, bg="lightblue")
    button.grid(row=i, column=6, sticky="w")

#for i in range(4, cart_details + 4):
for i in range(4, cart_details + 4):
    for j in range(4, cart_details + 4):
     total_price2 = sum(book_cart_price2)
     cart_details2 = len(backend.get_cart_details_count())
     #book_isbn = book_isbns[i - 4]
     user_id = 1
     #totalamount = total_price2
     book_name = book_titles[i - 4]
     quantityc1 = cart_details2

place_button = Button(frame2, text="Place order", command=lambda: backend.place_order(logged_acc, total_price2, quantityc1), bg="lightblue")
place_button.grid(row=(cart_details+4), column=6)

"""frame 4"""

tree = ttk.Treeview(frame4, columns=("No_of_books", "Amount", "User_id", "Date_of_order"), show="headings")
tree.heading("No_of_books", text="No_of_books")
tree.heading("Amount", text="Amount")
tree.heading("User_id", text="User_id")
tree.heading("Date_of_order", text="Date_of_order")

user_id12 = logged_acc

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Assuming you have a 'orders' table with columns 'No_of_books', 'Amount', 'User_id', and 'Date_of_order'
    query = "SELECT No_of_books, Amount, User_id, Date_of_order FROM order_list WHERE User_id = %s"
    cursor.execute(query, (user_id12,))
    
    orders = cursor.fetchall()

    for order in orders:
        tree.insert("", "end", values=order)

    tree.pack(fill=tk.BOTH, expand=True)

except mysql.connector.Error as err:
    print("MySQL Error:", str(err))
except Exception as e:
    print("Error:", str(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

"""frame 5"""
def update_password(username, new_password):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    try:
        update_query = "UPDATE user SET password = %s WHERE user_name = %s"
        cursor.execute(update_query, (new_password, username))
        connection.commit()
        messagebox.showinfo("Success", "Password updated successfully!")
    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
        messagebox.showerror("Failure", "An error occurred while updating the password.")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Failure", "An error occurred while updating the password.")

            
label_title2 = tk.Label(frame5, text="Change Password!", font=("Arial", 16, "bold"))
label_title2.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label_username_5 = tk.Label(frame5, text="Username:")
label_username_5.grid(row=1, column=0)
entry_username_5 = tk.Entry(frame5)
entry_username_5.grid(row=1, column=1)

label_new_password_5 = tk.Label(frame5, text="New Password:")
label_new_password_5.grid(row=2, column=0)
entry_new_password_5 = tk.Entry(frame5)  # Masking the new password
entry_new_password_5.grid(row=2, column=1)

label_confirm_password_5 = tk.Label(frame5, text="Confirm Password:")
label_confirm_password_5.grid(row=3, column=0)
entry_confirm_password_5 = tk.Entry(frame5, show="*")  # Masking the confirm password
entry_confirm_password_5.grid(row=3, column=1)

label_cust_email_5 = tk.Label(frame5, text="Email:")
label_cust_email_5.grid(row=4, column=0)
entry_cust_email_5 = tk.Entry(frame5)
entry_cust_email_5.grid(row=4, column=1)

# Button to update password
update_button_5 = tk.Button(frame5, text="Update Password", command=lambda: update_password(entry_username_5.get(), entry_new_password_5.get()))
update_button_5.grid(row=6, columnspan=2)

update_button_5 = tk.Button(frame5, text="cancel", command=cancel_page5)
update_button_5.grid(row=7, columnspan=2)

"""frame 6"""

def admin_login(username, password):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Assuming you have an 'admin' table with 'admin_username' and 'admin_password' columns
        query = "SELECT admin_id FROM admin WHERE admin_username = %s AND password = %s"
        cursor.execute(query, (username, password))

        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Admin login successful")
            show_page7()
            # Add your code here for admin actions
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
        messagebox.showerror("Error", "An error occurred while logging in as admin.")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Error", "An error occurred while logging in as admin.")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
admin_6 = tk.Label(frame6, text="Admin Login:", font=("Arial", 16, "bold"))
admin_6.grid(row=0, column=1) 
filler_6 = tk.Label(frame6, text="             ", bg="lightblue")
filler_6.grid(row=1, column=0)         
label_username_6 = tk.Label(frame6, text="Admin Username:", font=("Arial", 12))
label_username_6.grid(row=2, column=0)
entry_username_6 = tk.Entry(frame6)
entry_username_6.grid(row=2, column=1)

label_password_6 = tk.Label(frame6, text="Password:", font=("Arial", 12))
label_password_6.grid(row=3, column=0)
entry_password_6 = tk.Entry(frame6, show="*")  # Masking the password
entry_password_6.grid(row=3, column=1)

filler_2_6 = tk.Label(frame6, text="             ", bg="lightblue")
filler_2_6.grid(row=4, column=0) 
# Button for admin login
login_button_6 = tk.Button(frame6, text="Login", command=lambda: admin_login(entry_username_6.get(), entry_password_6.get()), font=("Arial", 12))
login_button_6.grid(row=5, columnspan=4)

"""frame 7"""

username_a= backend.fetch_username()
fullname_a = backend.fetch_fullname()
dateofbirth_a = backend.fetch_dob()
address_a = backend.fetch_address()
phonenumber_a = backend.fetch_phonenumber()
email_id_a = backend.fetch_email_id()
user_id_a = backend.fetch_user_id()

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)


label1 = Label(frame7, text="Username", font=font2)
label2 = Label(frame7, text="Name", font=font2)
label6 = Label(frame7, text="Date of birth", font=font2)
label7 = Label(frame7, text="Address", font=font2)
label9 = Label(frame7, text="Phone Number", font=font2)
label10 = Label(frame7, text="Email ID", font=font2)
label11 = Label(frame7, text="User ID", font=font2)

label1.grid(row=1, column=1, sticky="w")
label2.grid(row=1, column=3, sticky="w")
label6.grid(row=1, column=4, sticky="w")
label7.grid(row=1, column=5, sticky="w")
label9.grid(row=1, column=6, sticky="w")
label10.grid(row=1, column=7, sticky="w")
label11.grid(row=1, column=2, sticky="w")

for i, Name in enumerate(username_a, start=3):
    label3 = Label(frame7, text=Name, font=font2)
    label3.grid(row=i, column=1, sticky="w")  # Align labels to the left within the column frame


for i, authors in enumerate(fullname_a, start=3):
    label4 = Label(frame7, text=authors, font=font2)
    label4.grid(row=i, column=3, sticky="w")
    
for i, publishers in enumerate(dateofbirth_a, start=3):
    label4 = Label(frame7, text=publishers, font=font2)
    label4.grid(row=i, column=4, sticky="w")

for i, languages in enumerate(address_a, start=3):
    label4 = Label(frame7, text=languages, font=font2)
    label4.grid(row=i, column=5, sticky="w")

for i, prices in enumerate(phonenumber_a, start=3):
        label4 = Label(frame7, text=prices, font=font2)
        label4.grid(row=i, column=6, sticky="w")

for i, booki in enumerate(email_id_a, start=3):
        label4 = Label(frame7, text=booki, font=font2)
        label4.grid(row=i, column=7, sticky="w")
        
for i, booki in enumerate(user_id_a, start=3):
        label4 = Label(frame7, text=booki, font=font2)
        label4.grid(row=i, column=2, sticky="w")
        
menubar = tk.Menu(root)
root.config(menu=menubar)

menu_font = ("Arial", 16) 

book_name_a = backend.fetch_name()
book_authors_a = backend.fetch_book_author()
book_publisher_a = backend.fetch_publisher()
book_language_a = backend.fetch_language()
book_prices_a = backend.fetch_book_price()
book_isbns_a = backend.fetch_book_isbn()

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)


label1 = Label(frame8, text="Book Name", font=font2)
label2 = Label(frame8, text="Authors", font=font2)
label6 = Label(frame8, text="Publisher", font=font2)
label7 = Label(frame8, text="Language", font=font2)
label9 = Label(frame8, text="Price", font=font2)
label10 = Label(frame8, text="ISBN", font=font2)

label1.grid(row=1, column=1, sticky="w")
label2.grid(row=1, column=2, sticky="w")
label6.grid(row=1, column=3, sticky="w")
label7.grid(row=1, column=4, sticky="w")
label9.grid(row=1, column=5, sticky="w")
label10.grid(row=1,column=6,sticky="w")


for i, Name in enumerate(book_name_a, start=3):
    label3 = Label(frame8, text=Name, font=font2)
    label3.grid(row=i, column=1, sticky="w")  # Align labels to the left within the column frame


for i, authors in enumerate(book_authors_a, start=3):
    label4 = Label(frame8, text=authors, font=font2)
    label4.grid(row=i, column=2, sticky="w")
    
for i, publishers in enumerate(book_publisher_a, start=3):
    label4 = Label(frame8, text=publishers, font=font2)
    label4.grid(row=i, column=3, sticky="w")

for i, languages in enumerate(book_language_a, start=3):
    label4 = Label(frame8, text=languages, font=font2)
    label4.grid(row=i, column=4, sticky="w")

for i, prices in enumerate(book_prices_a, start=3):
        label4 = Label(frame8, text=prices, font=font2)
        label4.grid(row=i, column=5, sticky="w")

for i, booki in enumerate(book_isbns_a, start=3):
        label4 = Label(frame8, text=booki, font=font2)
        label4.grid(row=i, column=6, sticky="w")



"""frame 9"""
def insert_book_details():
    # Get values from input fields
    book_name = entry_nameb.get()
    book_author = entry_author.get()
    publisher = entry_publisher.get()
    language = entry_language.get()
    book_price = entry_price.get()
    book_isbn = entry_isbn.get()

    try:
        # Establish a database connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # SQL query to insert book details into the 'book_details' table
        insert_query = "INSERT INTO book_details (Name, book_author, Publisher, Language, book_price, book_isbn) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (book_name, book_author, publisher, language, book_price, book_isbn)
        cursor.execute(insert_query, data)

        # Commit the transaction
        connection.commit()

        # Show a success message
        messagebox.showinfo("Success", "Book details inserted successfully!")

    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
        messagebox.showerror("Failure", "An error occurred while inserting book details.")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Failure", "An error occurred while inserting book details.")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

label_addb = tk.Label(frame9, text="Add Book", font=font)
label_addb.grid(row=0, column=0, padx=10, pady=5)

label_nameb = tk.Label(frame9, text="Name:", font=font2)
entry_nameb = tk.Entry(frame9)

label_author = tk.Label(frame9, text="Author:", font=font2)
entry_author = tk.Entry(frame9)

label_publisher = tk.Label(frame9, text="Publisher:", font=font2)
entry_publisher = tk.Entry(frame9)

label_language = tk.Label(frame9, text="Language:", font=font2)
entry_language = tk.Entry(frame9)

label_price = tk.Label(frame9, text="Price:", font=font2)
entry_price = tk.Entry(frame9)

label_isbn = tk.Label(frame9, text="ISBN:", font=font2)
entry_isbn = tk.Entry(frame9)

# Create a button to insert book details
inserter_button = tk.Button(frame9, text="Insert", font=font2, command=insert_book_details)

# Organize widgets using grid layout
label_nameb.grid(row=1, column=0, padx=10, pady=5)
entry_nameb.grid(row=1, column=1, padx=10, pady=5)

label_author.grid(row=2, column=0, padx=10, pady=5)
entry_author.grid(row=2, column=1, padx=10, pady=5)

label_publisher.grid(row=3, column=0, padx=10, pady=5)
entry_publisher.grid(row=3, column=1, padx=10, pady=5)

label_language.grid(row=4, column=0, padx=10, pady=5)
entry_language.grid(row=4, column=1, padx=10, pady=5)

label_price.grid(row=5, column=0, padx=10, pady=5)
entry_price.grid(row=5, column=1, padx=10, pady=5)

label_isbn.grid(row=6, column=0, padx=10, pady=5)
entry_isbn.grid(row=6, column=1, padx=10, pady=5)

inserter_button.grid(row=7, column=0, columnspan=2, pady=10)

"""frame 10"""

def delete_book():
    # Get values from input fields
    book_named = entry_namebd.get()
    book_isbnd = entry_isbnd.get()

    try:
        # Establish a database connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # SQL query to delete a book based on its name and ISBN
        delete_query = "DELETE FROM book_details WHERE Name = %s AND book_isbn = %s"
        data = (book_named, book_isbnd)
        cursor.execute(delete_query, data)

        # Commit the transaction
        connection.commit()

        # Show a success message
        messagebox.showinfo("Success", "Book deleted successfully!")

    except mysql.connector.Error as err:
        print("MySQL Error:", str(err))
        messagebox.showerror("Failure", "An error occurred while deleting the book.")
    except Exception as e:
        print("Error:", str(e))
        messagebox.showerror("Failure", "An error occurred while deleting the book.")
    finally:
        if connection.is_connected():
            cursor.close()
            
label_addbd = tk.Label(frame10, text="Remove Book", font=font)
label_addbd.grid(row=0, column=0, padx=10, pady=5)

label_namebd = tk.Label(frame10, text="Name:", font=font2)
entry_namebd = tk.Entry(frame10)

label_isbnd = tk.Label(frame10, text="ISBN:", font=font2)
entry_isbnd = tk.Entry(frame10)

# Create a button to insert book details
deleter_button = tk.Button(frame10, text="Delete", font=font2, command=delete_book)

# Organize widgets using grid layout
label_namebd.grid(row=1, column=0, padx=10, pady=5)
entry_namebd.grid(row=1, column=1, padx=10, pady=5)

label_isbnd.grid(row=6, column=0, padx=10, pady=5)
entry_isbnd.grid(row=6, column=1, padx=10, pady=5)

deleter_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()