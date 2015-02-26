import requests
import urllib


class FacebookProvider:
    def __init__(self):
        self.apiKey = '475353605936118'
        self.apiSecret = '659818065b06a664b7c3a5a40e15f51e'
        self.accessToken = 'CAACEdEose0cBAFYeZANizijVRcKZBzpZC9W3rZCztDFJy6BbiSIhBvXdTL5MAz0D3q4cFfi91QDmrYVURM9hn4davpXNOGwSVnOEJC9GlLahnukCplRxKEDpLFpVZBPZBlmragLJ5CCqE6AZB1UFy8apTWT1jEZCLTe8LKKBVfyADHWrkDtv6U6BlSpZCcTPdWSElBZA6grnl2TWJ1uB8isB1CGrhHwrkmyTYZD'

    def search_pages(self, search_terms):
        result = []
        params = {
            "q": search_terms,
            "type": "page",
            "access_token": self.accessToken,
            "locale": "pt_PT",
            "limit": 10

        }
        url = 'https://graph.facebook.com/v2.2/search?' + urllib.urlencode(params)
        r = requests.get(url)
        fb_pages_json = r.json()
        for fb_page in fb_pages_json['data']:
            result.append({
                'name': fb_page['name']
            })
        return result