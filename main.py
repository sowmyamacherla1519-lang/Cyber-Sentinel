import hashlib

filename = "monitored_file.txt"

with open(filename, "rb") as file:
    content = file.read()

file_hash = hashlib.sha256(content).hexdigest()

print("Cyber Sentinel Started")
print("File:", filename)
print("SHA-256 Hash:", file_hash)
