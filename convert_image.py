from PIL import Image
import download_image

debug=1
base_img = download_image.get_image()
# base_img = Image.open('most_recent_img.png')
if debug: base_img.show()
size = base_img.size
color_rounded_img = Image.new('RGB',size)
round_sensitivity = 64*2

for x in range(size[0]):
    print('rounding colors...', 100 * x/size[0], '% complete', ' '*5, end='\r')
    for y in range(size[1]):
        rgb = [i // round_sensitivity * round_sensitivity for i in base_img.getpixel((x,y))]
        color_rounded_img.putpixel((x,y),tuple(rgb))

if debug:color_rounded_img.show()

line_size=2
lined_img = Image.new('RGB',size)
# this takes.. a while
for x in range(size[0]):
    print('adding lines...', 100 * x/size[0], '% complete', ' '*5, end='\r')
    for y in range(size[1]):
        rgb = color_rounded_img.getpixel((x,y))
        color = 255
        # for xx in range(line_size):
            # for yy in range(line_size):
        for xx in [-1,1]:
            for yy in [-1,1]:
                xxx = x+xx*line_size
                yyy = y+yy*line_size
                if xxx >= size[0]: xxx=size[0] - 1
                elif xxx <= 0: xxx=0
                if yyy >= size[1]: yyy=size[1] - 1
                elif yyy <= 0: yyy=0
                if color_rounded_img.getpixel((xxx,yyy)) != rgb:
                    color = 0
                    break
            if not color:
                break
        lined_img.putpixel((x,y),(color,color,color))

if debug: lined_img.show()
