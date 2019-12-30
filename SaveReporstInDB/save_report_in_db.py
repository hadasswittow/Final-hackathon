import glob

from model import DB
from license_plate_detector import detect_license_plate
import os

license_number= 1234
db = DB()

images = r'images'
cropped_imgs = r'cropped'
path_to_directory = r'C:\Users\USER\PycharmProjects\hackathon2_flask'
imgs_path = os.path.join(path_to_directory, images)
cropped_imgs_path = os.path.join(path_to_directory, cropped_imgs)


def main_function():
    global license_number
    imgs_names = []
    for crp in os.listdir(cropped_imgs_path):
        imgs_names.append(crp)
    for img_name in imgs_names:
        # license_number = find_license_plate_number(os.path.join(cropped_imgs_path, img_name))
        license_number+=200
        _, date, time, area, _ = img_name.split('_')
        date = date.replace('-','/')
        time = time.replace('-',':')

        db.insert_report(license_number,date,time,os.path.join(imgs_path, img_name),area)

    delete_images_in_directories() #delete the images because they are now in the database
def find_license_plate_number(img_path):
    return detect_license_plate(img_path)

def delete_images_in_directories():
    pass
if __name__ == "__main__":
    main_function()
