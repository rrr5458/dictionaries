ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][0]['interests'][1])
 # functin to add new key "friend count", will count number of friends and add
def friends_count(dictionary):
  #creaters a new key : value in a dictionary. Value is the length of friends, counts how many friends
  dictionary["friend count"] = len(dictionary['friends'])
  return dictionary

print(friends_count(ramit))




