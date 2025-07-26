import json
import sys

with open('file_metadata.json', 'r', encoding='utf-8') as f:
    files = json.load(f)
if all(f['path'].lower().endswith(('.png', '.pdn')) for f in files if f['path'].lower() not in ['preview.png', 'арт.png', 'art.png']):
    print('true')
else:
    print('false')
