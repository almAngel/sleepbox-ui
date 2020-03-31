import firebase_admin
import json
from firebase_admin import credentials, firestore
from core.tools.dbclient_iface import I_DBClient


class FirebaseClient(I_DBClient):
    _instance = None
    file_path = 'core/tools/config.json'

    def __new__(self):
        if FirebaseClient._instance is None:
            _credentials = credentials.Certificate(self.file_path)
            app = firebase_admin.initialize_app(credential=_credentials)
            FirebaseClient._instance = firestore.client()
        return FirebaseClient._instance

    @staticmethod
    def add(collection: str, document: dict):
        FirebaseClient._instance.collection(collection).add(document)
