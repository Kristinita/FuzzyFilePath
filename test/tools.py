import inspect

"""
	Inherit from TestCase to run tests receiving argument `ViewHelper`
	Convention: for a test to be executed/recognized its name must contains "should"
"""
class TestCase:
	def __init__(self, name):
		self.name = name
		self.tests = self.get_tests()
		self.length = len(self.tests)

	def get_tests(self):
		tests = []
		methods = inspect.getmembers(self, predicate=inspect.ismethod)
		for name, descr in methods:
			if "should" in name:
				tests.append(name)
		return tests