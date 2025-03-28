import requests  # pip install requests

def is_online(url="http://www.google.com", timeout=5):
    try:
        # Try to make a GET request to the specified URL
        response = requests.get(url, timeout=timeout)
        
        # Check if the response status code is in the success range (200-299)
        return 200 <= response.status_code < 300

    except requests.ConnectionError:
        return False

# Example usage
# def internet_status():
#     if is_online():
#         print("System is online.")
#     else:
#         print("System is offline.")

# # Call the function to check internet status
# internet_status()
