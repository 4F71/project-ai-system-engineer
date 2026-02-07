import re

# Read the file
with open('docs/project_roadmap.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Comprehensive emoji pattern
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002500-\U00002BEF"  # chinese char
    "\U00002702-\U000027B0"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001f926-\U0001f937"
    "\U00010000-\U0010ffff"
    "\u2640-\u2642"
    "\u2600-\u2B55"
    "\u200d"
    "\u23cf"
    "\u23e9"
    "\u231a"
    "\ufe0f"  # dingbats
    "\u3030"
    "]+",
    flags=re.UNICODE
)

# Remove emojis
content_no_emoji = emoji_pattern.sub('', content)

# Clean up extra spaces that might be left behind
# But preserve line structure
lines = content_no_emoji.split('\n')
cleaned_lines = []
for line in lines:
    # Remove multiple spaces (but keep indentation)
    line = re.sub(r'([^\s])\s{2,}', r'\1 ', line)
    # Fix "** text:**" to "**text:**"
    line = re.sub(r'\*\*\s+([^*]+):', r'**\1:', line)
    cleaned_lines.append(line)

content_final = '\n'.join(cleaned_lines)

# Write back
with open('docs/project_roadmap.md', 'w', encoding='utf-8') as f:
    f.write(content_final)

print("Emojiler başarıyla silindi!")
