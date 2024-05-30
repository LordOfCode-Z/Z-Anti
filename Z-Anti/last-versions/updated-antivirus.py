import tkinter as tk
import hashlib
import tkinter.filedialog

def scan():
    # Get the selected file path
    file_path = file_dialog.get()
    
    # Open the file and get the hash
    with open(file_path, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()

    # Check the hash against the known virus hashes
    virus_found = False
    with open("SHA256-Hashes_pack.txt", 'r') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            if str(readable_hash) == str(line.split(";")[0]):
                virus_found = True
                break

    # Display the result
    if virus_found:
        result_label.config(text=f"{file_path} Dosyasında Virüs Tespit Edildi")
    else:
        result_label.config(text=f"{file_path} Dosyasında Virüs Tespit Edilemedi")

# Create the main window
root = tk.Tk()
root.title("Z-Antivirus")

# Create a label and entry field for the file path
file_label = tk.Label(root, text="Select a file to scan:")
file_label.pack()
file_dialog = tkinter.filedialog.Open(root, filetypes=[('Executable files', '*.exe')])
file_dialog.pack()

# Create a button to start the scan
scan_button = tk.Button(root, text="Scan", command=scan)
scan_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()