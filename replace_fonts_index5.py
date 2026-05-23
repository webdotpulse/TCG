import re

with open('index5.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Dosis:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'
)
content = content.replace("font-family: 'Inter', sans-serif;", "font-family: 'Dosis', sans-serif;")

with open('index5.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index5.html")
