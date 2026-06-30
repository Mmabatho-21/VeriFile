from pathlib import Path

class DirectoryScanner:

    def discover_files(self):
        directory = Path.cwd()

        files = []

        for item in directory.rglob("*"):
            if item.is_file():
                file_info = {
                    "Path":str(item),
                    "Name": item.name,
                    "Size": item.stat().st_size,
                    "Modified_Time": item.stat().st_mtime,
                }

                files.append(file_info)

        return files

