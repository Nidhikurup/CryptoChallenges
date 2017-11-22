import base64

def sxor(a,b):
    return ''.join(chr(ord(x) ^ ord(y)) for x,y in zip(a,b))

hex_string = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"
hex_data = hex_string.decode("hex")
hex_data1 = str2.decode("hex")
print sxor(hex_data,hex_data1).encode("hex")
