#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional, List

from pydantic import BaseModel


class ProductItem(BaseModel):
    id: str
    name: str


class RecommendRequestDtO(BaseModel):
    user_id: str
    store_id: str
    scene_id: str

    # 搜索场景特有参数
    query: str
    search_product_ids: Optional[List[str]] = []

    # 购物车场景特有参数
    cart_product_ids: Optional[List[str]] = []


class RecommendResponseDto(BaseModel):
    product_list: List[ProductItem]
