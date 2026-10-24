from pathlib import Path

# Main project directory (where this script is located)
BASE_DIR = Path(__file__).resolve().parent

# Project folders
PROJECT_DIR = BASE_DIR / "week-01-python-engineering" / "simple_agent"

folders = [
    PROJECT_DIR,
    PROJECT_DIR / "core",
    PROJECT_DIR / "tools",
]

# Project files
files = [
    PROJECT_DIR / "main.py",
    PROJECT_DIR / "core" / "__init__.py",
    PROJECT_DIR / "core" / "agent.py",
    PROJECT_DIR / "tools" / "__init__.py",
    PROJECT_DIR / "tools" / "calculator.py",
]

# Create folders
for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)
    print(f"Created folder: {folder}")

# Create empty files
for file in files:
    file.touch(exist_ok=True)
    print(f"Created file: {file}")

print("\nProject structure created successfully!")
