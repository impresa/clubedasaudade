from TopicsProvider import TopicsProvider


class TopicsFacade:
    def __init__(self):
        self.topicsProvider = TopicsProvider()

    def get_topics(self, category):
        category_topics = {}

        trending_topics = self.topicsProvider.get_trending_topics(category)
        category_topics["trending"] = trending_topics

        editorial_topics = self.topicsProvider.get_editorial_topics(category)
        category_topics["editorial"] = editorial_topics

        return category_topics
