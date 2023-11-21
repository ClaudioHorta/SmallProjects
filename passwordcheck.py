import requests
import hashlib
import sys

# Function to make a request to the Pwned Passwords API with the given query character
def request_api_data(query_char):
    # Construct the API URL with the given query character
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # Make the API request
    res = requests.get(url)
    # Check if the request was successful (status code 200)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

# Function to parse the response from the Pwned Passwords API and get the count of password leaks
def get_password_leaks_count(hashes, hash_to_check):
    # Split the response into lines and then split each line into hash and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # Iterate through the hashes to find the count for the specified hash
    for h, count in hashes:
        if h == hash_to_check:
            return count
    # If the hash is not found, return 0
    return 0

# Function to check if a password has been compromised using the Pwned Passwords API
def pwned_api_check(password):
    # Transform the password to SHA1 hash
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split the SHA1 hash into first 5 characters and the rest
    first5_char, tail = sha1password[:5], sha1password[5:]
    # Make a request to the Pwned Passwords API with the first 5 characters of the hash
    response = request_api_data(first5_char)
    # Get the count of password leaks for the specified hash
    return get_password_leaks_count(response, tail)

# Main function that takes command-line arguments and checks each password
def main(args):
    # Iterate through each password provided as a command-line argument
    for password in args:
        # Check if the password has been compromised
        count = pwned_api_check(password)
        # Print the result based on the count
        if count:
            print(f'{password} was found {count} times... Probably you should change your password.')
        else:
            print(f'{password} was not found, Carry on!')
    # Return 'done!' when all passwords have been checked
    return 'done!'

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Exit the script after running the main function with command-line arguments
    sys.exit(main(sys.argv[1:]))

