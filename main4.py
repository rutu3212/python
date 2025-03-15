import requests


API_URL = "http://demo3773962.mockable.io"

def fetch_supermarket_data():
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()  
        display_data(data)
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")

def display_data(data):
    if isinstance(data, dict) and "supermarket" in data and "transactions" in data:
        print("\n Supermarket Details:")
        print(f"Store Name: {data['supermarket']['store_name']}")
        print(f"Location: {data['supermarket']['location']}")
        print(f"Contact: {data['supermarket']['contact']}\n")
        
        print("🛒 Transactions:")
        for item in data["transactions"]:
            print(f"Item Number: {item['item_number']}, Item Name: {item['item_name']}, Quantity: {item['quantity']}, "
                  f"Price Per Unit: ₹{item['price_per_unit']}, Total Bill: ₹{item['total_bill']}, "
                  f"Customer Phone: {item['phone_num']}")
            print("-" * 80)
    else:
        print("Error: Missing required data in API response.")

if __name__ == "__main__":
    fetch_supermarket_data()
