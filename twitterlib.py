import oauth2
import urllib
import json

class Twitter:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(self, consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def tweet(self, novo_tweet):
        query_cod = urllib.quote(novo_tweet, safe='')
        req = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_cod, method='POST')
        decodificar = req[1].decode()
        req_objeto = json.loads(decodificar)
        return req_objeto

    def search(self, query, lang):
        query_cod = urllib.quote(query, safe='')
        req = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_cod + '&lang=' + lang)
        decodificar = req[1].decode()
        req_objeto = json.loads(decodificar)
        tweets = req_objeto['statuses']
        return tweets