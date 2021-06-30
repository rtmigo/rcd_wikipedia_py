import json
import time
import urllib.parse
import warnings
from typing import *

import rcd.just

# https://en.wikipedia.org/w/index.php?title=Gregorio_Castaneda&action=edit&redlink=1
from rcd_wikipedia.urls import articleUrlToTitle


def article_url_to_wikidata_id(url: str, cache_sec=60 * 60 * 24) \
		-> Optional[str]:


    host = urllib.parse.urlparse(url).netloc
    title = articleUrlToTitle(url)

    query = f"https://{host}/w/api.php?action=query&prop=pageprops&titles={title}&format=json"
    jsonCode = rcd.just.getData(query, text=True, cacheSec=cache_sec,
								beforeDownloadFunc=lambda: time.sleep(1 / 3))
    # print(jsonCode)

    pages = json.loads(jsonCode)["query"]["pages"]
    firstPage = next(iter(pages.values()))
    # print(firstPage)
    return firstPage["pageprops"]["wikibase_item"]


# print(jsonCode)

# 135/636 https://en.wikipedia.org/w/index.php?title=Gregorio_Castaneda&action=edit&redlink=1-> Q395712

# https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&titles=Kofoworola_Abeni_Pratt&format=json


def articleUrlToWikidataId(*args, **kwargs):
    warnings.warn("Obsolete", DeprecationWarning)
    article_url_to_wikidata_id(*args, **kwargs)


if __name__ == "__main__":
    pass

# TestWikipedia().test_to_title()
