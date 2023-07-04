#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from apis.dto import RecommendRequestDtO, RecommendResponseDto
from service.aggregate.home_page_aggregate import HomePageAggregateService

router = APIRouter(
    prefix="/search_page",
    tags=["search_page"]
)

home_page_aggregate = HomePageAggregateService()


@router.post("/recommend")
async def recommend(request_dto: RecommendRequestDtO):
    recommend_products = home_page_aggregate.recommend(request_dto)
    response = RecommendResponseDto(product_list=recommend_products)
    return response
