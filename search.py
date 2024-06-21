# import requests
# from bs4 import BeautifulSoup
#
#
# def search_scientific_sites(query):
#     # URL de recherche Google (ou autre moteur de recherche)
#     search_url = f"https://www.google.com/search?q={query}"
#
#     # Effectuer la requête
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(search_url, headers=headers)
#     response.raise_for_status()
#
#     # Analyser le contenu de la page
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # Trouver tous les liens pertinents
#     for g in soup.find_all('div', class_='g'):
#         anchors = g.find_all('a')
#         if anchors:
#             link = anchors[0]['href']
#             print(f"Found link: {link}")
#
#
# # Exemple d'utilisation
# search_query = "scientific research articles"
# search_query = "articles scientifiques"
# search_scientific_sites(search_query)
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def search_pdfs(query):
#     search_url = f"https://www.google.com/search?q={query}+filetype:pdf"
#
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(search_url, headers=headers)
#     response.raise_for_status()
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     for g in soup.find_all('div', class_='g'):
#         anchors = g.find_all('a')
#         if anchors:
#             link = anchors[0]['href']
#             if link.endswith('.pdf'):
#                 print(f"Found PDF: {link}")
#
#
# # Exemple d'utilisation
# search_query = "fusion froide"
# search_pdfs(search_query)


