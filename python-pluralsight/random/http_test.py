# From Python 3 Fundamentals by Sarah Holderness
import requests, json
# Returns -1 if failed and prints whatever info, otherwise the number of people
# Note there is a "number of people" attribute in the json, coded as if there wasn't
# Requires internet connecetion to do request.
def space_people() -> int:
    r = requests.get('http://api.open-notify.org/astros.json')
    if not r.ok:
        print("Request didn't go through. Status code:",r.status_code)
        return -1
    data = r.json()
    for person in data['people']:
        print(person['name'])
    return len(data['people'])

if __name__ == '__main__':
    print(f'Amount of people: {space_people()}')