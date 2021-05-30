import requests
import json


def submit(slack_id: str, learning_unit: int) -> None:
    '''
    Submits the notebook to the grades-collector.

    param slack_id like "UTS63FC02"
    param learning_unit like 0
    '''
    data = {
        "learning_unit": learning_unit,
        "slack_id": slack_id,
        "grade": 0,
        "metadata": {}
    }
    response = requests.put(
        "https://sub-nb-grades-collector.herokuapp.com/submit",
        data=json.dumps(data)
    )
    print('Success' if response.ok else 'Whoopsie Daisy')
