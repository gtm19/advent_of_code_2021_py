from tasks.day_001 import *

filepath = "lib/tests/data/test_day_001.txt"

def test_day_01_part_01():
  task = Day01(filepath)
  assert task.count_increases() == 7
