import os

# discord bot token
TOKEN = "MTQ1OTk4NzAzMDU2OTM5MDI0NA.GU4fk5.oh3PROncn10rEx0PeV-KiVflZ8rvrhnSEDRHuM"

# db password for postgres
# user - cat_bot, database - cat_bot, ip - localhost, port - default
# Skye: defaulting to 'cat_bot_password' because I know you'll forget to set the env var
DB_PASS = os.environ.get("psql_password", "cat_bot_password")

#
# all the following are optional (setting to None will disable the feature)
#

# dsn of a sentry-compatible service for error logging
SENTRY_DSN = os.environ.get("sentry_dsn")

# top.gg vote webhook verification secret, setting this to None disables all voting stuff
WEBHOOK_VERIFY = os.environ.get("webhook_verify")

# top.gg modern (v1) token to post stats, commands and fetch fallback votes
TOP_GG_MODERN_TOKEN = os.environ.get("top_gg_modern_token")

# wordnik api key for /define command
WORDNIK_API_KEY = os.environ.get("wordnik_api_key")

# only post stats if server count is above this, to prevent wrong stats
MIN_SERVER_SEND = 200_000

# channel id for db backups, private extremely recommended
BACKUP_ID = 1060545763194707998

# channel to store supporter images, can also be used for moderation purposes
DONOR_CHANNEL_ID = 1249343008890028144

# cat bot will also log all rain uses/movements here
# cat!rain commands here can be used without author check and will dm reciever a thanks message
RAIN_CHANNEL_ID = 1492635229846765620

# stores channels where fake egirl command was used: {channel_id: message_id}
fake_egirl_storage = {}
