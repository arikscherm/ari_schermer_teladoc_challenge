from main import teladoc_challenge
import unittest

class TestGetMovies(unittest.TestCase):

	#Testing get movie_titles_from_page() helper function
	def test_spiderman_one_page(self):
		self.assertTrue(all(titles in teladoc_challenge.get_movie_titles_from_page("spiderman",1) for titles in ['Italian Spiderman', 'Superman, Spiderman or Batman']))

	def test_unsorted_result(self):
		self.assertEqual(teladoc_challenge.get_movie_titles_from_page("Christmas Special",1), ['The Harry Connick Jr. Christmas Special', 'Bachelors Walk Christmas Special'])

	def test_empty_page(self):
		self.assertEqual(teladoc_challenge.get_movie_titles_from_page("Harry Potter",50), [])

	def test_empty_string(self):
		self.assertIn("Waterworld", teladoc_challenge.get_movie_titles_from_page("",1))



	#Testing get_movie_titles()
	def test_spiderman_all_pages(self):
		self.assertTrue(all(titles in teladoc_challenge.get_movie_titles("spiderman") for titles in ['Italian Spiderman','They Call Me Spiderman']))

	def test_sorted_result(self):
		self.assertEqual(teladoc_challenge.get_movie_titles("Christmas Special"), ['Bachelors Walk Christmas Special', 'The Harry Connick Jr. Christmas Special'])

	def test_single_result(self):
		self.assertEqual(teladoc_challenge.get_movie_titles("spiderman 5"), ["Spiderman 5"])

	def test_numerical_search_parameter(self):
		self.assertEqual(len(teladoc_challenge.get_movie_titles("2")), 47)

	def test_null_result(self):
		self.assertEqual(teladoc_challenge.get_movie_titles("this should not return any movies"), [])


if __name__ == '__main__':
    unittest.main()