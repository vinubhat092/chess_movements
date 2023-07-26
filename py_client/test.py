import requests
import json
def make_api_request():
    url = "http://localhost:8000/chess/rook/"

    # Input data in JSON format
    input_data =  {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}
    try:
        response = requests.post(url, json=input_data)

        print("Request JSON Data:")
        print(input_data)
        print("Response Status Code:", response.status_code)
        print("Response JSON Data:")
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    make_api_request()

# import requests

# def make_api_request():
#     url = "http://localhost:8000/api/get_valid_moves/"
    
#     # Input data in JSON format
#     input_data = {
#         "Queen": "H1",
#         "Bishop": "B7",
#         "Rook": "H8",
#         "Knight": "F3"
#     }
    
#     try:
#         response = requests.post(url, json=input_data)

#         print("Request JSON Data:")
#         print(input_data)
#         print("Response Status Code:", response.status_code)
#         print("Response JSON Data:")
#         print(response.json())

#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     make_api_request()