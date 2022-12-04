import random

chars = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()'
size = 50
secret_key = "".join(random.sample(chars, size))

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1,localhost

#DATABASE-URL=postgres://postgres:postgres@localhost/testdb


#AWS
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=

INTERNAL_IPS=127.0.0.1
SENTRY_DSN
""".strip() % secret_key

# Writing our configuration file to .env
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
