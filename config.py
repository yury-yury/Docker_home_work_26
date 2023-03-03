class Config:
    DB_NAME: str = 'yury_db'
    DB_USER: str = 'yury'
    DB_PASSWORD: str = 'password'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False