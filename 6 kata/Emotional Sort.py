'''
https://www.codewars.com/kata/5a86073fb17101e453000258/train/python
'''
d = { ':D' : 'const_emo_1',  # super happy
':)' : 'const_emo_2',  # happy
':|' : 'const_emo_3', # normal
':(' : 'const_emo_4', # sad
'T_T' : 'const_emo_5' # super sad
     }

d_rev = { 'const_emo_1' : ':D', # super happy
'const_emo_2' : ':)', # happy
'const_emo_3' : ':|', # normal
'const_emo_4' : ':(', # sad
'const_emo_5' : 'T_T' # super sad
     }

def sort_emotions(arr, order):
    data = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] in d:
            data[i] = d.get(arr[i])
    data.sort()
    for i in range(len(data)):
        if data[i] in d_rev:
            data[i] = d_rev.get(data[i])
    if not order:
        data.reverse()
    return data
