from PIL import Image

### Open the indexed bitmap
img = Image.open("indexed.bmp")

### Read the palette...
pal = img.getpalette()
if (len(pal) != 768):
  print("ERROR: expect 256 RGB values for palette (768 bytes), got ", len(pal))
  exit(-1)

### Read the pixels...
pixels = img.getdata()
if (len(pixels) != (640*480)):
  print("ERROR: expected 640x480=307200 pixels, got ", len(pixels))
  exit(-1)

print("[OK] Palette and pixel data match expected size")
print("[INFO] Generating lookup tables...")

### Write the bg LUT
with open("palette_lut.v", "w") as file:
  file.write("reg [23:0] pal_rgb;\n")
  file.write("always @(posedge clk_50) begin\n")
  file.write("  case(bg_pix)\n")
  for i in range(256):
    file.write("    8'd%d : pal_rgb <= 24'h%02x%02x%02x;\n" % (i, pal[i*3], pal[(i*3) + 1], pal[(i*3) + 2]));
  file.write("  endcase\n")
  file.write("end\n")

### Write the bg pixdata.
print("[INFO] Generating background pixel data...")
with open("background.bin", "wb") as file:
  file.write(img.tobytes())

