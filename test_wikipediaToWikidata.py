import unittest

from rcd_wikipedia.pedia_to_data import articleUrlToWikidataId


class TestWikipedia(unittest.TestCase):

	#def test_to_host(self):

	#	self.assertEqual(wkpArticleUrl_to_host("https://en.wikipedia.org/wiki/Albert_R%C3%A0fols-Casamada"),
	#					 "en.wikipedia.org")




	def test_to_wikidataId(self):

		# васнецов
		self.assertEqual(
			articleUrlToWikidataId("https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D1%81%D0%BD%D0%B5%D1%86%D0%BE%D0%B2,_%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80_%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87"),
			"Q204138")

		self.assertEqual(
			articleUrlToWikidataId("https://en.wikipedia.org/wiki/Albert_R%C3%A0fols-Casamada"),
			"Q2607849")

		# этого почему-то нет в Wikidata (2019)
		#articleUrlToWikidataId("https://en.wikipedia.org/wiki/Bernardo_Martorell")
