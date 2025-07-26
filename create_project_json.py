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

# Проверка наличия preview.png
preview_exists = any(f['path'].lower() == 'preview.png' for f in file_metadata)
if not preview_exists:
    print("Ошибка: preview.png не предоставлен")
    sys.exit(1)

# Формирование метаданных проекта
project = {
    "name": project_name,
    "preview": {
        "path": "preview.png",
        "size_mb": next((f["size_mb"] for f in file_metadata if f["path"].lower() == "preview.png"), 0),
        "download_url": f"https://raw.githubusercontent.com/Endermanik13/AurumBotFiles/main/{project_name}/preview.png"
    },
    "paint_files": [f for f in file_metadata if f["path"].lower().endswith(('.png', '.pdn')) and f["path"].lower() != "preview.png"],
    "other_files": [f for f in file_metadata if not f["path"].lower().endswith(('.png', '.pdn'))],
    "final_files": file_metadata
}

# Сохранение в projects/
os.makedirs("projects", exist_ok=True)
with open(f"projects/{project_name}.json", "w", encoding="utf-8") as f:
    json.dump(project, f, indent=4, ensure_ascii=False)
