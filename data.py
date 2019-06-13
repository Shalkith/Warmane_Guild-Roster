
def Warmane():
    import requests
    url = "http://armory.warmane.com/api/guild/Born+On+A+Blood+Moon/Lordaeron/members"
    data1 = requests.get(url)
    data1 = data1.json()
    rosterlist = []
    for x in data1['roster']:
        rosterlist.append(x)
    return rosterlist

def Guildname():
    import requests
    url = "http://armory.warmane.com/api/guild/Born+On+A+Blood+Moon/Lordaeron/members"
    data2 = requests.get(url)
    data2 = data2.json()
    return data2['name']

def Articles():
    articles = [
        {
            'id':1,
            'title':'Article 1',
            'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author':'me',
            'create_date':'06-12-2019',
        },
        {
            'id':2,
            'title':'Article two',
            'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author':'someone else',
            'create_date':'06-12-2019',
        },
        {
            'id':3,
            'title':'Article three',
            'body':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author':'some third person',
            'create_date':'06-12-2019',
        }
    ]

    return articles
