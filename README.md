# Sleepbox UI

## Información:
[Trello Oficial](https://trello.com/b/fulZH2iV/sleepbox)

## Video Presentación:

[![SLEEPBOX UI PRESENTACION](https://img.youtube.com/vi/HS-1_-khcUI/0.jpg)](https://www.youtube.com/embed/HS-1_-khcUI)

## Historico:

### Semana 1 (23 marzo - 27 marzo)
  - Se ha creado el proyecto backend Django
  - Se ha creado el [Trello Oficial](https://trello.com/b/fulZH2iV/sleepbox)

### Semana 2 (30 marzo - 3 abril)
  - Se ha subido el repositorio de la API (carpeta Sleepbox API dentro de este repositorio)
  - Se están implementando los servicios de firebase por medio de API.
  - Se está haciendo uso de "TDD" o "Desarrollo guiado por pruebas". Ejemplo: 
```
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
```
