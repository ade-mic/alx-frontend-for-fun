#!/usr/bin/python3
"""
A Script that writes markdown to html
First argument is the name of the Markdown file
Second argument is the output file name
"""
import sys
import os
import markdown

'''
    A script that converts a markdown to html
    Args:
        markdown_name(file): markdown file name
        output_file(file): output file name
    Return:
        None
'''

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    markdown_name = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.exists(markdown_name):
        print(f'Missing {markdown_name}')
        exit(1)
    markdown.markdownFromFile(input=markdown_name, output=output_file)