import os
import sys
import filetype
from Crypto.Cipher import AES
from Crypto.Util import Counter

sAesIv = 22696201676385068962342234041843478898
secretKey = b'0\x82\x04l0\x82\x03T\xa0\x03\x02\x01\x02\x02\t\x00'

def make_aes():
    counter = Counter.new(128, initial_value=sAesIv)
    return AES.new(secretKey, mode=AES.MODE_CTR, counter=counter)

def decrypt_lsa(filepath):
    with open(filepath, 'rb') as f:
        return make_aes().decrypt(f.read())

def decrypt_lsav(filepath):
    size = os.path.getsize(filepath)
    header_size = max(min(1024, size), 16)
    with open(filepath, 'rb') as f:
        header = make_aes().decrypt(f.read(header_size))
        remainder = f.read()
    return header + remainder

def decrypt_file(filepath):
    ext = filepath.rsplit('.', 1)[-1].lower()
    if ext == 'lsa':
        return decrypt_lsa(filepath)
    elif ext == 'lsav':
        return decrypt_lsav(filepath)
    else:
        return None

def save_decrypted(data, input_path):
    base = os.path.splitext(input_path)[0]
    guessed_ext = filetype.guess_extension(data[:1024]) or 'bin'
    out_path = f"{base}.{guessed_ext}"
    with open(out_path, 'wb') as f:
        f.write(data)
    print(f"Saved: {out_path}")

def process(path):
    if os.path.isdir(path):
        for fname in os.listdir(path):
            fpath = os.path.join(path, fname)
            data = decrypt_file(fpath)
            if data:
                save_decrypted(data, fpath)
    elif os.path.isfile(path):
        data = decrypt_file(path)
        if data:
            save_decrypted(data, path)
        else:
            print("File must be .lsa or .lsav")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        process(sys.argv[1])
    else:
        print("Usage: python decrypt.py <file or folder>")