# Python - Async

Project on asynchronous programming with `async`/`await` and `asyncio`.

## Learning objectives

- How to write an `async` syntax coroutine.
- How to execute an async program with `asyncio`.
- How to run concurrent coroutines.
- How to create `asyncio` tasks.
- How to use the `random` module.

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8).
- All files end with a new line.
- The first line of all files is exactly `#!/usr/bin/env python3`.
- Code uses the `pycodestyle` style (version 2.5.x).
- All files are executable.
- All modules, classes and functions have documentation.
- All functions and coroutines are type-annotated.

## Files

| File | Description |
| ---- | ----------- |
| `0-basic_async_syntax.py` | Coroutine `wait_random` that waits a random delay between 0 and `max_delay` (default 10) seconds and returns it. |
| `1-concurrent_coroutines.py` | Coroutine `wait_n` that spawns `wait_random` n times and returns the delays in ascending order without calling `sort()`. |
