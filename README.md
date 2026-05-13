# .lsafiledecrypter
# 🔓 Xiaomi MIUI Gallery — Secret Album Decryptor (.lsa / .lsav)

A simple Python script to decrypt hidden photos and videos from the **Xiaomi MIUI Gallery Secret Album**.  
When you hide files in MIUI Gallery, they get encrypted and saved as `.lsa` (photos) or `.lsav` (videos).  
This tool converts them back to regular `.jpg`, `.mp4`, or other viewable formats.

---

## 📱 What Are .lsa Files?

When you move a photo or video into the **Secret/Private Album** on a Xiaomi, Redmi, or POCO phone, MIUI encrypts the file and stores it at:

```
Internal Storage → MIUI → Gallery → cloud → secretAlbum
```

The files get renamed like:
```
IMG_20240218_161521.3e751332435bfad27569ca4efed1b602.lsa
VID_20240506_230636.3e751332435bfad27569ca4efed1b602.lsav
```

These files **cannot be opened normally** — this tool decrypts them back to their original format.

---

## ✅ Supported Devices & Versions

- Xiaomi, Redmi, POCO phones
- MIUI 12, MIUI 13, MIUI 14, HyperOS
- Works for both `.lsa` (photos) and `.lsav` (videos)

---

## 🛠️ Requirements

- Python 3.7 or higher
- Two Python libraries:

```bash
pip install pycryptodome filetype
```

---

## 📁 Setup

**1. Clone or download this repository**

```bash
git clone https://github.com/YOUR_USERNAME/miui-lsa-decryptor.git
cd miui-lsa-decryptor
```

**2. Install dependencies**

```bash
pip install pycryptodome filetype
```

**3. Copy your `.lsa` / `.lsav` files**

Connect your Xiaomi phone via USB and copy files from:
```
Internal Storage → MIUI → Gallery → cloud → secretAlbum
```

Paste them into the project folder or note the path.

---

## ▶️ Usage

**Decrypt a single file:**
```bash
python decrypt.py path\to\yourfile.lsa
```

**Decrypt an entire folder at once:**
```bash
python decrypt.py path\to\secretAlbum
```

**Example (Windows):**
```bash
python decrypt.py "C:\Users\YourName\Desktop\secretAlbum"
```

**Example (Linux / Mac):**
```bash
python decrypt.py /home/yourname/secretAlbum
```

The decrypted files are saved in the **same folder** with their correct extension (`.jpg`, `.mp4`, `.png`, etc.).

---

## 📂 Example Output

```
secretAlbum/
├── IMG_20240218.lsa              ← original encrypted file
├── IMG_20240218.jpg              ← ✅ decrypted photo
├── VID_20240506.lsav             ← original encrypted file
└── VID_20240506.mp4              ← ✅ decrypted video
```

---

## ⚙️ How It Works

MIUI Gallery encrypts files using **AES-128 in CTR mode** with:
- A fixed secret key derived from the first 16 bytes of the MIUI Gallery APK certificate
- A fixed initialization vector (IV)

For `.lsa` photo files — the entire file is encrypted.  
For `.lsav` video files — only the first 1024 bytes (header) are encrypted; the rest is plain data.

After decryption, the script auto-detects the real file type using the `filetype` library and saves it with the correct extension.

---

## ❓ FAQ

**Q: Will this work if my phone is broken / reset?**  
A: Yes! As long as you have the `.lsa` files, you can decrypt them on any PC.

**Q: Are my files safe?**  
A: Everything runs 100% locally on your computer. No files are uploaded anywhere.

**Q: What if the output file doesn't open?**  
A: Your file may use a different key version. The default key works for most MIUI versions where the key MD5 is `3e751332435bfad27569ca4efed1b602`.

**Q: Does it work on Mac and Linux?**  
A: Yes, the script is cross-platform.

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🙏 Credits

Encryption format research based on the open-source work by the MIUI community.  
Original decryption logic reference: [ObikBobik/miui-cloud-decryptor](https://github.com/ObikBobik/miui-cloud-decryptor)

---

## ⭐ If this helped you recover your photos, give it a star!
