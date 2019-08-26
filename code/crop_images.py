#! /usr/bin/python

from PIL import Image
import face_recognition
import sys
import os

def main():
    assert len(sys.argv) > 2, 'python crop_images <Images Dir Name> <Output Dir>'
    root_dir = sys.argv[1]
    output_dir = sys.argv[2]
    for parent, dirs, files in os.walk(root_dir):
        for file_name in files:
            image = face_recognition.load_image_file(os.path.join(parent, file_name))
            face_locations = face_recognition.face_locations(image)
            for i in range(len(face_locations)):
                face_location = face_locations[i]
                top, right, bottom, left = face_location
                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image).resize((128, 128), Image.ANTIALIAS)
                main_file_name, ext_file_name = os.path.splitext(file_name)
                pil_image.save(os.path.join(output_dir, main_file_name) + str(i) + ext_file_name)

if __name__ == '__main__':
    main()
