def fib(n):
  """
  Returns the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number.

  Returns:
    The nth Fibonacci number.
  """

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)


def main():
  """
  The main function.
  """

  n = int(input())
  for i in range(n):
    print(fib(i))


if __name__ == "__main__":
  main()

