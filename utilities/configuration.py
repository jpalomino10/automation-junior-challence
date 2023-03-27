import configparser

def _getConfig():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    return config

def get_password():
    return _getConfig()['API']['password']

def get_email():
    return _getConfig()['API']['email']

def get_endpoint():
    return _getConfig()['API']['endpoint']
