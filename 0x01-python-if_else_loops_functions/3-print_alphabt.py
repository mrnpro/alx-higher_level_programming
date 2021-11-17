#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i is 101 or i is 113:
	continue
    else:
	print("{:c}".format(i), end="")
