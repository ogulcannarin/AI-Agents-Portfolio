from duckduckgo_search import DDGS

def search_tool(query):

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

    texts = []

    for r in results:
        texts.append(r["body"])

    return "\n".join(texts)