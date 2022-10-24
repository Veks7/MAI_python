'''
https://www.codewars.com//kata/51f9d93b4095e0a7200001b8
'''
def how_many_light_sabers_do_you_own(name = "Zara"):
    if name == 'Zach':
        return 18
    else:
        return 0

print(how_many_light_sabers_do_you_own("Zach"), "==",18)
print(how_many_light_sabers_do_you_own(), "==", 0)
print(how_many_light_sabers_do_you_own("zach"), "==",0)
