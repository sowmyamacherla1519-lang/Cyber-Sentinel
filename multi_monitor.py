import hashlib

files = ["file1.txt", "file2.txt", "file3.txt"]

for filename in files:
    with open(filename, "rb") as file:
        content = file.read()

    file_hash = hashlib.sha256(content).hexdigest()

    print(f"{filename}")
    print(f"Hash: {file_hash}")
    print("-" * 50)
