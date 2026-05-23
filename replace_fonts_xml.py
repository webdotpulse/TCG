import os
import glob

html_files = glob.glob('*.html')

old_font_link_xml = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet"/>'
new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Dosis:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_font_link_xml in content:
        content = content.replace(old_font_link_xml, new_font_link)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
