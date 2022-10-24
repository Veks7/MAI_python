'''
https://www.codewars.com//kata/54147087d5c2ebe4f1000805
'''
def _if(bool, func1, func2):
    if bool == True:
        return func1()
    else:
        return func2()
  
def a1():
    a = True
    print(True)
      
def a2():
    print(False, "Should respond to True correctly")
        
def b1():
    
    print(False, "Should support falsy/truthy values")
        
def b2():
    b = False
    print(False)
        
def c1():
    c = True
    print(True)
        
def c2():
    print(False, "Should support falsy/truthy values")
        
def d1():
    d = True
    print(True)
        
def d2():
    print(False, "Should support comparison")
        
def e1():
    e = True
    print(True)
         
def e2():
    print(False, "Should support comparison")
    
_if(True, a1, a2)
_if(False, b1, b2)
_if(1, c1, c2)
_if((3 < 4), d1, d2)
_if((9 % 3 == 0), e1, e2)
        

