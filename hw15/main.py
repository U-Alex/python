import logging
import os
from sys import argv
import dir_tree2 as dt

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger_handler = logging.FileHandler(os.path.join(os.path.dirname(argv[0]), 'logging.log'), encoding='utf-8')
    logger_formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)
    logger.info('запуск построения списка')

    if len(argv) > 1:
        dt.analyse_dir(logger, os.path.abspath(argv[1]))
    else:
        dt.analyse_dir(logger, os.path.split(argv[0])[0])
