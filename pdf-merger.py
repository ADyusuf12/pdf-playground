import PyPDF2
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pdf_merger(pdf_list, output_file, password=None):
    try:
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
            if reader.isEncrypted and password:
                reader.decrypt(password)
            merger.append(reader)
            logging.info(f"Appending {pdf}")
        merger.write(output_file)
        logging.info(f"Successfully merged PDFs and saved as {output_file}")
    except Exception as e:
        logging.error(f"Failed to merge PDFs: {e}")

def main():
    parser = argparse.ArgumentParser(description='Merge multiple PDF files into one.')
    parser.add_argument('pdf_files', nargs='+', help='List of PDF files to merge')
    parser.add_argument('output_file', help='Path to save the merged PDF file')
    parser.add_argument('--password', help='Password for encrypted PDFs (if any)', default=None)
    args = parser.parse_args()
    
    pdf_merger(args.pdf_files, args.output_file, args.password)

if __name__ == '__main__':
    main()
