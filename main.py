import pyttsx3
from PyPDF2 import PdfReader

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    pdf_file_path = "C:\\Users\\Allu Diwakar\\Desktop\\AWS_Academy_Graduate___AWS_Academy_Cloud_Architecting_Badge20231012-45-ar5cdk.pdf"  # PDF file's path
    text = extract_text_from_pdf(pdf_file_path)
    text_to_speech(text)

if __name__ == "__main__":
    main()
