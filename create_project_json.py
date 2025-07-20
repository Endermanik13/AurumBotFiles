import json
import sys

# Get project name from command-line argument
project_name = sys.argv[1] if len(sys.argv) > 1 else "default_project"

# Define project metadata
project = {
    "name": project_name,
    "preview": {
        "path": "preview.png",
        "size_mb": 0,
        "download_url": f"https://raw.githubusercontent.com/Endermanik13/AurumBotFiles/main/{project_name}/preview.png"
    },
    "paint_files": [],
    "other_files": []
}

# Write to project.json
with open(f"{project_name}/project.json", "w") as f:
    json.dump(project, f, indent=4)
