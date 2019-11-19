class Development:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:apple@127.0.0.1:5432/ims'
    SECRET_KEY = 'sdfghjkla'


class Production:
    pass
