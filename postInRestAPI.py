import csv
import json
import requests

def main():
    try:
        # Ler arquivo CSV
        csv_data = read_csv('dadosUsers.csv')

        # Enviar payload para o endpoint
        send_data_to_api(csv_data)
    except Exception as e:
        print('Ocorreu um erro em:', e)

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def send_data_to_api(data):
    url = 'http://localhost:3000/webhook'  # adicionar o a URL

    payload = [{ 'nome': entry['NOME'], 'email': entry['EMAIL'], 'equipe': entry['EQUIPE']} for entry in data]

    response = requests.post(url, json=payload)

    if response.ok:
        print(json.dumps(response.text))
    else:
        print('Failed to send data to the API')

if __name__ == "__main__":
    main()