from docx import Document

def srt_to_words(srt_file, encoding='utf-8'):
    """Reads an SRT file and converts it to words."""
    words = []
    with open(srt_file, 'r', encoding=encoding, errors='ignore') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.isdigit():
                continue  # Skip line numbers
            elif line:
                words += line.split()
    return words

def save_to_word(words, output_file):
    """Saves a list of words to a Word file."""
    doc = Document()
    for word in words:
        doc.add_paragraph(word)
    doc.save(output_file)

# Example usage
srt_file = '45meeting.srt'  # Replace with the path to your SRT file
output_file = 'output.docx'  # Specify the path for the output Word file
words = srt_to_words(srt_file, encoding='utf-8')  # Specify the correct encoding
save_to_word(words, output_file)
print(f'Words saved to {output_file}.')
