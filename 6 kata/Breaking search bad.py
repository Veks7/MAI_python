'''
https://www.codewars.com/kata/52cd53948d673a6e66000576/train/python
'''
def search(titles, term):
    return [title for title in titles if title.lower().find(term) >= 0]
