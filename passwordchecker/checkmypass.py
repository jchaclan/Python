import requests 
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error feching: {res.status_code} check the API and try again')
    return res

def convert_to_sha1(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(f'sha1password: {sha1password}')
    return sha1password

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        #print(f'Hash to check {hash_to_check} Working with hash: {hash} which has {count} entries')
        if hash == hash_to_check:
            print('FOUNDDDDDDDDDDDDDD')
            return count
    return 0

def check_password(sha1_password):
    first5characters = sha1_password[:5]
    response = request_api_data(first5characters)
    print(response)
    return response

def main(args):
    for password in args:
        sha1_password = convert_to_sha1(password)
        print(f'sha1_password:{sha1_password}')
        hashes = check_password(sha1_password)
        count = get_password_leaks_count(hashes,sha1_password[5:])
        if count:
            print(f'The password {password} was found {count} times')
        else:
            print(f'Password {password} is SECURE, it was not found')

main(sys.argv[1:])