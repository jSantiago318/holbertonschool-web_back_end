# Python - Async Comprehension

Project on asynchronous generators and comprehensions in Python.

## Learning objectives

- How to write an asynchronous generator.
- How to use async comprehensions.
- How to type-annotate generators.

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
| `0-async_generator.py` | Coroutine `async_generator` that loops 10 times, waits 1 second asynchronously and yields a random number between 0 and 10. |
| `1-async_comprehension.py` | Coroutine `async_comprehension` that collects 10 random numbers with an async comprehension over `async_generator`. |
