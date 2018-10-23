import binascii 
from Crypto.Cipher import AES
import base64
class decrypt:
	def unpad_string(self,value):
		a=None
		while value[-1] == '\x00':
			value = value[:-1]
		a=value
		value=None
    		return a
	
	def decryptaes(self,encrypted_text):
		print('Encrypted Text')
		print(encrypted_text)
		
		key= 'This is a key123'
		IV= 'This is an IV456'
		MODE = AES.MODE_CBC
		BLOCK_SIZE = 16
		SEGMENT_SIZE = 128 	
		encrypted_text=base64.b64decode(encrypted_text).encode('hex')
		print('Encrypted txt after B64 to hex' )
		print(encrypted_text)
		aes=AES.new(key, MODE, IV, segment_size=SEGMENT_SIZE)
		encrypted_text_bytes=binascii.a2b_hex(encrypted_text)
		print('Encrypted txt after a2b' )
		print(encrypted_text_bytes)
		decrypted_text=aes.decrypt(encrypted_text_bytes)
		print('DEC unpadded:' )
		print(decrypted_text)
		#decrypted_text=self.unpad_string(decrypted_text)
		encrypted_text=None
		encrypted_text_bytes=None
		aes=None

		return decrypted_text
	    
        
	