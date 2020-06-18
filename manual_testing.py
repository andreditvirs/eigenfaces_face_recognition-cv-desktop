import numpy as np
import cv2
import sys
import os

RESIZE_FACTOR = 4

folder_path = 'D:\\Teknik Informatika\\CV\\Project Akhir\\'
testing_path = folder_path+'testing\\'
dataset_haar_path = folder_path+'dataset_haar\\'

class RecogEigenFaces:
    def __init__(self):
        cascPath = "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.out_dir = folder_path+'dataset_haar\\'
        self.face_name = sys.argv[1]
        self.model = cv2.face.EigenFaceRecognizer_create()
        self.face_names = []

    def list_dir(self):
        listds = os.listdir(dataset_haar_path)
        number_files = len(listds)
        os.chdir(dataset_haar_path)
        arr = os.listdir()
        return arr

    def load_trained_data(self):
        names = {}
        key = 0
        for (subdirs, dirs, files) in os.walk(self.out_dir):
            for subdir in dirs:
                names[key] = subdir
                key += 1
        self.names = names 
        self.model.read(folder_path+'eigen_trained_data.json')

    def compare_faces(self):
        index = 0
        for (subdirs, dirs, files) in os.walk(testing_path):
            for subdir in dirs:
                img_path = os.path.join(testing_path, self.face_name)
                for fn in os.listdir(img_path):
                    print("Testing untuk "+fn)
                    path = img_path + '/' + fn
                    frame = cv2.imread(path)
                    inImg = np.array(frame)
                    self.process_image(inImg)
                    print()
                index += 1
        return

    def process_image(self, inImg):
        resized_width, resized_height = (100, 100)
        gray = cv2.cvtColor(inImg, cv2.COLOR_BGR2GRAY)
        gray_resized = cv2.resize(gray, (int(gray.shape[1]/RESIZE_FACTOR), int(gray.shape[0]/RESIZE_FACTOR))) 
        faces = self.face_cascade.detectMultiScale(
                gray_resized,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )
        face_i = faces[0]
        x = face_i[0] * RESIZE_FACTOR
        y = face_i[1] * RESIZE_FACTOR
        w = face_i[2] * RESIZE_FACTOR
        h = face_i[3] * RESIZE_FACTOR
        face = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (resized_width, resized_height))
        confidence = self.model.predict(face_resized)
        arr = {}
        arr = self.list_dir()
        for i in range(len(arr)):
            if i == confidence[0]:
                print("-> Tertebak "+arr[i]+" (benar)")
            else:
                print("Bukan "+arr[i]+" (salah)")
        return


if __name__ == '__main__':
    recognizer = RecogEigenFaces()
    recognizer.load_trained_data()
    recognizer.compare_faces()
    print ("Tekan 'q' untuk mengakhiri program")

