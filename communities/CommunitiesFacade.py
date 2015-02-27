from TwitterProvider import TwitterProvider


class CommunitiesFacade:
    def __init__(self):
        self.twitterProvider = TwitterProvider()

    def search_comments(self, search_terms):
        return self.twitterProvider.search_tweets(search_terms)

    def search_trends(self):
        return self.twitterProvider.search_trends()