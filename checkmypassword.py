import requests
import hashlib
import sys

#creating connection wit API
def request_api(query):
  url = 'https://api.pwnedpasswords.com/range/'+query
  res = requests.get(url)
  if res.status_code!=200:
    raise RuntimeError(f'Error{res.status_code} while fetching the api please try again with correct API url.')
  return res

#counting the number of password breaches
def password_leak_count(hashes, hash_toCheck):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h ==hash_toCheck:
      return count
  return 0

#creating hash and passing it to function to check leaks
def Pwned_check(password):
  hashed_Password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5, tail = hashed_Password[:5],hashed_Password[5:]
  response = request_api(first5)
  return password_leak_count(response, tail)

def main(args):
  for password in args:
    count = Pwned_check(password)
    if count:
      print(f'{password}, has been breached {count} times, Please change your password.')
    else:
      print('Dont worry you are safe')
  return 'Ez Pz Lemon Squeeze'


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))


