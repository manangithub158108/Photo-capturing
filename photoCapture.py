# importing the modules
import cv2;
import dropbox;
import time;
import random;

start_program_time = int(time.time());

def take_snapshot():
    num = random.randint(1, 100);

    # intializing the camera vision
    cameraVision = cv2.VideoCapture(0);

    while True:
        
        # read the frames while the camera is on
        ret, frames = cameraVision.read();

        # cv2.imwrite
        image_name = 'image' + str(num) + '.png';
        image_file = cv2.imwrite(image_name, frames);

        # break the while loop
        break

    return image_name;

    print('Snapshot taken successfully');

    cameraVision.realease();
    cv2.destroyAllWindows();


def upload_files(image_name):

    key = "n0UclT7uos4AAAAAAAAAAdiWin20w96MzwrJ2xoIw8z3IJ66mvUvRm6FGmoFiWC0";
    file_from = image_name;
    file_to = "/photos/" + str(file_from);

    dbx = dropbox.Dropbox(key);

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to);

    print('Image uploaded successfully');

def main():
    while True:
        if ((time.time() - start_program_time) >= 10):
            name = take_snapshot();
            upload_photo = upload_files(name);

main();



