
def write_file(name: str, text: str) -> None:
    """Записывыаем результат в текстовый файл"""

    with open(name, mode="w") as file:
        file.write(text)

