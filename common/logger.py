#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path
import logging


def get_logger(name, log_file=None, log_level='DEBUG'):
    """
    logger
    :param name: 模块名称
    :param log_file: 日志文件，如无则输出到标准输出
    :param log_level: 日志级别
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level.upper())
    formatter = logging.Formatter(
        '[%(levelname)s\t%(process)d\t%(thread)d\t%(threadName)s\t%(asctime)s\t%(module)s\t%(lineno)d]\t%(message)s')
    if log_file:
        f_handle = logging.FileHandler(log_file)
        f_handle.setFormatter(formatter)
        logger.addHandler(f_handle)
    handle = logging.StreamHandler()
    handle.setFormatter(formatter)
    logger.addHandler(handle)
    return logger


if sys.platform == "darwin":
    LOG_FILE = '/tmp/app.log'
    level = 'DEBUG'
else:
    LOG_FILE = '/logs/app.log'
    if not os.path.exists(LOG_FILE):
        Path(os.path.dirname(LOG_FILE)).mkdir(exist_ok=True)
    # 这个可以通过类似Apollo配置，在不同的环境配置不同的日志级别
    level = 'INFO'

logger = get_logger(__name__, log_file=LOG_FILE, log_level=level)


def set_log_level(log_level='DEBUG'):
    logger.setLevel(log_level.upper())


if __name__ == '__main__':
    logger.debug('hi')
    logger.info('hi')
    logger.error('hi')
    logger.warning('hi')
    set_log_level('info')
    logger.debug('hi')
    logger.info('hi')
    logger.error('hi')
    logger.warning('hi')
