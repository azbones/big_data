from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tempfile import NamedTemporaryFile


class TwitterAuth:
    """
    Class to authenticate to Twtitter and return connection object.
    Keys are available from Twitter at https://apps.twitter.com after
    setting up an app under "Keys and Access Tokens".

    Attributes:
        consumer_key(str): Consumer Key (API Key)
        consumer_secret(str): Consumer Secret (API Secret)
        access_token(str): Access Token
        access_token_secret(str): Access Token Secret
    """

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key 
        self.consumer_secret = consumer_secret 
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def make_connector(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        
        return auth


class PrintStream(StreamListener):
    """
    Subclass to send strea data to console using print.
    """ 

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


class FileStream(StreamListener):

    """
    Subclass to send stream data to console using print.

    Attributes:
        filepath(file): file for output
    """ 
    def __init__(self, filepath):
        self.filepath = filepath

    def on_data(self, data):
        with open(self.filepath, 'a') as f:
            f.write(data)

    def on_error(self, status):
        print status


def get_stream(con,listener):
    stream = Stream(con,listener)
    return stream
