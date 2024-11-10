from Crypto.Cipher import AES
import base64
import hashlib

# AES 대칭키를 생성 (128비트 키로 설정)
key = "shortkey12345678"  # 16바이트로 128비트 키 생성
key = key.encode('utf-8')  # 키를 바이트형으로 변환

# AES 암호화 클래스
class AESCipher:
    def __init__(self, key):
        self.key = key.zfill(32).encode()  # 32바이트 키로 패딩 (128비트 -> 256비트로 강제 패딩)

    def encrypt(self, raw):
        raw = raw.zfill(32)  # 32바이트로 패딩
        cipher = AES.new(self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw.encode())).decode()

    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return cipher.decrypt(base64.b64decode(enc)).decode().strip()

# 데이터 암호화 및 복호화
data = "고객만족도"

# 암호화
aes_cipher = AESCipher(key)
encrypted_data = aes_cipher.encrypt(data)
print("암호화된 데이터:", encrypted_data)

# 복호화
decrypted_data = aes_cipher.decrypt(encrypted_data)
print("복호화된 데이터:", decrypted_data)
