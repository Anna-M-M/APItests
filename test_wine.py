import pytest
import requests
import json

def create_new_wine(pl):

    url = "http://127.0.0.1:5000/wines"

    headers= {'Content-Type': 'application/json'}
    
    # convert dict to json string by json.dumps() for body data
    return requests.post(url, headers=headers, data=json.dumps(pl,indent=4))

@pytest.mark.skip
def test_get_wine():

    url = "http://127.0.0.1:5000/wines/5f89dff0bd087862a0d115cc"
    
    payload = {}
    headers= {'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers, data=json.dumps(payload,indent=4))

    assert response.status_code == 200

    print(response.text.encode('utf8'))

@pytest.mark.skip
def test_post_wine():
    
    payload = {'name': "test wine", 'vineyard': "test vineyard"}
    
    response = create_new_wine(payload)

    assert response.status_code == 201

    resp_body = response.json()
    assert resp_body['name'] == payload["name"]
    assert resp_body['vineyard'] == payload["vineyard"]    

    print(response.text.encode('utf8'))

@pytest.mark.skip
def test_delete_wine():
    
    payload0 = {'name': "test wine", 'vineyard': "test vineyard"}
    
    response0 = create_new_wine(payload0)
    
    resp_body0 = response0.json()
    wine_id = resp_body0['id']
    
    url = "http://127.0.0.1:5000/wines/"+str(wine_id)

    payload = {}
    headers = {'Content-Type': 'application/json'}
    
    response = requests.delete(url, headers=headers, data=json.dumps(payload,indent=4))

    resp_body = response.json()

    assert response.status_code == 201
     
    print(response.text.encode('utf8'))   

def test_get_list_of_wines():

    url = "http://127.0.0.1:5000/wines"
    
    payload = {}
    headers= {'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers, data=json.dumps(payload,indent=4))

    assert response.status_code == 200

    print(response.text.encode('utf8'))
