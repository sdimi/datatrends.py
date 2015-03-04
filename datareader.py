import numpy
import csv
import sys
import os
import itertools

class DataReader(object):
	"""reads a csv file and for each attr saves data"""

	def __init__(self, filename, initCombinations=False):
		self.filename = filename

		with open(filename, 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			self.features = { item : {'position':position} for position, item in enumerate(next(reader)) }
			self.set_features_data(reader)
			self.set_features_types(apply_default_type=True)

		self.combinationInfo = {}
		if initCombinations:
			self.setUpCombinations()

	def getBasename(self):
		return os.path.basename(self.filename)[:self.filename.index('.')]

	def set_features_data(self, csv_reader):
		data = { item:[] for item in self.features.keys() }

		reverseDict = { self.features[headerName]['position'] : headerName for headerName in self.features.keys()}

		for row in csv_reader:
			for position, item in enumerate(row):
				data[reverseDict[position]].append(None if len(item) == 0 else item)

		for key, value in data.items():
			self.features[key]['attr_name'] = str(key)
			self.features[key]['data'] = value


	def set_features_types(self, default_type=float, apply_default_type=False):
		features_types = { item:None for item in self.features }

		for feature,value in self.features.items():

			self.features[feature]['type'] = default_type
			
			for position,item in enumerate(self.features[feature]['data']):
				if item is not None:
					try:
						if not apply_default_type:
							float(item)
						else:
							self.features[feature]['data'][position] = float(item)
					except ValueError:
						self.features[feature]['type'] = str
						break

	def get_numerical_attributes(self):
		return [ self.features[key] for key in self.features if self.features[key]['type'] is not str ]

	def setUpCombinations(self, r=2):
		self.combinations = list(itertools.combinations(self.get_numerical_attributes(), r))
		"""self.combinationInfo = {}

		for combination in combinations:
			metrics = {}
			metrics['corrcoef'] = numpy.corrcoef(self.features[combination[0]]['data'], self.features[combination[1]]['data'])
			
			self.combinationInfo[combination] = metrics
		"""

	def getAttributes(self):
		return list(self.features.keys())

	def getData(self, attr):
		return self.features[attr]['data']
