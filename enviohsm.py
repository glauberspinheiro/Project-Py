import http.client
import json

conn = http.client.HTTPSConnection("api.wetalkie.net")
payload = json.dumps({
  "destinations": [
    {
      "to": "5534992133488"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YXBpLnVyYS5pbmZvQHdldGFsa2llLmNvbTpHLVE3eTMzYjVjYS0='
}
conn.request(f"POST", "/callcenter/hsm/send/2169", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))