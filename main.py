import os
import argparse
import math
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_prefix, start_page, end_page, pages_per_file):
    pdf_reader = PdfReader(input_path)
    total_pages = len(pdf_reader.pages)

    # ページ範囲の設定
    start_page = 1 if start_page is None else max(1, min(start_page, total_pages))
    end_page = total_pages if end_page is None else min(end_page, total_pages)

    # 0-indexedに調整
    start_index = start_page - 1
    end_index = end_page

    # outputディレクトリが存在しない場合は作成
    os.makedirs('output', exist_ok=True)

    if pages_per_file:
        # 指定されたページ数ごとに分割
        for i in range(start_index, end_index, pages_per_file):
            pdf_writer = PdfWriter()
            batch_end = min(i + pages_per_file, end_index)

            for page_num in range(i, batch_end):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            output_filename = f"output/{output_prefix}_{i+1:04d}-{batch_end:04d}.pdf"
            with open(output_filename, "wb") as output_file:
                pdf_writer.write(output_file)
            print(f"Created: {output_filename}")
    else:
        # 分割せずに1つのファイルとして出力
        pdf_writer = PdfWriter()
        for page_num in range(start_index, end_index):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        output_filename = f"output/{output_prefix}_{start_page:04d}-{end_page:04d}.pdf"
        with open(output_filename, "wb") as output_file:
            pdf_writer.write(output_file)
        print(f"Created: {output_filename}")

def main():
    parser = argparse.ArgumentParser(description="Split PDF file.")
    parser.add_argument("--input", required=True, help="Input PDF file path")
    parser.add_argument("--output", required=True, help="Output file prefix")
    parser.add_argument("--start", type=int, help="Start page number (optional)")
    parser.add_argument("--end", type=int, help="End page number (optional)")
    parser.add_argument("--split", type=int, help="Number of pages per split file (optional)")

    args = parser.parse_args()

    split_pdf(args.input, args.output, args.start, args.end, args.split)

if __name__ == "__main__":
    main()
