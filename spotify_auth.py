client_id = "ac6bc03869be402082494553e4bb1b0b"
client_secret = "61514f59196d482698c48fd70cca278a"
redirect_uri  = "http%3A%2F%2Fgoogle.com%2F"

base_auth_url = "https://accounts.spotify.com/authorize?"

#Parameters:
# Client ID from app registration
"client_id=ac6bc03869be402082494553e4bb1b0b"
#Response Type as Code
"&response_type=code"
#Set redirect uri as http://google.com/, url encode
"&redirect_uri=http%3A%2F%2Fgoogle.com%2F"

parameters = { "client_id": "ac6bc03869be402082494553e4bb1b0b", "response_type": "code", "redirect_uri": redirect_uri}

#Run the following authorization url, will redirect so we can retrieve the "code"
auth_url = "https://accounts.spotify.com/authorize?client_id=ac6bc03869be402082494553e4bb1b0b&response_type=code&redirect_uri=http%3A%2F%2Fgoogle.com%2F"
print(auth_url)

code_input = input("What is the code retrieved from the redirect uri? ")

#Client ID: Client Secret -> base64 encode
#ac6bc03869be402082494553e4bb1b0b:61514f59196d482698c48fd70cca278a
#YWM2YmMwMzg2OWJlNDAyMDgyNDk0NTUzZTRiYjFiMGI6NjE1MTRmNTkxOTZkNDgyNjk4YzQ4ZmQ3MGNjYTI3OGE=

#Token endpoint, CURL COMMAND TO GET TOKEN
token_base_url = "https://accounts.spotify.com/api/token"

#Parameters:
#curl -H "Authorization: Basic YWM2YmMwMzg2OWJlNDAyMDgyNDk0NTUzZTRiYjFiMGI6NjE1MTRmNTkxOTZkNDgyNjk4YzQ4ZmQ3MGNjYTI3OGE=" 
#-d grant_type=authorization_code 
#-d code= code 
#-d redirect_uri=http%3A%2F%2Fgoogle.com%2F 
#https://accounts.spotify.com/api/token

token_curl = "curl -H 'Authorization: Basic YWM2YmMwMzg2OWJlNDAyMDgyNDk0NTUzZTRiYjFiMGI6NjE1MTRmNTkxOTZkNDgyNjk4YzQ4ZmQ3MGNjYTI3OGE=' -d grant_type=authorization_code -d code=" + code_input + " -d redirect_uri=http%3A%2F%2Fgoogle.com%2F https://accounts.spotify.com/api/token"

print(token_curl)

#Run token curl in terminal for access token and refresh token

access_token = input("What is the access code retrieved? ")
refresh_token = input("What is the refresh token retrieved? ")

# Access Token and Refresh Token Info Retrieved
{
    "access_token": access_token,
    "token_type":"Bearer",
    "expires_in":3600,
    "refresh_token": refresh_token,
    "scope":""
}
