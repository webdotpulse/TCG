import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try regex matching to catch variations
    new_content = re.sub(
        r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*"\s+rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Dosis:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">',
        content
    )

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file} using regex")
