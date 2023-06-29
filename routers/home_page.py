#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from apis.dto import RecommendRequestDtO, RecommendResponseDto
from service.aggregate.home_page_aggregate import HomePageAggregateService

router = APIRouter(
    prefix="/home_page",
    tags=["home_page"]
)

home_page_aggregate = HomePageAggregateService()


@router.post("/feed")
async def feed(request_dto: RecommendRequestDtO):
    recommend_products = home_page_aggregate.recommend(request_dto)
    response = RecommendResponseDto(product_list=recommend_products)
    return response
