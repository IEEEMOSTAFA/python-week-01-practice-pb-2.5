
#-----------------
def equation(x, n):
  """
  Returns the value of the equation S.

  Args:
    x: The base of the equation.
    n: The exponent of the equation.

  Returns:
    The value of the equation S.
  """

  sum = 0
  for i in range(n + 1):
    exponent = 2 * i
    if exponent <= n:
      sum += x ** exponent
  return sum - 1


def main():
  """
  The main function.
  """

  x, n = map(int, input().split())
  print(equation(x, n))


if __name__ == "__main__":
  main()
