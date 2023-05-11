import time


def print_curs(text: str) -> None:
    """
    Печать текста в консоль (имитация машинного ввода)
    :return: None
    """
    text_list = text.split('\n')
    for each in text_list:
        if each != "":
            index = 0
            while len(each) > index:
                temp = each[:index]
                print(f'{temp}_', end="\r")
                time.sleep(0.1)
                index += 5
            print(each)
