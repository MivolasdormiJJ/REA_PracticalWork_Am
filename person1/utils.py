def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
def read_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
#новая функция
def append_text(filename, text):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)


# Updated by person1
