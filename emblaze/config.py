class Config(object):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD=True
    CACHE_TYPE = "null"
    UPLOAD_FOLDER  = "./emblaze/ResumeParser/data/input/example_resumes"
    ALLOWED_EXTENSIONS = set(['pdf'])
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'RahulRB@1997'# Put your MySQL root password here
    MYSQL_DATABASE_DB = 'WTProject'
    MYSQL_DATABASE_HOST = 'localhost'
    
class TestingConfig(Config):
    TESTING = True
