"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc
"""


def str_to_file(str_line, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(str_line)
    return


def file_to_str(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        str_line = file.read()
    return str_line


def rle_encode(line):
    enc_line = ''
    curr = line[0]
    cnt = 1
    if curr.isdigit():
        raise ValueError('строка содержит цифры')
    for i in range(1, len(line)):
        if (line[i] == curr) and cnt < 9:
            cnt += 1
        else:
            enc_line += str(cnt) + curr
            curr = line[i]
            cnt = 1
    else:
        enc_line += str(cnt) + curr

    return enc_line


def rle_decode(line):
    dec_line = ''
    for i in range(0, len(line)):
        if line[i].isdigit():
            dec_line += line[i + 1] * int(line[i])

    return dec_line


if __name__ == '__main__':
    st_str = input('enter string to compress: ')
    print(f'string: {st_str}')
    enc_line = rle_encode(st_str)
    print(f'encoded in: {enc_line}')
    str_to_file(enc_line, 'file_encode.txt')
    print(f'saved in: file_encode.txt')
    enc_line = file_to_str('file_encode.txt')
    print(f'read from: file_encode.txt')
    dec_line = rle_decode(enc_line)
    print(f'decoded in: {dec_line}')
    str_to_file(dec_line, 'file_decode.txt')
    print(f'saved in: file_decode.txt')
