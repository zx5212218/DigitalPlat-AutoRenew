import requests
import json
import os

email = os.getenv("DP_EMAIL")
password = os.getenv("DP_PASSWORD")

login_url = "https://dash.domain.digitalplat.org/api/login"
renew_url = "https://dash.domain.digitalplat.org/api/domain/renew"

session = requests.Session()

print("Logging in...")

resp = session.post(login_url, json={"email": email, "password": password})
if resp.status_code != 200:
    print("Login failed:", resp.text)
    exit(1)

print("Login success")

# 获取域名列表
domains_url = "https://dash.domain.digitalplat.org/api/domain/list"
resp = session.get(domains_url)
domains = resp.json().get("data", [])

if not domains:
    print("No domains found")
    exit(0)

for d in domains:
    domain = d["domain"]
    print(f"Renewing {domain} ...")

    r = session.post(renew_url, json={"domain": domain})
    print("Result:", r.text)

print("Done.")
