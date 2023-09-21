""" Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
    Результаты обхода сохраните в файлы json, csv и pickle.
    Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория.
    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import json
import csv
import os
import pickle


def _run(path: str, result, path_parr: str = ''):
    addr, dirs, files = next(os.walk(path))
    # print('1-- ', addr, dirs, files, path_parr)
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


def analyse_dir(path: str):
    result = []
    _, _ = _run(path, result)
    result.reverse()

    with open('report.json', 'w', encoding='UTF-8') as f_json:
        json.dump(result, f_json, indent=4)

    with open('report.pickle', 'wb') as f_pickle:
        pickle.dump(result, f_pickle, protocol=pickle.DEFAULT_PROTOCOL)

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

    with open('report.csv', 'w', newline='', encoding='utf-8') as f_scv:
        csv_write = csv.writer(f_scv, dialect='excel')
        csv_write.writerows(rows)

    return


if __name__ == '__main__':
    analyse_dir('files')


