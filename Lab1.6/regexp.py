import ipaddress
import re
import glob
file_list=glob.glob("C:\\Users\ilinpp\Seafile\p4ne_training\config_files\\*.txt")
for f in file_list:
    with open(f) as current_file:
        for line in current_file:
            m = re.search("ip address ((?:[0-9]{1,3}[.]?){4}) ((?:[0-9]{1,3}[.]?){4})$", line)
            if m:
                print("IP:", m.group(1))
                print("MASK", m.group(2))
            m = re.search("^hostname (.+)$", line)
            if m:
                print("Host: ", m.group(1))

