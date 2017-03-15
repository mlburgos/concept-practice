import socket

CRLF = '\r\n'

response = """HTTP/1.1 200 OK!!!! 
headers: junk

body! COUNT
""".replace('\n', CRLF)

# server
s = socket.socket()

# for socket reuse
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

s.bind(('127.0.0.1', 10000))

s.listen(0)

count = 0

while True:
    conn, addr = s.accept()
    count += 1

    # monicabsmacbook:~ monicaburgos$ nc 127.0.0.1 10000
    # hi!
    buf = ""

    while True:    
        data = conn.recv(5)
        buf += data

        if CRLF*2 in buf:
           
            print buf
            # i = data.index(CRLF*2)
            # buf += buf[:i]
            break 

            # better to use done as a boolean instead of a break

    r = response.replace("COUNT", str(count))
    conn.send(r)
    conn.close()



