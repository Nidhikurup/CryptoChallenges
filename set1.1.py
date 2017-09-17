import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hex_data = hex_string.decode("hex")
print hex_data
print base64.b64encode(hex_data)

