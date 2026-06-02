# get input
# utf encode
# get k0 to k3
# get k4 because (n-1 % 5 = 4)
# use key to decrypt hex

hex = input("hex: ")
encoded = bytes.fromhex(hex).decode('utf-8')

key = ""
# Get key by performing ( C_i XOR P_i )
for i in range(len(encoded)):
    plain_arr = ["T", "H", "M", "{", "}"]

    for i in range(4):
        key += chr(ord(encoded[i]) ^ ord(plain_arr[i%len(encoded)]))

    key += chr(ord(encoded[-1:]) ^ ord(plain_arr[-1]))

flag = ""
# XOR encoded string with repeated key
for i in range(len(encoded)):
    flag += chr(ord(encoded[i]) ^ ord(key[i%len(key)]))

print("key: " + key[:5])
print("flag: " + flag)