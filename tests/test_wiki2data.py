import unittest

from rcd_wikipedia.pedia_to_data import article_url_to_wikidata_id
from rcd_wikipedia.urls import NotAnArticleUrl


class TestWikipedia(unittest.TestCase):
    def test_to_wikidataId(self):
        # васнецов
        self.assertEqual(
            article_url_to_wikidata_id(
                "https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D1%81%D0%BD%D0%B5"
                "%D1%86%D0%BE%D0%B2,_%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80_%D0"
                "%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87"),
            "Q204138")

        self.assertEqual(
            article_url_to_wikidata_id("https://en.wikipedia.org/wiki/Albert_"
                                       "R%C3%A0fols-Casamada"),
            "Q2607849")

        with self.assertRaises(NotAnArticleUrl):
            article_url_to_wikidata_id(
                'https://en.wikipedia.org/w/index.php'
                '?title=Gregorio_Castaneda&action=edit&redlink=1'),

    # этого почему-то нет в Wikidata (2019)
# articleUrlToWikidataId("https://en.wikipedia.org/wiki/Bernardo_Martorell")
