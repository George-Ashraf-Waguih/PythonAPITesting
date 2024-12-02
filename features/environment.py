import requests

from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        json = {

        "ID": context.bookID

        }
        response_delete = requests.post(url, json=json, headers={"Content-type":"'application/json"}, )
        print(response_delete.status_code)  # 200
        assert response_delete.status_code == 200
        print(response_delete.json())
        res_del_json = response_delete.json()
        print(res_del_json['msg'])
        assert res_del_json['msg'] == 'book is successfully deleted'