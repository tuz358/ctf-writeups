import sys
sys.setrecursionlimit(int(sys.argv[1]))
def f(n):
	print n
	return n if n < 2 else f(n-2) + f(n-1)
print "SECCON{" + str(f(1))[:32] + "}"
