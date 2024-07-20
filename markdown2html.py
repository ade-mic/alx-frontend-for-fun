#!/usr/bin/python3
'''
A Script that writes markdown to html
'''
import sys
import os
import markdown

def markdown2html(markdown_name, output_file):
    '''
    A script that converts a markdown to html
    Args:
        markdown_name(file): markdown file name
        output_file(file): output file name
    Return:
        None
    '''
    if not os.path.exists(markdown_name):
        print(f'Missing {markdown_name}')
        exit(1)
    markdown.markdownFromFile(input=markdown_name, output=output_file)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    markdown_name = sys.argv[1]
    output_file = sys.argv[2]
    markdown2html(markdown_name, output_file)