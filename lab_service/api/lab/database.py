import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

credential = {
    "type": "service_account",
    "project_id": "ifamils",
    "private_key_id": "d38c8ffa6764bbc6405cbfe0a3d107d6e3b97257",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC53lyOo+nFeLJl\n22HKAApMg483Rd+mDSo23vOGC3IMQDemSxvosdlmQoW9o3T7mkBg94+E/jz6zovC\nk9b1Y/vDzeVDdOZGfwXJqOajHhGzMbSHZobiM/xeEd2/FOj4iK7AHe4d+6DZcVZi\nE4X8plKpn/ylyUHUFFxhORFKaA4fRh13JMw1he13GZrAQkMexg1PJDr2NLLlHOAA\n+fm0uhs6m3C9sb46hBSa8KVhRJU7LD8FcPmItU/9WxMhT4SJ61w3sKbx0HdGsEg6\nhWXjJMcE/50+bgl3uRoEg7ECLiqyX63qAfTTsHb54/wr6DECDlcnDDi3RcI4Ak1S\npAbKbXEDAgMBAAECggEABLas5jkl7ooXDBo6KqNBn5segKpW96ER1v5kcpvLsp/W\nSXNSK96Gwt8hASQqDU9mHo9opljENyARz0dshiCY++g2zjUiudryzKBp6O0USdUS\n3PQuq4Hh/oi5dOUU22ir9ddMeJovBBSpuicAmN2m7wJNp+6oqrYxeY228IofAY/8\nckwp5yCNkQt7l5ms1OAIo7x9EVjhi/p5ZHNM5TdPpBAMFHh8FpUSvYS4J/XkBYsl\nmyttvgc+EMPj1fR/77Eef2u/KL1prSlFsJLHBBV+/GkYYdhvMh6nbJSERYL7kWVN\nKJrkjN/iU0s5l+lK/kWEUSlRuBVrqPmbl0Ycd1wsYQKBgQD94feRMxj1ThtSSZ/1\nMlpTULEfPxmKtjjEQc9HgjN8kB1j4Yo75POe7jqJ7/anw5X+Wfb1+tO817Q+7xnu\nNBOMv2kISTKbvOjgEvYtRq8pK0tMvJGQfKapOU2/EguUNOYpJwTCD7bU3u6BklwS\nYFfeacZFR65No3bj4BOmPazeSQKBgQC7ay+qBW+ilKdPsKmhobyDgJYagiCQe+dJ\nMpVi8hvl7MYdamRrX40s4XkpM2BqAvWTLo1IBxsrBU/c2ILtfM3sWDQfWpa1QAF/\n5i2g6WVuuzGS52VmaWGu1RPtUA60nzpHx5oh26EI0RfYYkSCgtP0ed0S80RRZnKu\nAnme3CJE6wKBgFf9y0n9xbavXXTFo7TdwMSDgP/tZLLYuQ/8JxUHoUSYxjbp4nkj\nvvPkaVGJY5l9hizjjV5vkpcuw3/Uas5OKkBrzsFabTng3W1b5QqIJwlDwhNUf7bu\nHO0luTZx0KWLOAInTdTckWdx5IPv8A1Gau3hByDX2Sd7cidEcEr7sUBRAoGBALJG\nrzxHl31Lcit3nKRHOQ7NzfrBNUC627LhDwDj1G3N4FYy0frhFWVPxPTQDjJJRlgO\nvA171PgDQYiN210Ujrz22f3JKfqXO9Xxmg2qdfXy0qEuw2G7dFPeE+p1cMeXftSw\npYj3ZiMA4nHOZ+TNldjD4usXxDC6BvRHHnFibKapAoGAWpjxNWsX97dwrvaddWiC\n0LL7PbuUh0a8BsszSLAfaa8wlIe59+eQkvMCOsTeycRGdgY4FFRPSEmSQCqb5nHd\nWlv11WGHYAilUvMR0htFpCO1wKoS/Js4x/qDI9pbM5eh9nAdLiexD5PT6OA3Gkct\nbfSnzuk7oi9H1wCvaMEAW5A=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-4whv9@ifamils.iam.gserviceaccount.com",
    "client_id": "117046601303785763687",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-4whv9%40ifamils.iam.gserviceaccount.com"
}

class Database():

    def __init__(self):
        # f = open('ifamils-firebase-adminsdk-4whv9-d38c8ffa67.json',)
        cred = credentials.Certificate(credential)
        firebase_admin.initialize_app(cred)

db = Database()
client = firestore.client()

# client.collection('labs').add({
#     'name': "LAB01",
#     'numberOfComputers': 15,
# })