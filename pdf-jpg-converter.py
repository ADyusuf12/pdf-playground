import fitz  # PyMuPDF
import os
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pdf_to_jpg(pdf_path, output_folder):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        if not pdf_document.is_encrypted:
            logging.info(f"Successfully opened {pdf_path}")
        else:
            logging.warning(f"{pdf_path} is encrypted. Ensure it is decrypted before processing.")

        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        for page_num in range(len(pdf_document)):
            # Select page
            page = pdf_document.load_page(page_num)
            
            # Get the page dimensions
            pix = page.get_pixmap()
            
            # Define output path
            output_path = os.path.join(output_folder, f"page_{page_num + 1}.jpg")
            
            # Save as JPG
            pix.save(output_path)
            logging.info(f"Saved page {page_num + 1} as {output_path}")
        
        print(f"All pages converted and saved in {output_folder}")
    except Exception as e:
        logging.error(f"Failed to convert PDF to JPG: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert PDF pages to JPG images.')
    parser.add_argument('pdf_path', help='Path to the input PDF file')
    parser.add_argument('output_folder', help='Folder to save the output JPG images')
    args = parser.parse_args()
    
    pdf_to_jpg(args.pdf_path, args.output_folder)

if __name__ == '__main__':
    main()
