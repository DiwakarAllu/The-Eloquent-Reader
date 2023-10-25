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

# Function to interpolate gradient color
def gradient_color(start_color, end_color, fraction):
    r1, g1, b1 = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
    r2, g2, b2 = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:7], 16)
    r = int(r1 + fraction * (r2 - r1))
    g = int(g1 + fraction * (g2 - g1))
    b = int(b1 + fraction * (b2 - b1))
    return f'#{r:02X}{g:02X}{b:02X}'

# Create the main application window
app = tk.Tk()
app.title("The Eloquent Reader")

# Variables for PDF path and speech rate
pdf_path = tk.StringVar()
speech_rate = tk.StringVar()
speech_rate.set(150)

# Create a canvas for the gradient background
canvas = tk.Canvas(app, width=400, height=300)
canvas.pack()

# Define gradient colors
color1 = "#6AC7F3"  # Top color
color2 = "#224D92"  # Bottom color

# Create a gradient rectangle
canvas.create_rectangle(0, 0, 400, 300, fill="", outline="")
for i in range(300):
    y0 = i
    y1 = i + 1
    canvas.create_rectangle(0, y0, 400, y1, fill=gradient_color(color1, color2, i / 300), outline="")

# Create and configure widgets
file_label = tk.Label(app, text="Select PDF File:", bg=gradient_color(color1, color2, 0.3), fg="white")
file_entry = tk.Entry(app, textvariable=pdf_path, width=40)
browse_button = tk.Button(app, text="Browse", command=browse_pdf, bg=gradient_color(color1, color2, 0.3), fg="white")
rate_label = tk.Label(app, text="Speech Rate (words per minute):", bg=gradient_color(color1, color2, 0.3), fg="white")
rate_entry = tk.Entry(app, textvariable=speech_rate)
convert_button = tk.Button(app, text="Convert and Speak", command=convert_and_speak, bg=gradient_color(color1, color2, 0.3), fg="white")
result_label = tk.Label(app, text="", bg=gradient_color(color1, color2, 0.3), fg="red")

# Place widgets in the window
file_label.pack(pady=10)
file_entry.pack(pady=10)
browse_button.pack(pady=10)
rate_label.pack(pady=10)
rate_entry.pack(pady=10)
convert_button.pack(pady=10)
result_label.pack(pady=10)

# Start the main loop
app.mainloop()
