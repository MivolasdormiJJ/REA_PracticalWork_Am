
# Функции проекта
Функции работы с файлами находятся в `person1/utils.py`.
## write_text(filename, text)
Записывает текст в файл. Если файл существует,
его прежнее содержимое заменяется.
## read_text(filename)
Читает текст из файла и возвращает его содержимое.
## append_text(filename, text)
Добавляет текст в конец файла, сохраняя
существующее содержимое.
## Пример использования
```python
from utils import write_text, read_text, append_text
write_text("example.txt", "hello")
append_text("example.txt", ", world!")
print(read_text("example.txt"))
```

