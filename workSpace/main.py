from boot import relayOne, socket


def web_page():
  if relayOne.value() == 1:
    relayOne_state = "ON"
  else:
    relayOne_state = "OFF"
  
  html = """
  <html>
    <head>
      <title>Controle de Irrigação</title> 
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        body{font-family:Arial; text-align: center; margin: 0px auto; padding-top:30px;}
        .switch{position:relative;display:inline-block;width:120px;height:68px}.switch input{display:none}
        .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#ccc;border-radius:34px}
        .slider:before{position:absolute;content:"";height:52px;width:52px;left:8px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
        input:checked+.slider{background-color:#2196F3}
        input:checked+.slider:before{-webkit-transform:translateX(52px);-ms-transform:translateX(52px);transform:translateX(52px)}
      </style>
      <script>
        function toggleCheckbox(element) { 
          var xhr = new XMLHttpRequest(); 
          if(element.checked){ 
            xhr.open("GET", "/?relay=on", true); 
          }
          else { 
            xhr.open("GET", "/?relay=off", false); 
          } 
          xhr.send(); 
        }
      </script>
    </head>
    <body>
      <h1>Controle de Irrigação</h1>
      <label class="switch">
        <label>Relé 1</label>
        <input type="checkbox" onchange="toggleCheckbox(this)" %s>
        <span class="slider"></span>
      </label>
    </body>
  </html>""" % (relayOne_state)  
  return html
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)



while True:
  try:    
    if gc.mem_free() < 102000:
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    # print('Content = %s' % request)
    relayOne_on = request.find('/?relay=on')
    relayOne_off = request.find('/?relay=off')
    if relayOne_on == 6:
      print('RELAY ON')
      relayOne.on()
    if relayOne_off == 6:
      print('RELAY OFF')
      relayOne.off()
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html; charset=utf-8\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')


# from boot import releUm, socket


# def web_page():
#   if releUm.value() == 1:
#     releUm_state = "ON"
#   else:
#     releUm_state = "OFF"
  
#   html = """
#   <html>
#     <head> 
#       <title>Controle de Irrigação</title> 
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <link rel="icon" href="data:,"> 
#       <style>
#         html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
#         h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
#         border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
#         .button2{background-color: #4286f4;}
#       </style>
#     </head>
#     <body> 
#       <h1>Controle de Irrigação</h1> 
#       <p>Estado atual: <strong>""" + releUm_state + """</strong></p>
#       <p><a href="/?led=on"><button class="button">ON</button></a></p>
#       <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
#     </body>
#   </html>
#   """
#   return html
  
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('',80))
# s.listen(5)

# while True:
#   conn, addr = s.accept()
#   print('Got a connection from %s' % str(addr))
#   request = conn.recv(1024)
#   request = str(request)
#   print('Content = %s' % request)
#   led_on = request.find('/?led=on')
#   led_off = request.find('/?led=off')
#   print(led_on)
#   print(led_on)
#   if led_on == 6:
#     print('LED ON')
#     releUm.on()
#   if led_off == 6:
#     print('LED OFF')
#     releUm.off()

#   print(conn)
#   response = web_page()
#   conn.send('HTTP/1.1 200 OK\n')
#   conn.send('Content-Type: text/html; charset=utf-8\n')
#   conn.send('Connection: close\n\n')
#   conn.sendall(response)
#   conn.close()
  

