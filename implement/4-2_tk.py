# 1시간에 3이
# 일의자리 3 -> 0 1 2 3 4 5 -> 6개
# 십의자리 3 -> 01 2 3 4 5 6 7 8 9 -> 10개
# 중복 -> 1개
# 1분 -> 15개

n = int(input())
cnt = 0
h, m, s = 0, 0, 0

def descriminate(n):
    return n // 10 == 3 or n % 10 == 3

while h < n + 1:
    s += 1
    if s >= 60:
        s = 0
        m += 1
        if m >= 60:
            m = 0
            h += 1
    if descriminate(h) | descriminate(m) | descriminate(s):
        cnt += 1
print(cnt)