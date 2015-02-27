from communities.TwitterProvider import TwitterProvider


class TopicsProvider:

    def __init__(self):
        self.twitterProvider = TwitterProvider()
        self.editorialTopics = {
            "news": [
                {
                    "title": "Socrates continua em preventiva",
                    "img": "img/socrates.jpg"
                }, {
                    "title": "Madonna living for love",
                    "img": "img/madonna.jpg"
                }
            ],
            "books": [
                {
                    "title": "Prometo Falhar",
                    "img": "img/falhar.jpg"
                }, {
                    "title": "O irmao alemao",
                    "img": "img/alemao.jpg"
                }
            ],
            "music": [
                {
                    "title": "Duetos II",
                    "img": "img/duetos.jpg"
                }, {
                    "title": "Rua da Emenda",
                    "img": "img/emenda.jpeg"
                }
            ]
        }
        self.trendingTopics = {
            "news": [
                {
                    "title": "PJ detem Jornalista do Site TugaLeaks",
                    "img": "img/ruicruz.jpeg"
                }, {
                    "title": "Assassino de Chris Kyle condenado a perpetua",
                    "img": "img/assassino.jpg"
                }
            ],
            "books": [
                {
                    "title": "Barroco tropical",
                    "img": "img/barroco.jpg"
                }, {
                    "title": "O fio das missangas",
                    "img": "img/missangas.jpg"
                }
            ],
            "music": [
                {
                    "title": "Storia, Storia",
                    "img": "img/storia.jpg"
                }, {
                    "title": "Criolo",
                    "img": "img/criolo.jpg"
                }
            ]
        }

    def get_trending_topics(self, category):
        return self.trendingTopics[category]

    def get_editorial_topics(self, category):
        return self.editorialTopics[category]
