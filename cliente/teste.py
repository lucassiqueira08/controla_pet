from raven import Client
from decouple import config

client = Client("https://2253bf24f06f4a1e84121a74969def8c@sentry.io/1300066")

try:
    "1" / 0
except:
    client.captureException()
