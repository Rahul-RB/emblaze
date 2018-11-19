class Config(object):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD=True
    CACHE_TYPE = "null"
    UPLOAD_FOLDER  = "./emblaze/uploads"
    ALLOWED_EXTENSIONS = set(['pdf'])

    
class TestingConfig(Config):
    TESTING = True
