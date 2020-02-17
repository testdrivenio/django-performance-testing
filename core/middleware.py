# core/middleware.py

import logging
import time

from django.db import connection, reset_queries


def metric_middleware(get_response):
    def middleware(request):
        reset_queries()

        # Get beginning stats
        start_queries = len(connection.queries)
        start_time = time.perf_counter()

        # Process the request
        response = get_response(request)

        # Get ending stats
        end_time = time.perf_counter()
        end_queries = len(connection.queries)

        # Calculate stats
        total_time = end_time - start_time
        total_queries = end_queries - start_queries

        # Log the results
        logger = logging.getLogger("debug")
        logger.debug(f"Request: {request.method} {request.path}")
        logger.debug(f"Number of Queries: {total_queries}")
        logger.debug(f"Total time: {(total_time):.2f}s")

        return response

    return middleware
