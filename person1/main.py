from utils import read_text, write_text
write_text("data.txt", "Hello, GitHub!")
text = read_text("data.txt")
print("Содержимое файла:", text)
