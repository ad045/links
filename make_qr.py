"""Generate the poster QR code (SVG for print, PNG for slides)."""

import segno

URL = "https://ad045.github.io/links/"

qr = segno.make(URL, error="h")  # 30% redundancy: survives poster print + glare
qr.save("qr.svg", scale=10, border=2, dark="#16181d")
qr.save("qr.png", scale=40, border=2, dark="#16181d")  # ~4000 px, plenty for A0

if __name__ == "__main__":
    assert segno.make(URL, error="h").matrix, "empty QR matrix"
    print(f"wrote qr.svg + qr.png for {URL}")
