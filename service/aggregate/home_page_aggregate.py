#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apis.dto import RecommendRequestDtO
from decorator.singleton import Singleton
from service.recall.i2i_recall import I2IRecall


@Singleton
class HomePageAggregateService:

    def __init__(self):
        self.i2i_recall_service = I2IRecall()

    def recommend(self, request_dto: RecommendRequestDtO):
        search_product_ids = request_dto.search_product_ids
        result = self.i2i_recall_service.recall(search_product_ids)
        return result
