#!/usr/bin/python3
'''
A Script that writes markdown to html
'''
import sys
import os
import markdown


def main():
    '''
    A script that converts a markdown to html
    Args:
        markdown_name(file): markdown file name
        output_file(file): output file name
    Return:
        None
    '''
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        exit(1)

    # Read the Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

    exit(0)

if __name__ == "__main__":
    main()
