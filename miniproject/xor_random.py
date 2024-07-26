from time import thread_time_ns, time_ns
from sys import maxsize


def xorshift128plus():
	s0 = thread_time_ns()
	s1 = time_ns()

	def _random():
		nonlocal s0, s1
		x, y = s0, s1
		x = x ^ ((x << 23) & 0xFFFFFFFFFFFFFFFF)  # 64bit
		x = (x ^ (x >> 17)) ^ (y ^ (y >> 26))
		s0, s1 = y, x
		return s0 + s1

	return _random


def main():
	r = xorshift128plus()

	for i in range(10):
		print((r() % maxsize)/maxsize)


if __name__ == '__main__':
	main()
