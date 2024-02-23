from PIL import Image
image=Image.open('gh.png')
image.show()
info_dict = {
"Filename": image.filename,
"Image Size": image.size,
"Image Height": image.height,
"Image Width": image.width,
"Image Format": image.format,
"Image Mode": image.mode
}
for label,value in info_dict.items():
    print(label," ",value)