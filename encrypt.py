import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Şifreleme işlemi
def encrypt_file(file_path, key):
    key = key.ljust(32)[:32].encode('utf-8')  # AES-256 için 32 byte anahtar
    iv = os.urandom(16)  # Rastgele Initialization Vector (IV)

    with open(file_path, 'rb') as f:
        data = f.read()

    # Veriyi pad et
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Veriyi şifrele
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Şifrelenmiş veriyi aynı dosyaya yaz
    with open(file_path, 'wb') as f:
        f.write(iv + encrypted_data)

# Klasör ve alt klasörlerindeki tüm dosyaları şifreleme
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Şifreleniyor: {file_path}")
            encrypt_file(file_path, key)

if __name__ == "__main__":
    # Burada şifrelenecek klasörler tanımlanıyor
    folders_to_encrypt = [
        "/home/user/OrnekKlasor1",  # İlk klasör yolu
        "/home/user/OrnekKlasor2"   # İkinci klasör yolu
    ]

    # Şifreleme anahtarı
    key = input("Şifreleme anahtarını girin: ").strip()

    # Belirlenen klasörleri şifrele
    for folder_path in folders_to_encrypt:
        if os.path.isdir(folder_path):
            print(f"Klasör işleniyor: {folder_path}")
            encrypt_folder(folder_path, key)
        else:
            print(f"Hata: {folder_path} klasör yolu geçerli değil!")

    print("Tüm klasörler başarıyla şifrelendi.")