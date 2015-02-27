import requests
import urllib
from requests_oauthlib import OAuth1


class TwitterProvider:
    def __init__(self):
        self.auth = OAuth1(
            'hxyttWQ5OuciWPJdBJgntZ3UO',
            'oJFPWpLuuNM3hjfpTLhKCMOdjHo5gQktdzTfEK5BaetznEn5dK',
            '22373407-72aJvjhjUH7BZ3J9kJjeuv0wrWBWh4cRxCfNUGG89',
            'zA3YWLSxJr0BgvGnh5Ca9QXKhiumSUyTi5pYvxUJ7nNvh'
        )

    def search_tweets(self, search_terms):
        result = []
        params = {
            "lang": "pt",
            "q": search_terms,
            "count": 5
        }
        url = 'https://api.twitter.com/1.1/search/tweets.json?' + urllib.urlencode(params)
        r = requests.get(url, auth=self.auth)
        tweets_json = r.json()
        for tweet in tweets_json['statuses']:
            result.append({
                'text': tweet['text'],
                'picture': tweet['user']['profile_image_url']
            })
        return result

    def search_trends(self):
        result = []
        params = {
            "id": "23424925"
        }
        url = 'https://api.twitter.com/1.1/trends/place.json?' + urllib.urlencode(params)
        r = requests.get(url, auth=self.auth)
        print r.text
        trends_json = r.json()
        for trend in trends_json[0]['trends']:
            result.append({
                'name': trend['name']
            })
        return result[:2]