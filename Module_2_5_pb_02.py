
#--------------------------
def sum_of_consecutive_odd_numbers(x, y):
  

  sum = 0
  i = min(x, y) + 1
  while i < max(x, y):
    if i % 2 == 1:
      sum += i
    i += 1
  return sum


def main():
  """
  The main function.
  """

  t = int(input())
  for _ in range(t):
    x, y = map(int, input().split())
    print(sum_of_consecutive_odd_numbers(x, y))


if __name__ == "__main__":
  main()
