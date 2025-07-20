import json
import sys
import os

# Get project name and file metadata from command-line arguments
project_name = sys.argv[1] if len(sys.argv) > 1 else "default_project"
file_metadata = json.loads(sys.argv[2]) if len(sys.argv) > 2 else []

# Define project metadata
project = {
    "name": project_name,
    "preview": {
        "path": "preview.png",
        "size_mb": 0,
        "download_url": f"https://raw.githubusercontent.com/Endermanik13/AurumBotFiles/main/{project_name}/preview.png"
    },
    "paint_files": [],
    "other_files": [],
    "final_files": file_metadata
}

# Write to project.json
with open(f"{project_name}/project.json", "w") as f:
    json.dump(project, f, indent=4)
