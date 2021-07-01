# SPDX-FileCopyrightText: (c) 2020 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import json
import urllib.parse
import warnings
from typing import *

import requests

# https://en.wikipedia.org/w/index.php?title=Gregorio_Castaneda&action=edit&redlink=1
from rcd_wikipedia.urls import articleUrlToTitle


def session_get(session: Optional[requests.Session],
                *args, **kwargs) -> requests.Response:
    close = False
    if session is None:
        close = True
        session = requests.Session()
    try:
        return session.get(*args, **kwargs)
    finally:
        if close:
            session.close()


def article_url_to_wikidata_id(url: str,
                               session: requests.Session = None) \
        -> Optional[str]:
    host = urllib.parse.urlparse(url).netloc
    title = articleUrlToTitle(url)

    query = f"https://{host}/w/api.php?action=query" \
            f"&prop=pageprops&titles={title}&format=json"
    json_code = session_get(session, url=query).text

    # json_code = rcd.just.getData(query, text=True, cacheSec=cache_sec,
    #                             beforeDownloadFunc=lambda: time.sleep(1 / 3))

    pages = json.loads(json_code)["query"]["pages"]
    firstPage = next(iter(pages.values()))
    # print(firstPage)
    return firstPage["pageprops"]["wikibase_item"]


# 135/636 https://en.wikipedia.org/w/index.php?title=Gregorio_Castaneda&action=edit&redlink=1-> Q395712

# https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&titles=Kofoworola_Abeni_Pratt&format=json


def articleUrlToWikidataId(*args, **kwargs):
    warnings.warn("Obsolete", DeprecationWarning)
    return article_url_to_wikidata_id(*args, **kwargs)


if __name__ == "__main__":
    pass
