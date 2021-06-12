from google.cloud import automl_v1beta1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.getcwd(), 'key.json')


def get_prediction(content):
    project_id = "159077774146"
    model_id = "ICN5826855274329145344"
    prediction_client = automl_v1beta1.PredictionServiceClient()
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content}}
    request = prediction_client.predict(name=name, payload=payload)
    return request.payload[0].display_name

