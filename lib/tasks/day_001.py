from grp import struct_group


import sys

class Day01:
  def __init__(self, filepath = "") -> None:
    if not filepath:
      self.filepath = sys.argv[1]
    else:
      self.filepath = filepath
    self.input = self.__parse_input(filepath)
    
  def __parse_input(self, filepath: str):
    str_input = open(self.filepath, "r").read().split()
    return [int(x) for x in str_input]
  
  def count_increases(self):
    increases = 0
    last_num = self.input[0]
    for num in self.input[1:]:
      if num > last_num:
        increases += 1
      last_num = num
    print(f"The depth increases {increases} time(s)")
    return increases

if __name__ == "__main__":
  print("DAY 01: PART 1  ++++++++++++")
  task = Day01()
  task.count_increases()
  print("++++++++++++++++++++++++++++")
