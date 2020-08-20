from requests_oauthlib import OAuth1Session

# トークン情報
CONSUMER_KEY = 'TWITTER_CLIENT_KEY'
CONSUMER_SECRET = 'TWITTER_CLIENT_SECRET'
ACCESS_TOKEN = 'TWITTER_CLIENT_ID_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'TWITTER_CLIENT_ID_ACCESS_TOKEN_SECRET'
# OAuth認証
api = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# 「hogehoge」が含まれるツイートを5つ取得
url = 'https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended'
params = {'q': 'roland', 'count': 5}
response = api.get(url, params=params)


# print(type(response)) // <class 'requests.models.Response'> レスポンスクラス
print(response.text)