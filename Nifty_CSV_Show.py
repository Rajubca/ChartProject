import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load CSV
df = pd.read_csv("nifty50.csv")

# Clean column names (remove \n and extra spaces)
df.columns = df.columns.str.replace(r"\n", " ", regex=True).str.strip()

# Create GUI
root = tk.Tk()
root.title("Nifty 50 Data Viewer")
root.geometry("1000x600")

# Frame for Treeview
frame = ttk.Frame(root)
frame.pack(fill="both", expand=True)

# Create Treeview
tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")

# Define headings
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

# Insert data into table
for _, row in df.iterrows():
    tree.insert("", "end", values=list(row))

# Add scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

root.mainloop()
