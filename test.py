import unittest
from JPGtoPNGconverter import main_function

class TestMain(unittest.TestCase):
	def test_convertion_current_dir(self):
		first_folder = "Pokedex"
		second_folder = "new"
		res = main_function(first_folder, second_folder)
		self.assertEqual(res, 0)

	def test_convertion_current_dir2(self):
		first_folder = "Pokedex/"
		second_folder = "new"
		res = main_function(first_folder, second_folder)
		self.assertEqual(res, 0)

	def test_convertion_current_dir3(self):
		first_folder = ""
		second_folder = "new"
		res = main_function(first_folder, second_folder)
		self.assertEqual(res, "Wrong name of folder")

	def test_convertion_current_dir4(self):
		first_folder = "Pokedex1"
		second_folder = "new"
		res = main_function(first_folder, second_folder)
		self.assertEqual(res, "First folder does not exist")

	def test_convertion_current_dir5(self):
		first_folder = "empty"
		second_folder = "new"
		res = main_function(first_folder, second_folder)
		self.assertEqual(res, "First folder must contain files")

	def test_convertion_current_dir6(self):
		first_folder = "other_files"
		second_folder = "new"
		res = main_function(first_folder, second_folder)
		self.assertEqual(res, "First folder must contain jpg files")

if __name__ == '__main__':
		unittest.main()	
		