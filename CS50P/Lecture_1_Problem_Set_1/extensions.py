EXTENSIONS_DICT = {
    "gif": "image/gif", 
    "jpg": "image/jpeg", 
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

def main():
    fileName = input("File name: ").strip().lower()
    print(get_extension(fileName))

def get_extension(fileName):
    file_ex = fileName.split(".")[-1]
    if file_ex in EXTENSIONS_DICT:
        return EXTENSIONS_DICT[file_ex]
    else:
        return "application/octet-stream"

main()