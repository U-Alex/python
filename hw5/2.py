""" ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def path_parse(path: str):
    *s1, s2 = path.split('/')
    return f"{'/'.join(s1)}/", *s2.rsplit('.', 1)


def path_parse2(path: str):
    s1 = path.rsplit('/', 1)
    return f"{s1[0]}/", *s1[1].rsplit('.', 1)


print(path_parse('/mnt/work/video_admin/_GB/Погружение в Python/Урок.5.mp4'))
print(path_parse2('/mnt/work/video_admin/_GB/Погружение в Python/Урок.5.mp4'))
