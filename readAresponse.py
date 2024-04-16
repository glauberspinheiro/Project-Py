import requests

def fetch_data_from_endpoint(endpoint, headers):
    try:
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {endpoint}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching data: {str(e)}")
        return None

def print_selected_fields(data):
    if data:
        print("Available fields:")
        for key in data.keys():
            print(key)
        
        selected_fields = input("Enter fields you want to print (comma-separated): ").strip().split(',')
        
        print("Selected fields:")
        for field in selected_fields:
            if field.strip() in data:
                print(f"{field}: {data[field.strip()]}")
            else:
                print(f"Field '{field}' not found!")

if __name__ == "__main__":
    endpoint = input("Enter the endpoint URL: ").strip()

    headers = {
        "Authorization": "Basic  ",
        "Content-Type": "application/json"  # Adjust content type if needed
    }
    
    data = fetch_data_from_endpoint(endpoint, headers)
    if data:
        print_selected_fields(data)
