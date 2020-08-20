# python3 ベースのdocker image
## Twitter APIのOAuth1認証

環境変数はTwitter APIに登録しているアカウントから追記する

```
CONSUMER_KEY = 'TWITTER_CLIENT_KEY'
CONSUMER_SECRET = 'TWITTER_CLIENT_SECRET'
ACCESS_TOKEN = 'TWITTER_CLIENT_ID_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'TWITTER_CLIENT_ID_ACCESS_TOKEN_SECRET'
```

## requests.models.Responseクラスの属性
text属性からツイートを取得可能

```
print(response.text)
```

- url: url属性
url属性でアクセスしたURLを取得できる。
- ステータスコード: status_code属性
status_code属性でステータスコードを取得できる。
headers属性はCaseInsensitiveDictという型。
基本的には辞書（dict型）だが、小文字と大文字を区別しないという特徴がある。
- エンコーディング: encoding属性
headers属性でレスポンスヘッダを取得できる。
- レスポンスヘッダ: headers属性
encoding属性でRequestsが推測したエンコーディングを取得できる。
encoding属性には任意の値を代入することが可能。
- テキスト: text属性
encoding属性でデコードされたレスポンスの内容（文字列）はtext属性で取得できる。
Webページの内容を取得したい場合はこのtext属性を使う。
- バイナリデータ: content属性
デコードされていないレスポンスの内容（バイト列）はcontent属性で取得できる。
content属性は画像やzipなどのテキストではないデータをダウンロードするときなど
引用：http://hxn.blog.jp/archives/10811003.html


参考記事
- Dockerfile, docker-composeの作成
https://qiita.com/reflet/items/4b3f91661a54ec70a7dc
- requests-oauthlib
https://github.com/requests/requests-oauthlib