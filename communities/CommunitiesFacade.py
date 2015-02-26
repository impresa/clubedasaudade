from TwitterProvider import TwitterProvider


class CommunitiesFacade:
    def __init__(self):
        self.twitterProvider = TwitterProvider()

    def search(self, tags):
        return self.twitterProvider.search(tags)