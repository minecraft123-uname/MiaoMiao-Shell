from PIL import Image


mrp = Image.open("images/mrp.png")
for i in range(mrp.size[0]):
	for j in range(mrp.size[1]):
		raw = mrp.getpixel((i, j))
		new = tuple([raw[0], 255, raw[2], raw[3]])
		mrp.putpixel((i, j), new)
mrp.save("images/mrpRBkeep.png")