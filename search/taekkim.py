import timeit

def ttoboki():
		n, m = map(int, input().split())
		d = sorted(map(int, input().split()), reverse=True)
		i = 0
		d_max = d[i]
		while d_max > 0:
				d_sum = 0
				for x in d:
						if x > d_max:
								d_sum += x - d_max
								print(x, d_sum)
						else:
								break
				if d_sum >= m:
						print(d_max)
						return d_max
				else:
						d_max -= 1

t1 = timeit.timeit('ttoboki()', setup='from __main__ import ttoboki')
print(t1)

