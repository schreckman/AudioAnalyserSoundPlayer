import speech_recognition as sr


class Speech2Text:
    def __init__(self, language: str):
        self.language = ""
        self.changeLanguage(language)

    def speech2text(self, filename: str):
        speech_engine = sr.Recognizer()
        with sr.AudioFile(filename) as f:
            data = speech_engine.record(f)
            text = speech_engine.recognize_google(data, language=self.language)
            return text

    def changeLanguage(self, language):
        self.language = language
        if self.language == "german":
            self.language = "de-DE"
        elif self.language == "english":
            self.language = "en-US"
        else:
            # fallback
            self.language = "en-US"


class TextAnalyser:
    def __init__(self, words: list):
        self.words = ""
        self.changeWords(words)

    def checkContains(self, text: str):
        c = 0
        for i in self.words:
            if text.find(i) != -1:
                c += 1
        if c >= 1:
            return True
        else:
            return False

    def changeWords(self, words: list):
        self.words = words
