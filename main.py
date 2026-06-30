from directory_scanner import DirectoryScanner
from file_hasher import FileHasher

scanner = DirectoryScanner()
hasher = FileHasher()

files = scanner.discover_files()

for file in files:
    file_hash = hasher.hash_file(file)
    print(file, file_hash)