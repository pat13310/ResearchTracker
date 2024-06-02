import unittest
from summarizer.utils import TextProcessor

class TestTextProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = TextProcessor()

    def test_simplify_text(self):
        text = (
            "Les récentes avancées dans le domaine de l'intelligence artificielle ont conduit au développement de modèles sophistiqués capables de réaliser une large gamme de tâches avec une grande précision. "
            "L'un de ces modèles est le transformer, qui a révolutionné notre approche du traitement du langage naturel. "
            "En exploitant la puissance des transformers, les chercheurs ont atteint des résultats de pointe dans diverses tâches de NLP, y compris la simplification de texte, la traduction et la réponse aux questions. "
            "Ces avancées ouvrent la voie à des systèmes plus intelligents capables de comprendre et d'interagir plus efficacement avec les humains."
        )
        simplified_text = self.processor.simplify_text(text)
        self.assertIsInstance(simplified_text, str)
        self.assertNotEqual(text, simplified_text)
        print(f"Texte simplifié : {simplified_text}")

    def test_summarize_text(self):
        text = (
            "Les récentes avancées dans le domaine de l'intelligence artificielle ont conduit au développement de modèles sophistiqués capables de réaliser une large gamme de tâches avec une grande précision. "
            "L'un de ces modèles est le transformer, qui a révolutionné notre approche du traitement du langage naturel. "
            "En exploitant la puissance des transformers, les chercheurs ont atteint des résultats de pointe dans diverses tâches de NLP, y compris la simplification de texte, la traduction et la réponse aux questions. "
            "Ces avancées ouvrent la voie à des systèmes plus intelligents capables de comprendre et d'interagir plus efficacement avec les humains."
        )
        summarized_text = self.processor.summarize_text(text)
        self.assertIsInstance(summarized_text, str)
        self.assertNotEqual(text, summarized_text)
        print(f"Texte résumé : {summarized_text}")

    def test_translate_text(self):
        text = (
            "Recent advancements in artificial intelligence have led to the development of sophisticated models capable of performing a wide range of tasks with high precision. "
            "One such model is the transformer, which has revolutionized our approach to natural language processing. "
            "By leveraging the power of transformers, researchers have achieved state-of-the-art results in various NLP tasks, including text summarization, translation, and question answering. "
            "These advancements are paving the way for more intelligent systems that can understand and interact with humans more effectively."
        )
        translated_text = self.processor.translate_text(text)
        self.assertIsInstance(translated_text.lower(), str)
        self.assertNotEqual(text, translated_text)
        # Optionally, check if the translated text contains expected French words
        #self.assertIn("récents progrès", translated_text.lower() or "progrès récents" in translated_text.lower())
        print(f"Texte traduit : {translated_text}")

if __name__ == '__main__':
    unittest.main()
