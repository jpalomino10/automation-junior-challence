

def register():
    json_schema = {
        "title": "Register User",
            "type": "object",
            "properties": { 
                "id": {"type": "number"},
                "token": {"type": "string"}
            },
            "required": [
                "id",
                "token"
            ]
    }

    return json_schema

def error():
     return {
        "title": "Error",
        "type": "object",
        "properties": { 
            "error": {"type": "string"}
        },
        "required": ['error']
     }


def login():
     return {
        "title": "Login",
        "type": "object",
        "properties": { 
            "token": {"type": "string"}
        },
        "required": ['token']
     }

def users():
     return {
        "title": "Login",
        "type": "object",
        "properties": { 
            "data": { "$ref": "#/definitions/Data"}
        },
        "definitions": {
            "Data": {
                "title": "Data",
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"}
                 }
            },
            "required": ["id","email","first_name","last_name","avatar"],
        }
     }


def empty():
     return {
        "title": "Empty Result",
        "type": "object",
        "properties": {}
     }