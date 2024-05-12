import timeit
import sys

version = sys.version

def test():
    r = 0
    for i in range(int(1e8)):
        r += i

repeat = 1
result = timeit.timeit('test()', globals=globals(), number=repeat)
result /= repeat

with open('for_loop_result.tsv', 'a') as f:
    f.write(str(version)[:6] + '\n' + str(result) + '\n')