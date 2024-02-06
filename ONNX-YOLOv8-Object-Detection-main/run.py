import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

def start_object_detection():
    object_detection_thread = threading.Thread(target=run_script, args=('object_detection.py',))
    object_detection_thread.start()

def start_text_extraction():
    text_extraction_thread = threading.Thread(target=run_script, args=('text_extraction.py',))
    text_extraction_thread.start()

def stop_scripts():
    messagebox.showinfo("Stop", "Stopping scripts...")
    # Add code to stop or terminate the running scripts

# Create the main window
root = tk.Tk()
root.title("SVAG Script Runner Applet")
root.geometry("400x200")

# Apply a colorful theme
style = ttk.Style()
style.theme_use("clam")

# Configure a custom style for SVAG
style.configure("SVAG.TButton", foreground="white", background="#4CAF50", font=('Arial', 12, 'bold'))

# Create buttons with the custom SVAG style
object_detection_button = ttk.Button(root, text="Run Object Detection", style="SVAG.TButton", command=start_object_detection)
object_detection_button.pack(pady=10, padx=20, fill=tk.X)

text_extraction_button = ttk.Button(root, text="Run Text Extraction", style="SVAG.TButton", command=start_text_extraction)
text_extraction_button.pack(pady=10, padx=20, fill=tk.X)

stop_button = ttk.Button(root, text="Stop", style="SVAG.TButton", command=stop_scripts)
stop_button.pack(pady=10, padx=20, fill=tk.X)

# Start the main loop
root.mainloop()
