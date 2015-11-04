from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tempfile import NamedTemporaryFile
from interruptingcow import timeout

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


class TwitterAuth:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key 
        self.consumer_secret = consumer_secret 
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def make_connector(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        return auth


class PrintStream(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

class FileStream(StreamListener):

    def on_data(self, data):
        with open('test.txt', 'w') as f:
            f.write(data)

    def on_error(self, status):
        print status





auth = TwitterAuth(consumer_key, consumer_secret, access_token, access_token_secret)
con = auth.make_connector()
listener = PrintStream()
stream = Stream(con, listener)
