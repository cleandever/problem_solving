def solution(n):
    n_str = sorted(str(n), reverse=True)
    return int(''.join(n_str))


assert solution(118372) == 873211
assert solution(111222333) == 333222111
assert solution(1) == 1
assert solution(8000000000) == 8000000000
assert solution(101010) == 111000

