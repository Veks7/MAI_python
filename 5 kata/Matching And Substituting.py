'''
https://www.codewars.com/kata/59de1e2fe50813a046000124/train/python
'''
def check_validity_version(version):
    if version.count('.') != 1 or version.find('.') == 0:
        return False
    for el in version:
        if not(el.isdigit or el == '.'):
            return False
    return True


def check_validity_phone(phone):
    if len(phone) != 15:
        return False
    if phone[0:3] != '+1-' or phone[6] != '-' or phone[10] != '-':
        return False
    if not(phone[3:6].isdigit()) or not(phone[7:10].isdigit()) or not(phone[11:15].isdigit()):
        return False
    return True


def change(s, prog, version):
    date = 'Date: 2019-01-01'
    author = 'Author: g964'
    program_title = 'Program:'
    
    l = s.split('\n')
    l[0] = program_title + ' ' + prog
    l[1] = author
    l[3] = l[3].split(' ')
    l[4] = date
    l[5] = l[5].split(' ')
    if not(check_validity_version(l[5][1])) or not(check_validity_phone(l[3][1])):
        return 'ERROR: VERSION or PHONE'
    l[3][1] = "+1-503-555-0090"
    if l[5][1] != '2.0':
        l[5][1] = version
    l[3] = ' '.join(l[3])
    l[5] = ' '.join(l[5])
    l.pop(6)
    l.pop(2)
    
    return ' '.join(l)
