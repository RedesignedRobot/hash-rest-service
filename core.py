import bcrypt
import time
import platform
import socket
import ifaddr

from flask import Flask, Response, request, jsonify

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

execution_time = 0
start_time = 0
end_time = 0
rounds = 10


def get_hashed_password(text):
    global rounds
    return bcrypt.hashpw(text, bcrypt.gensalt(rounds))


def encode(s):
    return s.encode('utf-8')

def get_ip_list():
    adapters = ifaddr.get_adapters()
    ip_list = []
    for adapter in adapters:
        for ip in adapter.ips:
            x = str(ip.ip)
            if x.startswith('1'):
                ip_list.append(x)
    return ip_list

def build_response(plain_text, hashed_text):
    global rounds
    perf_monitor_stop()
    host_name = socket.gethostname()
    host_ips = get_ip_list()
    js = ({"hash": str(hashed_text),
           "plain_text": plain_text,
           "exec_time": str("{0:.2f}".format(execution_time)),
           "rounds": str(rounds),
           "platform":str(platform.platform()),
           "host_name": str(host_name),
           "host_ips": ', '.join(host_ips),
           "endpoint": str("http://IP_ADDR/hash?text="+plain_text+"&&rounds="+str(rounds)),
           })
    return js


def perf_monitor_reset():
    global start_time
    global end_time
    global execution_time
    start_time = 0
    end_time = 0
    execution_time = 0


def perf_monitor_start():
    global start_time
    perf_monitor_reset()
    start_time = time.time()


def perf_monitor_stop():
    global start_time
    global end_time
    global execution_time
    end_time = time.time()
    execution_time = end_time - start_time


@app.route('/hash')
def hash_endpoint():
    perf_monitor_start()
    global rounds
    rounds = request.args.get('rounds', default = 10, type = int)
    text = request.args.get('text', default = 'hello world', type = str)
    hashed_text = get_hashed_password(encode(text))
    package = build_response(text, hashed_text)
    return jsonify(package)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)
