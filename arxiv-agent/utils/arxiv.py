#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                 Tool for arXiv shearch                   #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/

import requests
import xml.etree.ElementTree as ET

def arxiv_search(query, max_results):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    results = []
    # metadata retrieval
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip()
        link = entry.find('atom:id', ns).text.strip()
        authors = [author.find('atom:name', ns).text.strip() for author in entry.findall('atom:author', ns)]
        published = entry.find('atom:published', ns).text[:10]
        results.append({
    "title": title,
    "authors": authors,
    "summary": summary,
    "url": link,
    "date": published
})
    return results