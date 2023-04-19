import base64 

def encode_base64():
	message = input("[*]enter what you want to encode : ")
	ascii_msg = message.encode('ascii')
	bytes = base64.b64encode(ascii_msg)
	msg_base64 = bytes.decode('ascii')
	print("[*]",msg_base64)

def decode_base64():
	message = input("[*]enter what you wantt to decode :")
	encode_msg = message.encode('ascii')
	bytes = base64.b64decode(encode_msg)
	final_msg = bytes.decode('ascii')
	print("[*]",final_msg)

print("#base64 decode = a")
print("#base64 encode = b")  

c = input("enter what you want :  ")

if c == "a":
	decode_base64()
elif c == "b": 
	encode_base64()

else:
	print ("***bad enter***")
