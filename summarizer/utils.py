import re
from transformers import pipeline


class TextProcessor:
    def __init__(self):
        self.summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
        self.simplifier = pipeline('text2text-generation', model="t5-base")
        self.translator = pipeline('translation_en_to_fr', model="Helsinki-NLP/opus-mt-en-fr")

    def clean_text(self, text):
        # Nettoyage de termes incorrects
        text = re.sub(r'\bFrançoise\b|\badolescente\b', '', text)
        return text.strip()

    def capitalize_sentences(self, text):
        return re.sub(r'(\. )([a-z])', lambda p: p.group(0).upper(), text).capitalize()

    def remove_redundancy(self, text):
        # Supprimer les phrases redondantes
        sentences = text.split('. ')
        seen = set()
        cleaned_sentences = []
        for sentence in sentences:
            if sentence.lower() not in seen:
                seen.add(sentence.lower())
                cleaned_sentences.append(sentence)
        return '. '.join(cleaned_sentences)

    def simplify_text(self, text):
        try:
            simplified_text = self.simplifier(f"simplify: {text}", max_length=90, min_length=30, do_sample=False)[0][
                'generated_text']
            simplified_text = self.capitalize_sentences(simplified_text)
            simplified_text = self.clean_text(simplified_text)
            simplified_text = self.remove_redundancy(simplified_text)
            translated_text = self.translate_text(simplified_text)
            return translated_text
        except Exception as e:
            return f"Error in simplification: {e}"

    def summarize_text(self, text):
        max_length = min(130, len(text.split()) * 2)
        min_length = min(30, len(text.split())) // 2
        try:
            summarized_text = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0][
                'summary_text']
            summarized_text = self.clean_text(summarized_text)
            translated_text = self.translate_text(summarized_text)
            return translated_text
        except Exception as e:
            return f"Error in summarization: {e}"

    def translate_text(self, text):
        try:
            translated_text = self.translator(text)[0]['translation_text']
            return translated_text
        except Exception as e:
            return f"Error in translation: {e}"

    def process_text(self, text):
        summarized_text = self.summarize_text(text)
        if "Error" in summarized_text:
            return {'error': summarized_text}

        simplified_text = self.simplify_text(summarized_text)
        if "Error" in simplified_text:
            return {'error': simplified_text}

        return {
            'simplified_text': simplified_text,
            'summarized_text': summarized_text
        }
