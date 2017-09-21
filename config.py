# config.py


class Config(object):
    """"
    Common configurations
    """

    # Put any common configurations across all environments here


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
