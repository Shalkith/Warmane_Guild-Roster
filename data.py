
def Warmane():
    import requests
    url = "http://armory.warmane.com/api/guild/Born+On+A+Blood+Moon/Lordaeron/members"
    data = requests.get(url)
    data = data.json()
    rosterlist = []
    fakelist =[
        {
            'name': 'Kassie',
            'online': False,
            'level': '80',
            'gender': 'Female',
            'race': 'Draenei',
            'racemask': 1024,
            'class': 'Priest',
            'classmask': 16,
            'achievementpoints': '4260',
            'professions': {'professions': [{'name': 'Tailoring', 'skill': '450'}, {'name': 'Enchanting', 'skill': '450'}]}},
        {'name': 'Sylphia', 'online': False, 'level': '80', 'gender': 'Female', 'race': 'Night Elf', 'racemask': 8, 'class': 'Druid', 'classmask': 1024, 'achievementpoints': '4040', 'professions': {'professions': [{'name': 'Leatherworking', 'skill': '450'}, {'name': 'Herbalism', 'skill': '450'}]}},
        {'name': 'Fannypac', 'online': False, 'level': '5', 'gender': 'Female', 'race': 'Dwarf', 'racemask': 4, 'class': 'Rogue', 'classmask': 8, 'achievementpoints': '20', 'professions': []}
    ]
    for x in data['roster']:
        rosterlist.append(x)
    return rosterlist

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
