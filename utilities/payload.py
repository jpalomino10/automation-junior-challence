def addRegisterPayload(user,password):
    body = {
        "email": user,
        "password":password
    }
    return body



def addLoginPayload(user,password):
    return addRegisterPayload(user,password)





