from docx import Document
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def srt_to_words(srt_file, encoding='utf-8'):
    # Reads an SRT file and converts it to words.
    words = []
    with open(srt_file, 'r', encoding=encoding, errors='ignore') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.isdigit() or ' --> ' in line:
                continue  # Skip line numbers and timeline
            elif line:
                words += line.split()
    return words

def save_to_word(words, output_file):
    # Saves a list of words to a Word file.
    doc = Document()
    for word in words:
        doc.add_paragraph(word)
    doc.save(output_file)
    messagebox.showinfo("Success", f'Words saved to {output_file}.')

def upload_srt():
    # Opens a file dialog for the user to select an SRT file.
    file_path = filedialog.askopenfilename(filetypes=[('SRT Files', '*.srt')])
    if file_path:
        output_file = file_path.split('.')[0] + '.docx'  # Use the same name as the SRT file with .docx extension
        words = srt_to_words(file_path, encoding='utf-8')
        save_to_word(words, output_file)

# Create a simple Tkinter GUI
root = tk.Tk()
root.title("SRT to Word Converter")

# Instructions label
label = tk.Label(root, text="Please select an SRT file to convert to Word:")
label.pack(pady=10)

# Upload button
button = tk.Button(root, text="Upload SRT File", command=upload_srt)
button.pack(pady=10)

root.mainloop()
