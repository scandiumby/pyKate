from environs import Env

env = Env()
env.read_env()

# TODO: Move AUTH_BACKENDS declaration into documentation and it should be removed from here
#  (AUTH_BACKENDS should be blanked list by default)
AUTH_BACKENDS = [
    "pykate.auth.backends.telegram.TelegramNativeAuthFrontend",
    "pykate.auth.backends.telegram.TelegramPhoneAuthFrontend",
]

AUTH_SLUG = "auth"
AUTH_BACKENDS_SLUG = "backends"
AUTH_BACKENDS_ROOT = f"{AUTH_SLUG}/{AUTH_BACKENDS_SLUG}"

# AUTH_BACKENDS = [
#
# ]

# PLEASE DONT USE SECRET_KEY from env.demo in production environment
SECRET_KEY = env.str("SECRET_KEY")
ALGORITHM = env.str("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
