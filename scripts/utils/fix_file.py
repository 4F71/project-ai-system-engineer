import re

# Read the corrupted file
with open('docs/project_roadmap.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix line breaks that were removed
# Add line breaks before common patterns
patterns_to_fix = [
    (r'(\w)\*\*([A-ZÇÖÜĞİŞ])', r'\1\n\n**\2'),  # Before **Capital letter
    (r'(\w)(\d+\.\s+[A-ZÇÖÜĞİŞ])', r'\1\n\n\2'),  # Before numbered lists  
    (r'(```)(\w)', r'\1\n\n\2'),  # After code blocks
    (r'(\w)(###\s+)', r'\1\n\n\2'),  # Before ### headers
    (r'(\w)(##\s+[^#])', r'\1\n\n\2'),  # Before ## headers (but not ###)
    (r'(\.)(\*\*[A-ZÇÖÜĞİŞ])', r'\1\n\n\2'),  # After period before **Capital
    (r'(```)([^`])', r'\1\n\n\2'),  # After closing ```
    (r'(\w)(---)', r'\1\n\n\2'),  # Before ---
    (r'(---)(\w)', r'\1\n\n\2'),  # After ---
    (r'(\*\*)\s*(\w+:)\*\*(\d)', r'**\2**\n\n\3'),  # Fix **Text:**Number
    (r'(\w)(\*\*[A-ZÇÖÜĞİŞ][^*]*:\*\*)', r'\1\n\n\2'),  # Before **Text:**
]

for pattern, replacement in patterns_to_fix:
    content = re.sub(pattern, replacement, content)

# Clean up excessive newlines (more than 2)
content = re.sub(r'\n{4,}', '\n\n', content)

# Write the fixed content
with open('docs/project_roadmap.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Dosya düzeltildi!")
