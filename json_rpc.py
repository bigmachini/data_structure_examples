import requests
import json

def main():
    url = "http://localhost:3030"
    url = "{}/web/session/authenticate".format(url)
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload ={
    "jsonrpc":"2.0",
    "method": "call",
    "params":
        {
        "db": "odoo_erp",
        "login":"admin",
        "password": "Adm1N@C0p1A18"
        },
    "id":666
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print("response: {}".format(response))

if __name__ == "__main__":
    main()