import PyPDF2
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_watermark(input_file, output_file, watermark_file, pages=None, password=None):
    try:
        template = PyPDF2.PdfFileReader(open(input_file, 'rb'))
        if template.isEncrypted and password:
            template.decrypt(password)
        watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))
        output = PyPDF2.PdfFileWriter()
        
        total_pages = template.getNumPages()
        pages_to_watermark = pages if pages else list(range(total_pages))
        
        for i in range(total_pages):
            page = template.getPage(i)
            if i in pages_to_watermark:
                page.mergePage(watermark.getPage(0))
            output.addPage(page)
        
        with open(output_file, 'wb') as file:
            output.write(file)
        logging.info(f"Successfully added watermark to {input_file} and saved as {output_file}")
    except Exception as e:
        logging.error(f"Failed to add watermark to PDF: {e}")

def main():
    parser = argparse.ArgumentParser(description='Add a watermark to a PDF file.')
    parser.add_argument('input_file', help='Path to the input PDF file')
    parser.add_argument('output_file', help='Path to save the watermarked PDF file')
    parser.add_argument('watermark_file', help='Path to the watermark PDF file')
    parser.add_argument('--pages', nargs='+', type=int, help='Specific pages to watermark (default: all pages)', default=None)
    parser.add_argument('--password', help='Password for encrypted PDF (if any)', default=None)
    args = parser.parse_args()
    
    add_watermark(args.input_file, args.output_file, args.watermark_file, args.pages, args.password)

if __name__ == '__main__':
    main()
