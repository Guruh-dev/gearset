import requests
import json

# API endpoint for customer data retrieval
api_url = https://staging.gearset.com/

# Create a session to simulate a logged-in user from Team A
session = requests.Session()
session.cookies.set('sessionid', 'valid_session_cookie_for_TeamA')

def fetch_data(customer_id):
    response = session.get(api_url, params={'customerId': customer_id})
    
    # Debug: print request details
    print(f"Request URL: {response.url}")
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    
    # Attempt to parse JSON
    try:
        data = response.json()
        print(json.dumps(data, indent=4))
    except Exception as e:
        print("Failed to parse JSON:", response.text)

print("Team A Data Response:")
fetch_data('TeamA')

print("\nTeam B Data Response:")
fetch_data('TeamB')
