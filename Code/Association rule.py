#Association rule

import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()
root.title("Association Rule")
root.geometry("500x300") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.


support_var=tk.DoubleVar() 
confidence_var=tk.DoubleVar() 
lift_var=tk.DoubleVar() 
length_var=tk.DoubleVar() 

# Frame for result
result_frame = tk.LabelFrame(root, text="Result")
result_frame.place(height=50, width=500, rely=0.75, relx=0)

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=500, rely=0.35, relx=0)

#Create Text Boxes Labels
min_support_label = Label(root ,text = "Min support").grid(row = 0,column = 0)
min_confidence_Label = Label(root ,text = "Min confidence").grid(row = 1,column = 0)
min_lift_Label = Label(root ,text = "Min lift").grid(row = 2,column = 0)
min_length_Label = Label(root ,text = "Min length").grid(row = 3,column = 0)
# Create Text Boxes
min_support = Entry(root,textvariable = support_var).grid(row = 0,column = 1)
min_confidence = Entry(root,textvariable = confidence_var).grid(row = 1,column = 1)
min_lift = Entry(root,textvariable = lift_var).grid(row = 2,column = 1)
min_length = Entry(root,textvariable = length_var).grid(row = 3,column = 1)


# Buttons
button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
button2.place(rely=0.65, relx=0.30)

# The file/file path text
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)

# Result  text
label_result = ttk.Label(result_frame, text="No result")
label_result.place(rely=0, relx=0)



def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("csv files", "*.csv"),("All Files", "*.*")))
    label_file["text"] = filename
    
    return None


def Load_excel_data():
 
    support=support_var.get()
    confidence=confidence_var.get()
    lift=lift_var.get()
    length=length_var.get()    
    print(support)
    
# Data Preprocessing
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)   
        df = pd.read_csv(excel_filename, header = None)
        
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None
    label_result["text"] = "Well done the result sent into a file in your path "
    
    transactions = []
    for i in range(0, 5):
        transactions.append([str(df.values[i,j]) for j in range(0, 5)])
        
        # Training the Apriori model on the dataset
        from apyori import apriori
        rules = apriori(transactions, min_support = support, min_confidence = confidence, min_lift = lift, min_length = length)
        
        # Visualising the results
        results = list(rules)
        print(results)
        

   
root.mainloop()
