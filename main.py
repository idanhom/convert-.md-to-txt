import os
import re

def strip_markdown(md_text):
    # Remove Markdown syntax with simple regex rules
    text = re.sub(r'!\[.*?\]\(.*?\)', '', md_text)  # remove images
    text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', text)  # remove links but keep text
    text = re.sub(r'[#*>`]', '', text)  # remove common markdown chars
    text = re.sub(r'\s+', ' ', text)  # collapse whitespace
    return text.strip()

# Walk through all directories
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".md"):
            md_path = os.path.join(root, filename)
            txt_path = os.path.join(root, filename.replace(".md", ".txt"))

            with open(md_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
                plain_text = strip_markdown(md_content)

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(plain_text)

            print(f"Converted: {md_path} → {txt_path}")
