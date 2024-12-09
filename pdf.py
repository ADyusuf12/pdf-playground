import PyPDF2
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rotate_pdf(input_file, output_file, rotation, password=None):
    try:
        with open(input_file, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            if reader.isEncrypted and password:
                reader.decrypt(password)
            writer = PyPDF2.PdfFileWriter()
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                page.rotateCounterClockwise(rotation)
                writer.addPage(page)
            with open(output_file, 'wb') as new_file:
                writer.write(new_file)
        logging.info(f"Successfully rotated {input_file} and saved as {output_file}")
    except Exception as e:
        logging.error(f"Failed to rotate PDF: {e}")

def main():
    parser = argparse.ArgumentParser(description='Rotate a PDF file.')
    parser.add_argument('input_file', help='Path to the input PDF file')
    parser.add_argument('output_file', help='Path to save the rotated PDF file')
    parser.add_argument('rotation', type=int, help='Rotation angle in degrees (e.g., 90, 180, 270)')
    parser.add_argument('--password', help='Password for encrypted PDF (if any)', default=None)
    args = parser.parse_args()
    
    rotate_pdf(args.input_file, args.output_file, args.rotation, args.password)

if __name__ == '__main__':
    main()
