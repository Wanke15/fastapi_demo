#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from apis.dto import ProductItem
from decorator.singleton import Singleton


@Singleton
class I2IRecall(object):
    def __init__(self):
        pass

    def recall(self, base_products):
        return self.random_fake_products()

    @staticmethod
    def random_fake_products():
        idxs = [random.randint(0, 100) for _ in range(10)]
        return [ProductItem(id=f"pid_{i}", name=f"p_name_{i}") for i in idxs]
