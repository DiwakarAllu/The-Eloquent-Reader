import pyttsx3
import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

# Function to convert PDF to speech
def convert_pdf_to_speech(pdf_path, speech_rate):
    doc = fitz.open(pdf_path)
    speaker = pyttsx3.init()
    speaker.setProperty('rate', speech_rate)

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text()
        speaker.say(text)
        speaker.runAndWait()

# Function to browse for a PDF file
def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_path.set(file_path)

# Function to convert and speak
def convert_and_speak():
    pdf_file = pdf_path.get()
    rate = int(speech_rate.get())
    if pdf_file:
        convert_pdf_to_speech(pdf_file, rate)
    else:
        result_label.config(text="Please select a PDF file.")

# Create the main application window
app = tk.Tk()
app.title("The Eloquent Reader")

# Variables for PDF path and speech rate
pdf_path = tk.StringVar()
speech_rate = tk.StringVar()
speech_rate.set(150)

# Define colors for styling
bg_color = "#F6F7F8"
label_color = "#333333"
button_color = "#6AC7F3"

# Create and configure widgets
file_label = tk.Label(app, text="Select PDF File:", bg=bg_color, fg=label_color)
file_entry = tk.Entry(app, textvariable=pdf_path, width=40)
browse_button = tk.Button(app, text="Browse", command=browse_pdf, bg=button_color, fg="white")
rate_label = tk.Label(app, text="Speech Rate (words per minute):", bg=bg_color, fg=label_color)
rate_entry = tk.Entry(app, textvariable=speech_rate)
convert_button = tk.Button(app, text="Convert and Speak", command=convert_and_speak, bg=button_color, fg="white")
result_label = tk.Label(app, text="", bg=bg_color, fg="red")

# Place widgets in the window
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button.grid(row=0, column=2, padx=10, pady=10)
rate_label.grid(row=1, column=0, padx=10, pady=10)
rate_entry.grid(row=1, column=1, padx=10, pady=10)
convert_button.grid(row=2, column=1, padx=10, pady=10)
result_label.grid(row=3, column=1, padx=10, pady=10)

# Start the main loop
app.mainloop()
