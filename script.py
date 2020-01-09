filein = open('input.txt', 'r')
text = filein.read()
lines = text.split('\n')
sal = ''
add2 = ''
for line in lines:
    if 'Organization' in line:
        org = line[line.index('\t') + 1:]
    elif 'Salutation' in line:
        sal = line[line.index('\t') + 1:]
    elif 'Job Contact First Name' in line:
        first = line[line.index('\t') + 1:]
    elif 'Job Contact Last Name' in line:
        last = line[line.index('\t') + 1:]
    elif 'Address Line One' in line:
        add1 = line[line.index('\t') + 1:]
    elif 'Address Line Two' in line:
        add2 = line[line.index('\t') + 1:]
    elif 'City' in line:
        city = line[line.index('\t') + 1:]
    elif 'Province' in line:
        prov = line[line.index('\t') + 1:]
    elif 'Postal Code' in line:
        postal = line[line.index('\t') + 1:]
name = f'{first} {last}'
if sal != '':
    name = f'{sal} {first} {last}'
fileout = open('output.txt', 'w')
text = f'{name} \nHuman Resources Coordinator \n{org} \n{add1} {add2} \n{city} {prov} {postal}'
fileout.write(text)