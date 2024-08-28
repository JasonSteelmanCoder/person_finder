import os
from dotenv import load_dotenv
import cv2
import shutil

load_dotenv()

archive_path = f'C:/Users/{os.getenv('USERNAME')}/Pictures/ath_photo_archive/Athens Photo Archive Files'

for root, dirs, files in os.walk(archive_path):
    for file in files:
        image = cv2.imread(os.path.join(root, file))
        if image is not None:
            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

            (humans, _) = hog.detectMultiScale(image, winStride=(10, 10), padding=(32, 32), scale=1.1)
            if len(humans) > 0:
                source_path = os.path.join(root, file)
                destination_folder = f"C:/Users/{os.getenv("USERNAME")}/Pictures/archive_of_people"
                destination_path = os.path.join(destination_folder, os.path.basename(source_path))
                shutil.copy(source_path, destination_path)
                print("copied!")