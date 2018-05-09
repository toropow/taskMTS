import re

def check_ident(ident):
    if not re.match('^\d{5}-\d{5} \d$', ident):
        return False
    else:
         positions = range(10, 1, -1)
         pairs = zip(positions, [int(char) for char in ident.replace('-', '').replace(' ', '')])
         check_sum = sum([pow(value, 2, position) for position, value in pairs])
         print check_sum

    if check_sum > 10:
        check_sum %= 10

    print check_sum

    return check_sum == int(ident[-1:])

print(check_ident("98765-43219 9"))