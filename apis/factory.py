#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from importlib import import_module

from fastapi import FastAPI

# from apis.utils import get_config


def create_app():
    logger = logging.getLogger(__name__)

    app = FastAPI()

    # config = get_config()
    # services = config.get('services')
    services = ["items", "users", "home_page"]
    for service in services:
        try:
            service_module_name = "routers.{}".format(service)
            service_module = import_module(service_module_name)
            api_router = getattr(service_module, "router")
        except Exception as e:
            logger.exception("Failed to load Router {}!".format(service))
            logger.error(e)
        else:
            app.include_router(api_router)
    logger.info("Recommend projects application started")
    return app