from utils import read_text, write_text
write_text("data.txt", "Hello from person3!")
text = read_text("data.txt")
print("Содержимое файла:", text)
