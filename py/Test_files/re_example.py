import re
#name =raw_input("enter input")
name=" sdfg,jsdgf"
get_name = name.replace(" ","")
print len(get_name)

name_split= get_name.split(',')

if len(name_split[0]) == 1:
    print str(name_split[0]+name_split[1][0]+"*").upper()
elif len(name_split[0]) == 2:
    print str(name_split[0][0:2]+name_split[1][0]+"*").upper()
elif len(name_split[0]) >= 3:
    print str(name_split[0][0:3]+name_split[1][0]+"*").upper()
# elif len(get_name) > 4:
#     print str(get_name.split[0:3].upper()+"*")
    
# m = re.search(',', name)
# print m.group(1)