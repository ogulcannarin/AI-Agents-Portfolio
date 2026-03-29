import os
from langchain_community.tools.tavily_search import TavilySearchResults

# Tavily API anahtarını ortam değişkenlerinden alalım
# os.environ["TAVILY_API_KEY"] = "tvly-..." 

web_search_tool = TavilySearchResults(k=3) # En alakalı 3 sonucu getir