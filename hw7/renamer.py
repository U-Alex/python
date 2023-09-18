""" Напишите функцию группового переименования файлов. Она должна:
    принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    принимать параметр количество цифр в порядковом номере.
    принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
    принимать параметр расширение конечного файла.
    принимать диапазон сохраняемого оригинального имени.
        Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
        К ним прибавляется желаемое конечное имя, если оно передано.
        Далее счётчик файлов и расширение.
    Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

from pathlib import Path


def mass_rename(*, dir_path='', final_name, len_count=4, source_ext, final_ext, old_letters=None):
    """
    :param dir_path: путь в каталог с файлами, возможен относительный и абсолютный, по умолчанию пустая строка (текущая директория)
    :param final_name: желаемое конечное имя, по умолчанию пустая строка
    :param len_count: количество цифр в порядковом номере, по умолчанию 4
    :param source_ext: расширение исходного файла, возможно указание "*" (все) или пустая строка (без расширения)
    :param final_ext: расширение конечного файла, возможно указание пустой строки (без расширения)
    :param old_letters: диапазон сохраняемого оригинального имени [start, stop], по умолчанию None
    """
    cnt = 0
    target_path = Path(Path.cwd() / dir_path)
    for obj in target_path.iterdir():
        t_name = list(obj.parts).pop().rsplit('.', 1)
        if len(t_name) < 2:
            t_name.append('')
        if source_ext == '*' or source_ext == t_name[1]:
            t_name[1] = final_ext
            t_name[0] = t_name[0][old_letters[0] - 1: old_letters[1]:] if old_letters else ''
            t_cnt = '_' + ('0' * len_count + str(cnt))[-len_count::]
            t_name[0] += final_name + t_cnt
            cnt += 1
            t_name = '.'.join(t_name).rstrip('.')
            obj.rename(target_path / t_name)
            #print(t_name)


if __name__ == '__main__':
    mass_rename(dir_path='files', final_name='_new', len_count=3, source_ext='py', final_ext='tmp', old_letters=[1, 4])
    #mass_rename(dir_path='files', final_name='new', len_count=4, source_ext='py', final_ext='tmp')
    print(mass_rename.__doc__)
