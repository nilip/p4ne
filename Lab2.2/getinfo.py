from flask import Flask, jsonify
import re
import glob

app=Flask(__name__)
l=[]
ip_addresses={}
current_hostname=''

@app.route('/')
def hello():
    return "Это веб-сервер с REST API <br> " \
            "─╔══╦═══╦════╗ <br>" \
            "─╚╗╔╣╔══╩═╗╔═╝ <br>" \
            "──║║║╚══╗─║║ <br>" \
            "╔╗║║║╔══╝─║║ <br>" \
            "║╚╝╚╣╚══╗─║║ <br>" \
            "╚═══╩═══╝─╚╝ <br>"
@app.route('/configs')
def configs():
        return jsonify(l)
@app.route('/config/hostname')
def host():
    return jsonify(ip_addresses)
@app.route('/config/<x>')
def func1(x):
    return jsonify(ip_addresses[x])

file_list = glob.glob("C:\\Users\ilinpp\Seafile\p4ne_training\config_files\\*.txt")
for f in file_list:
    with open(f) as current_file:
        for line in current_file:
            m = re.search("^hostname (.+)$", line)
            if m:
                l.append(m.group(1))

file_list=glob.glob("C:\\Users\ilinpp\Seafile\p4ne_training\config_files\\*.txt")
for f in file_list:
    with open(f) as current_file:
        for line in current_file:
            m = re.search("^hostname (.+)$", line)
            if m:
                current_hostname = str(m.group(1))
                ip_addresses[current_hostname] = []

            f = re.search("ip address ((?:[0-9]{1,3}[.]?){4}) ((?:[0-9]{1,3}[.]?){4})$", line)
            if f:
                ip_addresses[current_hostname].append(str(f.group(1)))

if __name__ == '__main__':
           app.run(debug=True)

