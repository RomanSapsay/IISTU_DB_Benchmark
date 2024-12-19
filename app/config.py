class Config:

    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:EfOFAAZabDkkMOuuBrvHpwFILlrPUsHF@autorack.proxy.rlwy.net:56784/railway'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'your-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = 30

    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'