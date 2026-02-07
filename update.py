import requests
import json

def fetch_data():
    # Porkbun's public pricing
    res = requests.get("https://api.porkbun.com/api/json/v3/pricing/get").json()
    data = []
    for tld, prices in res['pricing'].items():
        data.append({
            "tld": f".{tld}",
            "reg": float(prices['registration']),
            "renew": float(prices['renewal'])
        })
    return data

if __name__ == "__main__":
    domains = fetch_data()
    with open('domains.json', 'w') as f:
        json.dump(domains, f, indent=4)