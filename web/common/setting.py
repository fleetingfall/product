import os


class Config:
    DEBUG=True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    TEMPLATES_AUTO_RELOAD=True

    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:123456@localhost:3306/tea"
    SQLALCHEMY_ECHO=True

    UPLOAD_FOLDER="uploads"
    SECRET_KEY=os.urandom(24)