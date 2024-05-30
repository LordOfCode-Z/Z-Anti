import hashlib

def scan(file):
    #default virus found to false
    virus_found = False





    # open file and get hash
    with open(file,"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest();


    # SHA256 HASHES check + pack 1
    with open("SHA256-Hashes_pack.txt", 'r') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            if str(readable_hash) == str(line.split(";")[0]):
                virus_found = True
                f.close()
    f.close()
    # check if virus is found else pass
    if virus_found == True:
        print(file,"Dosyasında Virüs Tespit Edildi")
    else:
        print(file,"Dosyasında Virüs Tespit Edilemedi")
# the files will be scanned or what is the file we want to scan
scan(file.exe)