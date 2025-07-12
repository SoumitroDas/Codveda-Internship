import PyPDF2

# Path to your PDF
pdf_path = 'nb181_report.pdf'  # Update if the PDF has a different name
output_txt = 'nb181_report.txt'

try:
    # Open and read the PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text() + '\n'

    # Save to text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    print(f"Text extracted to '{output_txt}'")
except FileNotFoundError:
    print(f"Error: '{pdf_path}' not found in D:\\Study\\My Projects\\Internship\\Codveda\\Tasks")
    exit()
except Exception as e:
    print(f"Error extracting PDF: {e}")
exit()
