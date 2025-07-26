import json
import sys

with open('file_metadata.json', 'r', encoding='utf-8') as f:
    files = json.load(f)
if any(f['path'].lower() in ['preview.png', 'арт.png', 'art.png'] for f in files):
    print('true')
else:
    print('false')
