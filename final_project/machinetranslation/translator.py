from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    English to French
    """
    if english_text is None:
        return None
    else:
        french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
        return french_text

def french_to_english(french_text):
    """
    French to English
    """
    if french_text is None:
        return None
    else:
        english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
        return english_text
