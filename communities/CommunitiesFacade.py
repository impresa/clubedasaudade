from TwitterProvider import TwitterProvider
from FacebookProvider import FacebookProvider


class CommunitiesFacade:
    def __init__(self):
        self.twitterProvider = TwitterProvider()
        self.facebookProvider = FacebookProvider()

    def search_comments(self, search_terms):
        return self.twitterProvider.search_tweets(search_terms)

    def search_pages(self, search_terms):
        return self.facebookProvider.search_pages(search_terms)