# Base64 alphabet
B64_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def kx(text, key="rev"):
    out = []
    for i, ch in enumerate(text):
        out.append(chr(ord(ch) ^ ord(key[i % len(key)])))
    return "".join(out)

def rol3(text):
    out = []
    for ch in text:
        b = ord(ch)
        rotated = ((b << 3) & 0xFF) | (b >> 5)
        out.append(chr(rotated))
    return "".join(out)

def tb64(text):
    bits = "".join(f"{ord(c):08b}" for c in text)
    while len(bits) % 6 != 0:
        bits += "0"
    out = ""
    for i in range(0, len(bits), 6):
        chunk = bits[i:i+6]
        val = int(chunk, 2)
        out += B64_ALPH[val]
    while len(out) % 4 != 0:
        out += "="
    return out

def z(text):
    return text[::-1]


def main():
    try:
        with open("flag.txt", "r") as f:
            blob = f.read().strip()
            if not blob:
                print("flag.txt is empty")
                return
    except FileNotFoundError:
        print("flag.txt not found. Put the encoded blob (one line) into flag.txt")
        return

    
    step1 = kx(blob)
    step2 = rol3(step1)
    step3 = tb64(step2)
    step4 = z(step3)

    print("Final encoded flag:", step4)

if __name__ == "__main__":
    main()
