# SPDX-FileCopyrightText: (c) 2020 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import re


class NotAnArticleUrl(Exception):
    pass


def articleUrlToTitle(url: str) -> str:
    # Про адреса написано здесь
    # https://en.wikipedia.org/wiki/Help:URL

    import urllib.parse
    url = urllib.parse.unquote(url)

    m = re.search("(?<=/wiki/)[^/]+", url)
    if m:
        return m.group(0)
    raise NotAnArticleUrl()
