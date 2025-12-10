# repo_txt
# Version 1

def open_file():
    with open(".\\wörter.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()
    return lines
