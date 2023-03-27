

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
