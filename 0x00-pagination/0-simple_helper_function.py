#!/usr/bin/env python3
"""
Pagination indexing
"""


def index_range(page, page_size):
    """
    Creates pagination indexes
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)