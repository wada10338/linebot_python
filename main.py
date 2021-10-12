import requests
from line_access_token import ACCESS_TOKEN
import sys

def main():
    api_url="https://notify-api.line.me/api/notify"
    headers = {"Authorization":"Bearer {}".format(ACCESS_TOKEN)}
    data = {"message":"こんにちは！"}
    requests.post(api_url,headers=headers,data=data)
if __name__ == "__main__":
    main()