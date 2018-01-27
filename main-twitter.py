from twitterlib import Twitter

consumer_key = '<yourkey>'
consumer_secret = '<yoursecret>'
token_key = 'yourtoken-key'
token_secret = '<yourtoken-secret>'

twitter = Twitter(consumer_secret,consumer_key,token_secret,token_key)


twitter.tweet('Testando lib')
pesquisa = twitter.search('0x00s4d', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])
    print('')
