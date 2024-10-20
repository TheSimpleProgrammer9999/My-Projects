"""Plots"""

import matplotlib.pyplot as mat

cubes = [1, 8, 27, 64, 125, 216, 243, 512]
squares = [1, 4, 9, 16, 25, 36, 49, 64]
tesseracts = [1, 16, 81, 256, 625, 1296, 2401, 4096]  # a.k.a 'to the 4th power'. Oh, and by the way, I made up the name tesseracts.
hyperhypercubes = [1, 32, 243, 1024, 3125, 7776, 16807, 32768] # a.k.a 'to the 5th power'. Oh, and by the way, I also made up the name hyperhypercube.
names = ["1", "2", "3", "4", "5", "6", "7", "8"]

mat.subplot(221)
mat.bar(names, cubes)
mat.subplot(222)
mat.scatter(names, squares)
mat.subplot(223)
mat.plot(names, tesseracts)
mat.subplot(224)
mat.barh(names, hyperhypercubes)
mat.show()