import time


def print_curs(text: str) -> None:
    """
    Печать текста в консоль
    :return: None
    """
    index = 0
    while len(text) > index:
        temp = text[:index]
        print(f'{temp}_', end="\r")
        time.sleep(0.2)
        index += 1
