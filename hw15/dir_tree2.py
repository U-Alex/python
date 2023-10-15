"""
📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
📌Соберите информацию о содержимом в виде объектов namedtuple.
📌Каждый объект хранит: ○ имя файла без расширения или название каталога,
                        ○ расширение, если это файл,
                        ○ флаг каталога,
                        ○ название родительского каталога.
📌В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import os
from collections import namedtuple


def _run(path: str, result, path_parr: str = ''):
    addr, dirs, files = next(os.walk(path))
    f_cnt = len(files)
    f_size = 0
    for idx in range(len(dirs)):
        res = _run(os.path.join(addr, dirs[idx]), result, path)
        dirs[idx] = {'name': dirs[idx], 'f_cnt': res[0], 'f_size': res[1]}
        f_cnt += res[0]
        f_size += res[1]
    for idx in range(len(files)):
        f_path = os.path.join(addr, files[idx])
        f_size_ = os.path.getsize(f_path)
        files[idx] = {'name': files[idx], 'f_size': f_size_}
        f_size += f_size_
    dct = {'current_dir': {'parent': os.path.split(path_parr)[1],
                           'name': os.path.split(addr)[1],
                           'f_cnt': f_cnt,
                           'f_size': f_size},
           'inside_dirs': dirs,
           'inside_files': files
           }
    result.append(dct)
    return f_cnt, f_size


def analyse_dir(logger, path: str):
    result = []
    _, _ = _run(path, result)
    result.reverse()

    rows = [['type', 'parent', 'name', 'count', 'size']]
    for dct in result:
        rows.append(['DIR',
                     dct['current_dir']['parent'],
                     dct['current_dir']['name'],
                     dct['current_dir']['f_cnt'],
                     dct['current_dir']['f_size']])
        for fl in dct['inside_files']:
            rows.append(['File',
                         dct['current_dir']['name'],
                         fl['name'],
                         '',
                         fl['f_size']])

    result = []
    Data = namedtuple('Data', rows[0])

    for num, ob in enumerate(rows):
        if num:
            entry = Data(*ob)
            result.append(entry)
            logger.info(entry)

    for ob in result:
        print(ob)

    return
