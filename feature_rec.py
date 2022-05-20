from PIL import Image, ImageDraw
import face_recognition
import PIL
import math

image = face_recognition.load_image_file("base.jpeg")

face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        if facial_feature == 'nose_tip':
            tip_coord = face_landmarks[facial_feature][2]
        if facial_feature == 'nose_bridge':
            bridge_coord = face_landmarks[facial_feature][0]

    x_pos = (bridge_coord[0]+tip_coord[0])//2
    y_pos = (bridge_coord[1]+tip_coord[1])//2

    new_height = int((bridge_coord[1]-tip_coord[1])*2)

    rotation = math.degrees(
        math.atan((bridge_coord[0]-tip_coord[0])/(bridge_coord[1]-tip_coord[1]))) % 360

    im1 = Image.open('add.png')
    width_1, height_1 = im1.size
    new_width = int((new_height/height_1) * width_1)
    im1 = im1.resize((abs(new_width), abs(new_height)), Image.ANTIALIAS)

    mask = Image.new('L', im1.size, 255)
    im1 = im1.rotate(rotation, expand=True)
    mask = mask.rotate(rotation, expand=True)

    width, height = im1.size

    pil_image.paste(im1, (x_pos-(width//2), y_pos-(height//2)), mask=im1)
pil_image.save('result.jpg', quality=95)
