#fetching required libraries
#pip install psycopg2
import tkinter as tk
from tkinter import messagebox
import psycopg2
from tkinter import ttk

# Function to add a new student
def add_student():
    # Retrieve input values from entry fields
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    parent_name = entry_parent_name.get()
    address = entry_address.get()
    city = entry_city.get()
    phone_number = entry_phone_number.get()

    # Validate input values
    if not first_name or not last_name or not dob or not parent_name or not address or not city or not phone_number:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Connect to the PostgreSQL database, values differ accordingly
        conn = psycopg2.connect(
            dbname="School",
            user="postgres",
            password="Sampath99@",
            host="localhost",
            port="5432"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Insert the student details into the Students table
        insert_query = "INSERT INTO Students (first_name, last_name, date_of_birth, parent_name, address, city, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (first_name, last_name, dob, parent_name, address, city, phone_number))

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Student added successfully.")

        # Clear the entry fields
        entry_first_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_dob.delete(0, tk.END)
        entry_parent_name.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_city.delete(0, tk.END)
        entry_phone_number.delete(0, tk.END)

    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))


# Function to display the list of students
def show_students():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="School",
            user="postgres",
            password="Sampath99@",
            host="localhost",
            port="5432"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Retrieve student data from the Students table
        select_query = "SELECT * FROM Students"
        cursor.execute(select_query)
        students = cursor.fetchall()

        # Close the database connection
        cursor.close()
        conn.close()

        # Create a new window for displaying the student table
        table_window = tk.Toplevel()
        table_window.title("Student's List")

        # Create a Treeview widget for the student table
        tree = ttk.Treeview(table_window)

        # Define columns
        tree["columns"] = ("first_name", "last_name", "date_of_birth", "parent_name", "address", "city", "phone_number")

        # Format columns
        tree.column("#0", width=0, stretch=tk.NO)  # Hidden column
        tree.column("first_name", width=100)
        tree.column("last_name", width=100)
        tree.column("date_of_birth", width=100)
        tree.column("parent_name", width=150)
        tree.column("address", width=150)
        tree.column("city", width=100)
        tree.column("phone_number", width=100)
        
        # Create headings
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("first_name", text="First Name", anchor=tk.W)
        tree.heading("last_name", text="Last Name", anchor=tk.W)
        tree.heading("date_of_birth", text="Date of Birth", anchor=tk.W)
        tree.heading("parent_name", text="Parent's Name", anchor=tk.W)
        tree.heading("address", text="Address", anchor=tk.W)
        tree.heading("city", text="City", anchor=tk.W)
        tree.heading("phone_number", text="Phone Number", anchor=tk.W)

        # Insert student data into the table
        for student in students:
            tree.insert("", tk.END, text="", values=student)

        # Pack the Treeview widget
        tree.pack()
        
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))

def report_students():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="School",
            user="postgres",
            password="Sampath99@",
            host="localhost",
            port="5432"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Retrieve student data from the Students and Marks tables
        select_query = """
        SELECT s.first_name, s.last_name FROM Students s JOIN (SELECT student_id, AVG(score) AS average_score
    FROM Marks GROUP BY student_id) AS avg_scores ON s.student_id = avg_scores.student_id
	WHERE avg_scores.average_score > 60"""
        
        cursor.execute(select_query)
        students = cursor.fetchall()

        # Close the database connection
        cursor.close()
        conn.close()
        
        table_window = tk.Toplevel()
        table_window.title("Student's List Who Scored Above 60%")

        tree = ttk.Treeview(table_window)

        # Define columns
        tree["columns"] = ("first_name", "last_name")

        # Format columns
        tree.column("#0", width=0, stretch=tk.NO)  # Hidden column
        tree.column("first_name", width=100)
        tree.column("last_name", width=100)
                
        # Create headings
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("first_name", text="First Name", anchor=tk.W)
        tree.heading("last_name", text="Last Name", anchor=tk.W)
        
        # Insert student data into the table
        for student in students:
            tree.insert("", tk.END, text="", values=student)

        # Pack the Treeview widget
        tree.pack()        

    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))

def execute_multiple_commands():
    add_student()  # Execute the add_student function
    show_students()  # Execute the show_students function

# Create the GUI window
window = tk.Tk()
window.title("Student Management System")

# Create labels and entry fields for student details
label_first_name = tk.Label(window, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(window)
entry_first_name.pack()

label_last_name = tk.Label(window, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(window)
entry_last_name.pack()

label_dob = tk.Label(window, text="Date of Birth(yyyy-mm-dd):")
label_dob.pack()
entry_dob = tk.Entry(window)
entry_dob.pack()

label_parent_name = tk.Label(window, text="Parent's Name:")
label_parent_name.pack()
entry_parent_name = tk.Entry(window)
entry_parent_name.pack()

label_address = tk.Label(window, text="Address:")
label_address.pack()
entry_address = tk.Entry(window)
entry_address.pack()

label_city = tk.Label(window, text="City:")
label_city.pack()
entry_city = tk.Entry(window)
entry_city.pack()

label_phone_number = tk.Label(window, text="Phone Number:")
label_phone_number.pack()
entry_phone_number = tk.Entry(window)
entry_phone_number.pack()

# Create a button to add a new student
btn_add_student = tk.Button(window, text="Add Student", command=execute_multiple_commands)
btn_add_student.pack()

# Create a button to show the list of students
#btn_show_students = tk.Button(window, text="Show Students", command=show_students)
#btn_show_students.pack()

# Create a button to show the report of students 
btn_show_students = tk.Button(window, text="Students Report(Score > 60%)", command=report_students)
btn_show_students.pack()


# Start the GUI event loop
window.mainloop()
