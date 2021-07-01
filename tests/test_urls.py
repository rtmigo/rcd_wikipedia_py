# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest

from rcd_wikipedia.urls import articleUrlToTitle, NotAnArticleUrl


class TestArticleUrlToTitle(unittest.TestCase):
    def test_to_title(self):
        src = "https://en.wikipedia.org/wiki/Albert_R%C3%A0fols-Casamada"
        dst = articleUrlToTitle(src)
        self.assertEqual(dst, "Albert_Ràfols-Casamada")

        src = "https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D1%81%D0%BD%D0%B5%D1%86%D0%BE%D0%B2,_%D0%92%D0%B8%D0%BA%D1%82%D0%BE%D1%80_%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87"
        dst = articleUrlToTitle(src)
        self.assertEqual(dst, "Васнецов,_Виктор_Михайлович")

        src = "https://en.wikipedia.org/w/index.php?title=Gregorio_Castaneda&action=edit&redlink=1"
        with (self.assertRaises(NotAnArticleUrl)):
            articleUrlToTitle(src)