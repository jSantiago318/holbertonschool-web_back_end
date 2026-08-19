# Pagination

Project on paginating a dataset with simple page numbers, hypermedia
metadata and deletion-resilient pagination.

## Learning objectives

- How to paginate a dataset with simple `page` and `page_size` parameters.
- How to paginate a dataset with hypermedia metadata.
- How to paginate in a deletion-resilient manner.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- All files end with a new line.
- The first line of all files is exactly `#!/usr/bin/env python3`.
- Code uses the `pycodestyle` style (version 2.5.x).
- All files are executable.
- All modules, classes and functions have documentation.
- All functions and coroutines are type-annotated.

## Files

| File | Description |
| ---- | ----------- |
| `0-simple_helper_function.py` | Function `index_range` that returns a tuple of the start and end indexes corresponding to the range of indexes to return for the given 1-indexed `page` and `page_size`. |
| `1-simple_pagination.py` | `Server` class with a `get_page` method that asserts its arguments are positive integers and returns the matching page of `Popular_Baby_Names.csv`, or an empty list when out of range. |
