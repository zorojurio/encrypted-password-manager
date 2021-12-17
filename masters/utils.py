from Crypto.Cipher import AES


def encrypt_master_password(password):
    # 32 byte key is needed thats why encoding
    key32 = "{: <32}".format(password).encode("utf-8")
    text = "{: <32}".format(password).encode("utf-8")
    obj = AES.new(key32, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(text)
    return ciphertext


def encrypt_platform_password(password, platform_password):
    # 32 byte key is needed thats why encoding
    key32 = "{: <32}".format(password).encode("utf-8")
    platform_password = "{: <32}".format(platform_password).encode("utf-8")
    obj = AES.new(key32, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(platform_password)
    return ciphertext


def decrypt_password(password, encrypted_message):
    key32 = "{: <32}".format(password).encode("utf-8")
    obj = AES.new(key32, AES.MODE_CBC, 'This is an IV456')
    decrupted = obj.decrypt(encrypted_message)
    return decrupted.decode("utf-8")
