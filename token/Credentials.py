class Credentials:
    def __init__(cred):
        cred.api = ""
        cred.api_secret=""
        cred.token = ""
        cred.token_secret = ""
        with open('token/credentials.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
            
                key, value = line.split("=", 1)
            
            
                if key == "API-KEY":
                    cred.api = value
                elif key == "API-KEY-SECRET":
                    cred.api_secret = value
                elif key == "ACCESS-TOKEN":
                    cred.token = value
                elif key == "ACCESS-TOKEN-SECRET":
                    cred.token_secret = value
    def __str__(cred):
        return f"{cred.api} {cred.api_secret}"

