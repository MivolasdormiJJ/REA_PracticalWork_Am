
from utils import read_text, write_text, append_text
def test_write_text(tmp_path):
    file_path = tmp_path / "test.txt"
    write_text(file_path, "Hello GitHub!")
    assert file_path.read_text(encoding="utf-8") == "Hello GitHub!"

def test_read_text(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Python CI", encoding="utf-8")
    result = read_text(file_path)
    assert result == "Python CI"

def test_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    write_text(file_path, "")
    assert read_text(file_path) == ""

def test_unicode_text(tmp_path):
    file_path = tmp_path / "unicode.txt"
    write_text(file_path, "Привет, мир!")
    assert read_text(file_path) == "Привет, мир!"

def test_overwrite_file(tmp_path):
    file_path = tmp_path / "test.txt"
    write_text(file_path, "Old text")
    write_text(file_path, "New text")
    assert read_text(file_path) == "New text"

#тесты для новой функции
def test_append_text(tmp_path):
    file_path = tmp_path / "append.txt"
    write_text(file_path, "Hello")
    append_text(file_path, " World")
    assert read_text(file_path) == "Hello World"

def test_append_to_empty_file(tmp_path):
    file_path = tmp_path / "empty_append.txt"
    append_text(file_path, "New text")
    assert read_text(file_path) == "New text"
