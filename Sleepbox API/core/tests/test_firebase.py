from django.test import TestCase
import unittest
from unittest import mock
import json
import inspect
from core.tools import firebase_client, dict_manipulate
from core.models.batch import Batch
from django.core import serializers
import time


class FirebaseTest(TestCase):
    def setUp(self):
        pass

    def test_get_config_file(self):
        # Arrange
        client = mock.Mock()
        path = "core/tools/config.json"

        client.config = {
            "type": "service_account",
            "project_id": "sleepbox-fb735",
            "private_key_id": "f822bcf3f5348848ccb0b8f4f2227cbe6871c7c0",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDuHOb88p0cNcLy\nIc8VRxzxiX9oiAyBZgyNnnZG0aNG2jddv9T9jXvp8BZHb77K7q9vj080QG0tB9j0\nvI6T82oDuTaJeJl9ubFDQ3770svY+rIWClJ8yLn/9WTz2yhcxLB8V3t0cHDb9nMM\naH4ADUtyOQUunRV+cxuGenw/d8+FZ8rNzSGegyg92R8oGfGQWz0i/MLYljIWd09T\nj3IcSuFHBW2fFZF9r0xOcnG/lB53z4rhCt4eJN1gjML7cWaGouNb7IU1w2v3wxbO\n3jSY/64Rfq9XeidGXM8nbqI/GAM/aUtwhkFaKCa2+yleJCs99DMGShGjee7DE4J2\ngWDgmOfbAgMBAAECggEACOc+wdWGh2ABPpGCDz8d93AXOf7gTNRWgtMahBJhowwU\nxuYd3i80o24tPxWQEkFzgN3gbck869Kfy6LjR+fxnlsGDYTbZGaVmLjE3kCnC6Fw\nGD/hjrXosofn8vBOZY2bNcMFpDhyF99ytNORZooYuJgmN/R6scQ3EsOwsqTVtxy0\ncNsbwvDI4eLanqyj0y7BV6JLB0x5Fh3a5dFszsT44iWrMCoP5EvY9OAtP+2dDL4S\n5/XaXJ5rqVPwhp0kEMBuyClqSdwRwm8ggW9JSw5IC6OaDYeugFY3/2CuzYlwMlmN\nv3q4w5YAnEAGYlCymAqcnPOWUs+QwW3BBzRK3TcOZQKBgQD/JIZiSG5RoULvRmUr\nDQRj+UNexJUx2BOE0QH70cAweicnxgfqkvCgVBFjWOMSZHvRsxbbnhS0WBvE3waK\nRZ6b3DvjMglrb4x+ef3QXbB6ohR27ZtKBvDBtODpWkunZCowYKvpCtXAlXq5pdfY\nlJYNFeaCaLQ0R/4h8H4nVz6+/QKBgQDu6bpvGW7Af60rYvVxBi155jkw7mUlX3XP\ndEJIq52wG9dKaOFZ/aDskYf1KTnnNpJ+TtVrSPqO6oAn5I/FcFdUBm8IJ/CTDHty\nMbFAn9o85d3mLt+k/VKhuvvQKtG27D+ridKxfmjJdDoCuUg0tNZ60COzVYclF2tp\nTZ5NEkQ1twKBgA5bl9RgDxU45fNhGsBZcy3NESV8Gok7h52pxVrOaupPdXSfiEKD\nEldzY6cbkWuvi+g5E8g4FSIw8x8ZDd0qHcrXkecvIaiSFm3nn4jiPNQp2sz2gg6g\nZVwBOcbn9entkRI33nS2z2CPCOD5nDPr6KXD3bzo93sZsgtm5TKBjl5hAoGBAM/6\nQaSTdDk5LCuXwug4I4B5bRHuhbhqCGmm4EjYtLXpFpqdAIfRZbRq3/sIf3KKrC4u\nPFVfu1aMRzHzI0ESEcOAsklcU23/MLtxDMegIGBhDrFh3qiHKdbGqo1FqThfIvIW\nUYbX7ypn9lQGrRfM0OUqqdlku/gLEiMiQYsAOsazAoGAODPRx/0KffhsW2WCvu5v\nJy6/x1kOcwrioA+k/SfnpsrdNycxtFnmLQKMa/KCD+gLv+xe34IQpyZx7SWoJFDv\nSuWNynQD/LozFokIntEDFuydgoAiOkyAQdsVazfAPdQe91QRKVicv4jKRvVztj5j\nT9qGNX8tBM2SjxgkFIan0Ns=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-xyi4p@sleepbox-fb735.iam.gserviceaccount.com",
            "client_id": "114505941830011615216",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xyi4p%40sleepbox-fb735.iam.gserviceaccount.com"
        }

        # Act
        try:
            with open(path) as file:
                config_file = json.load(file)
        except:
            config_file = "Error: File not found"

        # Assert
        self.assertEquals(client.config, config_file)

    @unittest.skip("skipping")
    def test_create_batch_document(self):

        # Arrange
        client = firebase_client.FirebaseClient()
        doc = Batch()
        doc.device_id = '1234567-F'
        doc.timestamp = int(time.time())

        # Act
        col = client.collection('batches')
        col.add(doc.__dict__)

        # Assert
        self.assertTrue(True)

    def test_get_batch_document(self):

        # Arrange
        client = firebase_client.FirebaseClient()

        args = {
            "device_id": '1234567-F',
            "timestamp": int(time.time())
        }
        doc = Batch(**args)

        # Act
        col = client.collection('batches')
        retrieved = {}
        for el in col.get():
            retrieved.update(el.to_dict())

        aux = Batch(**retrieved)

        # Assert
        self.assertEqual(type(doc), type(aux))
    
    @unittest.skip("skipping")
    def test_add_method_implementation(self):

        # Arrange
        client = firebase_client.FirebaseClient()
        doc = Batch(device_id='1234567-F', timestamp=int(time.time()))

        # Act
        firebase_client.FirebaseClient.add(
            collection='batches', document=doc.__dict__)

        # Assert
        self.assertTrue(True)
