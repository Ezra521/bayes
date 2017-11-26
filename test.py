

people = {
    'Alice':{
        'phone':'2341',
        'addr':' foo drive 23'
    },
    'Franke': {
        'phone': '1321',
        'addr': ' fee drive 10'
    },
    'Jane': {
        'phone': '9341',
        'addr': ' fo drive 56'
    },
    'Rose': {
        'phone': '0361',
        'addr': ' foo drive 87'
    }
}
lables = {
    'phone':'phone number',
    'addr' :'address'
}

name = input('NAME: ')

request = input('Phone number (p) or adrress (a)?')

if request == 'p':key = 'phone'
if request == 'a':key = 'addr'

if name in people :print("%s's %s is %s." % (name,lables[key],people[name][key]))

