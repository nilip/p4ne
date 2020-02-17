import glob
string_list=[]
file_list=glob.glob("C:\\Users\ilinpp\Seafile\p4ne_training\config_files\\*.txt")
for f in file_list:
    with open(f) as current_file:
        for line in current_file:
            if line.find('ip address')!=-1:
                line2=line.replace('ip address','').replace('dhcp','').replace('match  prefix-list bogons','').replace('no','').replace('match  prefix-list ROTEKS','').strip()
                string_list.append(line2)

list1=list(set(string_list))
del list1[0]
for x in list1:
    print(x)


