
# SRT to Word Converter

This is a simple program that converts SubRip Subtitle (SRT) files to Microsoft Word (.docx) files using the docx and tkinter libraries in Python.

# Dependencies

The program requires the following libraries to be installed in order to run:

docx: A library for creating, modifying, and extracting information from Microsoft Word files.
tkinter: The standard Python interface to the Tk GUI toolkit.

# Installation

To use this program for editing purpose , you need to have Python installed on your system. You can download Python from the official Python website (https://www.python.org/).

Once you have Python installed, you can install the docx library using pip, the Python package manager, by running the following command in your terminal or command prompt:

```bash
pip install python-docx
```

The tkinter library comes pre-installed with Python, so you don't need to install it separately.


# Usage

## Running the Program

To run the program, you can execute the Python script in your Python environment. The script will open a simple Tkinter GUI window with instructions for the user.

The user should click on the "Upload SRT File" button to open a file dialog.

The user can then select an SRT file from their local file system.

The program will convert the SRT file to a Word file (.docx) with the same name as the SRT file and display a success message.

## Editing the Code
If you want to edit the code for your own use, you can follow these steps:

Download or clone the code from GitHub in srttoword.py 

Open the Python script in a text editor or an Integrated Development Environment (IDE) of your choice.

Paste the code for you need, and save your changes.

## Using Git to Download the Code

If you want to download the code using Git, you can follow these steps:
Install Git on your system if you don't have it already. You can download Git from the official Git website (https://git-scm.com/).
Open a command prompt or terminal window.
Navigate to the directory where you want to download the code.
Run the following command to clone the repository to your local machine:
```bash
git clone https://github.com/haohao3945/srttoword
```

## Code Explanation
The provided code is a simple GUI application that allows users to convert an SRT file (a subtitle file format) to a Word document. It uses the docx library to create a Word document and the tkinter library to create a graphical user interface.

The code consists of the following main functions:
1. srt_to_words(srt_file, encoding='utf-8'): This function takes an SRT file path as input and returns a list of words extracted from the file. It reads the SRT file line by line, skips line numbers and timeline information, and extracts words from the remaining lines.
2. save_to_word(words, output_file): This function takes a list of words and an output file path as input and saves the words to a Word document using the docx library. It creates a new Word document, adds each word as a paragraph, and saves the document with the provided output file path.
3. upload_srt(): This function is called when the user clicks the "Upload SRT File" button in the GUI. It opens a file dialog for the user to select an SRT file, and then calls the srt_to_words() and save_to_word() functions to convert and save the selected SRT file to a Word document.
4. root: This is the main window of the GUI created using the tkinter library. It contains a label with instructions, a button for uploading SRT files, and a main loop that handles user interactions with the GUI.
