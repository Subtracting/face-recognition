from PIL import Image, ImageDraw
import face_recognition
import PIL
import math

image = face_recognition.load_image_file("nerd2.png")

face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        if facial_feature == 'left_eye':
            tip_coord = face_landmarks[facial_feature][1]
        if facial_feature == 'left_eye':
            bridge_coord = face_landmarks[facial_feature][4]
        if facial_feature == 'right_eye':
            tip_coord2 = face_landmarks[facial_feature][1]
        if facial_feature == 'right_eye':
            bridge_coord2 = face_landmarks[facial_feature][4]


x_pos = (bridge_coord[0]+tip_coord[0])//2
y_pos = (bridge_coord[1]+tip_coord[1])//2

x_pos2 = (bridge_coord2[0]+tip_coord2[0])//2
y_pos2 = (bridge_coord2[1]+tip_coord2[1])//2

new_height = int((bridge_coord[1]-tip_coord[1])*15)
new_height2 = int((bridge_coord2[1]-tip_coord2[1])*15)

rotation = 90

im1 = Image.open('vag.png')
width_1, height_1 = im1.size
new_width = int((new_height/height_1) * width_1)
new_width2 = int((new_height2/height_1) * width_1)
im1 = im1.resize((abs(new_width), abs(new_height)), Image.ANTIALIAS)

mask = Image.new('L', im1.size, 255)
im1 = im1.rotate(rotation, expand=True)
mask = mask.rotate(rotation, expand=True)

width, height = im1.size

pil_image.paste(im1, (x_pos-(width//2), y_pos-(height//2)), mask=im1)
pil_image.paste(im1, (x_pos2-(width//2), y_pos2-(height//2)), mask=im1)
pil_image.save('paste6.jpg', quality=95)
