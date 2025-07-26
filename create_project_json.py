import json
import sys
import os

# Проверка аргументов
if len(sys.argv) < 3:
    print("Ошибка: недостаточно аргументов. Укажите project_name и file_metadata")
    sys.exit(1)

project_name = sys.argv[1]
try:
    file_metadata = json.loads(sys.argv[2])
except json.JSONDecodeError as e:
    print(f"Ошибка: неверный формат file_metadata: {e}")
    sys.exit(1)

# Проверка корректности file_metadata
if not isinstance(file_metadata, list):
    print("Ошибка: file_metadata должен быть списком")
    sys.exit(1)

# Проверка наличия preview.png, арт.png или art.png
preview_exists = any(f['path'].lower() in ['preview.png', 'арт.png', 'art.png'] for f in file_metadata)
if not preview_exists:
    print("Ошибка: preview.png, арт.png или art.png не предоставлен")
    sys.exit(1)

# Поиск имени файла превью
preview_file = next(f for f in file_metadata if f['path'].lower() in ['preview.png', 'арт.png', 'art.png'])

# Формирование метаданных проекта
project = {
    "name": project_name,
    "preview": {
        "path": preview_file["path"],
        "size_mb": preview_file["size_mb"],
        "download_url": f"https://raw.githubusercontent.com/Endermanik13/AurumBotFiles/main/{project_name}/{preview_file['path']}"
    },
    "paint_files": [f for f in file_metadata if f["path"].lower().endswith(('.png', '.pdn')) and f["path"].lower() not in ['preview.png', 'арт.png', 'art.png']],
    "other_files": [f for f in file_metadata if not f["path"].lower().endswith(('.png', '.pdn'))],
    "final_files": file_metadata
}

# Сохранение в projects/
os.makedirs("projects", exist_ok=True)
with open(f"projects/{project_name}.json", "w", encoding="utf-8") as f:
    json.dump(project, f, indent=4, ensure_ascii=False)
