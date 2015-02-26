class TopicsProvider:

    def __init__(self):
        self.editorialTopics = {
            "news": ["BES", "Socrates"],
            "music": ["Rui Veloso", "Xutos e Pontapes"],
            "books": ["1984","O Triunfo dos Porcos"]
        }
        self.trendingTopics = {
            "news": ["Secretas", "Grecia"],
            "music": ["Dead Combo", "Capitao Fausto"],
            "books": ["50 Sombras de Grey", "Caim"]
        }

    def get_trending_topics(self, category):
        return self.trendingTopics[category]

    def get_editorial_topics(self, category):
        return self.editorialTopics[category]
