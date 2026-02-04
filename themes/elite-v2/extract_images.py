import re
import json
import html

with open('temp_page.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON data-content
match = re.search(r'data-content="([^"]+)"', content)
if match:
    json_str = html.unescape(match.group(1))
    data = json.loads(json_str)
    
    # Extract image URLs
    images = []
    for item in data.get('items', []):
        # Prefer the 'img' src
        if 'img' in item and 'src' in item['img']:
            images.append(item['img']['src'])
    
    # Print the first 8 unique image URLs
    seen = set()
    count = 0
    for img in images:
        if img not in seen:
            print(img)
            seen.add(img)
            count += 1
            if count >= 8:
                break
else:
    print("No gallery data found")
