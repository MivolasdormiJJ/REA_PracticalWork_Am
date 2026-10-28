from utils import read_text, write_text
write_text("data.txt", "Data updated by person1 and person3!")
text = read_text("data.txt")
print("Содержимое файла:", text)
