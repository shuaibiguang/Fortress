import socket,psutil,pickle

class server():
    def main(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("",8001))
        s.listen(5)
        while True:
            con,add = s.accept()
            print(add)
            mass = con.recv(512).decode()
            print(mass)
            if mass == 'serverinfo':
                info = pickle.dumps(self.get_server_info())

            con.send(info)

    def get_server_info(self):
        # 1.cpu 2.net_io 3.mem
        return [psutil.cpu_percent(),psutil.net_io_counters(),psutil.virtual_memory()]

if __name__ == '__main__':
    ser = server()
    ser.main()
