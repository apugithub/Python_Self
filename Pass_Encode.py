import base64

a = base64.b64encode(b'password')  # Encoding the pass but check the output, format is (b<'password'>)
b = base64.b64decode(b'cGFzc3dvcmQ=')  # Decoding the pass, check the output, additional b is coming in front

print (a)
print(b)

secret = b.decode('utf-8')

print(secret)



