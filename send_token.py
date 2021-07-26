import requests


def post_id(token, telegram_id):
    url = 'http://127.0.0.1:8000/accounts/get_telegram_id'
    params = {'token': token, 'telegram_id': telegram_id}
    requests.post(url, params=params)
