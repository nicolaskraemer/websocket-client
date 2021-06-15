import wss

if __name__ == "__main__":
    wss.enableTrace(True)
    ws = wss.create_connection("ws://echo.wss.org/")
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received '%s'" % result)
    ws.close()
