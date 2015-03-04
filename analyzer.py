import datareader
import sys
import numpy
import scipy.stats
import itertools
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time

pdf = PdfPages("report.pdf")

				
def showLstSqr(data1, data2, corrcoef):

	x = numpy.array(data1[1])
	y = numpy.array(data2[1])
	polynomialDegree = 1

	corrcoef = round(corrcoef,2)

	rSquared = corrcoef*corrcoef
	rSquared = round(rSquared,2)


	if rSquared <= 0.50:
		polynomialDegree = 3
	elif rSquared <= 0.75:
		polynomialDegree = 2
	else:
		polynomialDegree = 1


	print("Attributes  : ", data1[0], data2[0])
	print("RSquared    : ", rSquared)
	print("Poly Degree : ", polynomialDegree)


	fig = plt.figure()
	plt.gca().set_position((.1, .5, .8, .4))
	statx = scipy.stats.describe(x)
	#minx = statx[1][0]
	#miny = statx[1][1]

	#statx = (round(statx[0],2), round(statx[1],2), round(statx[2],2), round(statx[3],2))

	stx = numpy.std(x)
	stx = round(stx,1)


	sty = numpy.std(y)
	sty = round(sty,1)

	staty = scipy.stats.describe(y)

	plt.figtext(.02, .02, 'Correlation Coefficient is \'%s\' '\
			'and R2 is \'%s\'\n\n' \
			'The observations of \'%s\' are \'%s\' \n' \
			'The min and max are \'%s\' \'%s\' \n' \
			'The Arithmetic mean is \'%.2f\'\n'\
			'The variance is \'%.2f\'\n'\
			'The standard deviation is \'%.2f\' \n \n'\
			'The observations of \'%s\'  are  \'%s\'\n'\
			'The min and max are \'%s\' \'%s\' \n'\
			'The Arithmetic mean is \'%.2f\'\n'\
			'The variance is \'%.2f\'\n'\
			'The standard deviation is \'%.2f\'   '%(corrcoef, rSquared, data1[0], statx[0], statx[1][0], statx[1][1], statx[2], statx[3], stx, data2[0], staty[0], staty[1][0], staty[1][1], staty[2], staty[3], sty))
	
	if polynomialDegree == 1:
		plt.xlabel(data1[0])
		plt.ylabel(data2[0])

		#find least squares equation
		A = numpy.vstack([x, numpy.ones(len(x))]).T
		m, c = numpy.linalg.lstsq(A, y)[0]

		plt.plot(x, y, 'o', label='Original Data')
		plt.plot(x, m*x + c, 'r', label='R^2 line (r = %s)'%(corrcoef))
		
		plt.legend(loc='best')
	else:
		
		plt.title(data1[0]+data2[0])
		
		corrpol= numpy.polyfit(x, y, polynomialDegree)
		poly = numpy.poly1d(corrpol)		
		startXPoint = statx[1][0]
		maxXPoints = statx[1][1]
		xpoints = numpy.linspace(0.0, maxXPoints)
		

		plt.plot(x, y, 'x', xpoints, poly(xpoints), '-')

	pdf.savefig(fig)
	print("---")


if __name__ == '__main__':
	
	start = int(round(time.time() * 1000))
	files = {}

	for filename in sys.argv[1:]:
		data = datareader.DataReader(filename)
		files[data.getBasename()] = data


	helper = {}
	for fileno, filename in enumerate(files.keys()):
		for attribute in files[filename].get_numerical_attributes():
			helper[str(fileno)+"."+str(attribute['position'])] = (filename, attribute['attr_name'])


	for combination in list(itertools.combinations(helper.keys(), 2)):

		filename1, attr1 = helper[combination[0]]
		filename2, attr2 = helper[combination[1]]

		data1 = files[filename1].getData(attr1)
		data2 = files[filename2].getData(attr2)

		corrcoef = numpy.corrcoef(data2, data1)[0][1]
		if abs(corrcoef) >= 0.5:
			showLstSqr( (str(helper[combination[0]]), data1 ), ( str(helper[combination[1]]), data2), corrcoef)
		else:
			print("Low correlation coefficient for %s and %s" %(str(helper[combination[0]]), str(helper[combination[1]])))

	pdf.close()
	end = int(round(time.time() * 1000))
	print("Finished in ", (end-start), "ms")
