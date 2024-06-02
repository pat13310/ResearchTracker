import feedparser
import requests

# URL du flux RSS


def read_rss(url):
    entries = []
    try:
        # Récupérer le flux RSS brut
        response = requests.get(url)
        response.raise_for_status()  # Assurez-vous que la requête a réussi

        # Vérifier s'il y a des erreurs de syntaxe
        feed_content = response.content.decode('utf-8')
        feed = feedparser.parse(feed_content)

        if feed.bozo:
            raise ValueError(f"Erreur lors de la récupération du flux RSS: {feed.bozo_exception}")

        entries = feed.entries

    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête HTTP: {e}")
    except ValueError as e:
        print(f"Erreur de flux RSS: {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")

    return entries


#rss_url = 'https://www.sciencesetavenir.fr/rss'
#rss_url="https://rss.sciencedirect.com/publication/science/00221694"
rss_url="https://www.cea.fr/presse/_layouts/15/i2i/web/ceasrchrss.ashx?pid=124&wid=g_7e22cc1a_b0a5_4b90_b17c_95c221e596d4"
rss_url="https://la1ere.francetvinfo.fr/decouverte/sciences/rss"
rss_url="https://partner-feeds.publishing.tamedia.ch/rss/24heures/savoirs"
rss_url="https://www.lemonde.fr/sciences/rss_full.xml"
rss_url="https://www.lepoint.fr/astronomie/rss.xml"
rss_url="https://cnes.fr/fr/news/feed"
rss_url="https://www.cnrs.fr/fr/rss/press.rss"
rss_url="https://anr.fr/rss/?news&aap"

entries = read_rss(rss_url)
for entry in entries:
    print(f"\nTitre: {entry.title}")
    print(f"Lien: {entry.link}")
    print(f"Résumé: {entry.summary}")
    if 'published' in entry:
        print(f"Publié le: {entry.published}")
