## Advent of Code 2021: Python Edition

This repository contains the (basic) Python code I am writing to try to tackle the [2021 Advent of Code](https://adventofcode.com/2021), which I had got up to Day 15 on using Ruby.

### Solutions

These should be placed in [`lib/tasks`](lib/tasks), and will be named after the day of the task.

Similarly, the puzzle input should be placed as a text file in [`lib/tasks/data`](lib/tasks/data).

So, for example, on the 10th day of Christmas, you would need to create:

  - `lib/tasks/day_010.py`
  - `lib/tasks/data/day_010.txt`

### Tests

This project uses `pytest` to run tests using the tiny test inputs.

Similar to the teasks themselves, for tests (on day 10), the following files need to be created:

  - `lib/tests/test_day_010.py`
  - `lib/tests/data/test_day_010.txt`

## Makefile

All of these files can be initialised using GNU Make, as follows:

```
make init_010
```

In addition, the test for a given day is run like so:

```
make test_010
```

...and the actual task with the puzzle input, like so:

```
make task_010
```
