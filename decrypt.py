import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Deşifreleme işlemi
def decrypt_file(file_path, key):
    key = key.ljust(32)[:32].encode('utf-8')

    with open(file_path, 'rb') as f:
        data = f.read()

    iv = data[:16]  # İlk 16 byte IV
    encrypted_data = data[16:]  # Şifrelenmiş veri

    # Veriyi deşifre et
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Pad kaldır
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    # Deşifre edilmiş veriyi aynı dosyaya yaz
    with open(file_path, 'wb') as f:
        f.write(data)

# Klasör ve alt klasörlerindeki tüm dosyaları deşifreleme
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Deşifre ediliyor: {file_path}")
            decrypt_file(file_path, key)

if __name__ == "__main__":
    # Burada deşifrelenecek klasörler tanımlanıyor
    folders_to_decrypt = [
        "/home/user/OrnekKlasor1",  # İlk klasör yolu
        "/home/user/OrnekKlasor2"   # İkinci klasör yolu
    ]

    # Deşifreleme anahtarı
    key = input("Deşifreleme anahtarını girin: ").strip()

    # Belirlenen klasörleri deşifre et
    for folder_path in folders_to_decrypt:
        if os.path.isdir(folder_path):
            print(f"Klasör işleniyor: {folder_path}")
            decrypt_folder(folder_path, key)
        else:
            print(f"Hata: {folder_path} klasör yolu geçerli değil!")

    print("Tüm klasörler başarıyla deşifre edildi.")