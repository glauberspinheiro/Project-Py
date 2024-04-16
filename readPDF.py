import PyPDF2
import json

def read_pdf(pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages

        # Initialize an empty list to store text from each page
        pdf_text = []

        # Iterate through each page and extract text
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extractText()
            pdf_text.append(text)

        return pdf_text

def create_json_payload(pdf_text):
    # Create a dictionary to store the PDF text
    payload = {
        "PDF_Text": pdf_text
    }
    return payload

if __name__ == "__main__":
    # Provide the path to the PDF file
    pdf_file_path = "relatorioClientesm.pdf"

    # Read the PDF file
    pdf_text = read_pdf(pdf_file_path)

    # Create JSON payload
    payload = create_json_payload(pdf_text)

    # Print the JSON payload
    print(json.dumps(payload, indent=4))
