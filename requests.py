import requests

# Create a new person
data = {'name': 'John Doe'}
response = requests.post('http://127.0.0.1:5001/api', json=data)
print(response.json())

# Get details of a person by ID
person_id = 1  # Replace with an actual person ID
response = requests.get(f'http://127.0.0.1:5001/api/{person_id}')
print(response.json())

# Update a person by ID
updated_data = {'name': 'Updated Name'}
response = requests.put(f'http://127.0.0.1:5001/api/{person_id}', json=updated_data)
print(response.json())

# Delete a person by ID
response = requests.delete(f'http://127.0.0.1:5001/api/{person_id}')
print(response.json())
