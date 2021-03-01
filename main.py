# From a list of random numbers
# we want to add some together to get as close to 35 as possible
# if we can't get to 35 we will take closest (closest over?)

import itertools

numbers = [
  [0, 15.3],
  [1, 12.5], 
  [2, 25.3],
  [3, 2.9], 
  [4, 15.7],
  [5, 2.6],
  [6, 7.3]
]

results = []

def run():
  for i in range(1, len(numbers) + 1):
    combinations = itertools.combinations(numbers, i)
    for combination in combinations:
      total = 0
      keys = []
      for item in combination:
        total = total + item[1]
        keys.append(item[0])
      print("Keys: " + str(keys) + " total: " + str(total))    
      results.append([keys, total])


if __name__ == "__main__":
  print("Running")
  run()
  print(len(results))
