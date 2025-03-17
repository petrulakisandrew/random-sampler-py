import tkinter as tk
from tkinter import filedialog
import os

def save_inputs():
    report_directory = entry_file.get()
    column = entry_column.get()
    sample_size = entry_sample.get()
    sampled_data = entry_sampled_data.get()
    output_directory = entry_output_dir.get()
    
    # Use the directory of this script for consistency
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input_values.txt")
    
    try:
        with open(file_path, "w") as f:
            f.write(f"{report_directory}\n{column}\n{sample_size}\n{sampled_data}\n{output_directory}")
        print(f"Successfully saved inputs to: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
    
    root.destroy()


def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)
    
def browse_output_directory():
    folder_selected = filedialog.askdirectory()
    entry_output_dir.delete(0, tk.END)
    entry_output_dir.insert(0, folder_selected)

# Tkinter GUI Setup
root = tk.Tk()
root.title("Input Collection")

tk.Label(root, text="Select Excel File:").grid(row=0, column=0, padx=5, pady=5)
entry_file = tk.Entry(root, width=50)
entry_file.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Column Name:").grid(row=1, column=0, padx=5, pady=5)
entry_column = tk.Entry(root, width=30)
entry_column.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Sample Size:").grid(row=2, column=0, padx=5, pady=5)
entry_sample = tk.Entry(root, width=10)
entry_sample.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Output Excel File Name (without extension):").grid(row=3, column=0, padx=5, pady=5)
entry_sampled_data = tk.Entry(root, width=30)
entry_sampled_data.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Select Output Directory:").grid(row=4, column=0, padx=5, pady=5)
entry_output_dir = tk.Entry(root, width=50)
entry_output_dir.grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_output_directory).grid(row=4, column=2, padx=5, pady=5)

tk.Button(root, text="Save Inputs", command=save_inputs).grid(row=5, column=1, padx=5, pady=10)

root.mainloop()