from pathlib import Path
new_dir = Path.home() / "new_directory"
new_dir.mkdir()

new_dir.exists()