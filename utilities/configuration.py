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

def get_user_id():
    return _getConfig()['API']['user_id']

def get_avatar():
    return _getConfig()['API']['avatar']

def get_first_name():
    return _getConfig()['API']['first_name']

def get_last_name():
    return _getConfig()['API']['last_name']
