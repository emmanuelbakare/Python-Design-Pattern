
class Translator:
    def translate(self, text):
        pass


# Define the Adaptee class for Google Translate API
class GoogleTranslateAPI:
    def translate_text(self, text):
        print(f"Translating '{text}' to {text[::-1]} using Google Translate API")


class GoogleTranslateAdapter(Translator):
    def __init__(self, google_translate_api):
        self._google_translate_api = google_translate_api

    def translate(self, text):
        self._google_translate_api.translate_text(text)




# Define the Adaptee class for Yandex Translate API
class YandexTranslateAPI:
    def yandex_translate(self, text):
        print(f"Translating ''{text}' to {', '.join(text)} using Yandex Translate API")


class YandexTranslateAdapter(Translator):
    def __init__(self, yandex_translate_api):
        self._yandex_translate_api = yandex_translate_api
    
    def translate(self, text):
        self._yandex_translate_api.yandex_translate(text)


text = "Hello, how are you?"
google_translate_api = GoogleTranslateAPI()
google_translate_adapter = GoogleTranslateAdapter(google_translate_api)
google_translate_adapter.translate(text)


yandex_translate_api = YandexTranslateAPI()
yandex_translate_adapter = YandexTranslateAdapter(yandex_translate_api)
yandex_translate_adapter.translate(text)