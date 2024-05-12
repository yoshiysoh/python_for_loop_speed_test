import sys
import timeit

version = sys.version


def test():
    r = 0
    for i in range(int(1e5)):
        r += i


repeat = 10
result = timeit.timeit("test()", globals=globals(), number=repeat)
result /= repeat

with open("for_loop_result.txt", "a") as f:
    f.write(str(version)[:6] + "\n" + str(result) + "\n")
