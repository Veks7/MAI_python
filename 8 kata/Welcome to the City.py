'''
https://www.codewars.com//kata/5302d846be2a9189af0001e4
'''

def say_hello(name, city, state):
    return 'Hello, ' + ' '.join(name) + '! Welcome to ' + city + ', ' + state + '!';
print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))
print(say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois'))
print(say_hello(['Wallace','Russel','Osbourne'],'Albany','New York'))
print(say_hello(['Lupin','the','Third'],'Los Angeles','California'))
print(say_hello(['Marlo','Stanfield'],'Baltimore','Maryland'))
