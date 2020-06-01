import numpy as np
import cv2
import sys
import os

RESIZE_FACTOR = 4

folder_path = 'D:\\Teknik Informatika\\CV\\Project Akhir\\'
in_path = folder_path+'dataset\\'
out_path = folder_path+'dataset_haar\\'
listds = os.listdir(in_path)
number_files = len(listds)
os.chdir(in_path)
arr = os.listdir()

class TrainEigenFaces:
    def __init__(self):
        print("Dataset = " + in_path)
        print("Jumlah file dataset = " + str(number_files))
        # Looping untuk DATASET
        self.face_cascade = cv2.CascadeClassifier(folder_path+'haarcascade_frontalface_default.xml')
        self.model = cv2.face.EigenFaceRecognizer_create()

    def capture_training_images(self):
        while True:
            for (subdirs, dirs, files) in os.walk(in_path):
                for subdir in dirs:
                    img_path = os.path.join(in_path, subdir)
                    img_no=1
                    resized_width, resized_height = (112, 92)  
                    for img_name in os.listdir(img_path):
                        img_file = img_path+'/'+img_name
                        image = cv2.imread(img_file)
                        self.process_image(np.array(image), subdir, img_no)
                        img_no+=1
                return

    def process_image(self, inImg, path, img_no):
        frame = cv2.flip(inImg,1)
        resized_width, resized_height = (100, 100)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        gray_resized = cv2.resize(gray, (int(gray.shape[1]/RESIZE_FACTOR), int(gray.shape[0]/RESIZE_FACTOR)))        
        faces = self.face_cascade.detectMultiScale(
        gray_resized,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if len(faces) > 0:
            areas = []
            for (x, y, w, h) in faces: 
                areas.append(w*h)
                max_area, idx = max([(val,idx) for idx,val in enumerate(areas)])
                face_sel = faces[idx]
            
                x = face_sel[0] * RESIZE_FACTOR
                y = face_sel[1] * RESIZE_FACTOR
                w = face_sel[2] * RESIZE_FACTOR
                h = face_sel[3] * RESIZE_FACTOR

                face = gray[y:y+h, x:x+w]
                face_resized = cv2.resize(face, (resized_width, resized_height))

                cv2.imwrite('%s/%s.png' % (out_path+path, img_no), face_resized)
                print("Dataset : ", path, img_no)
            # print("Training data ini berhasil. Tekan 'q' untuk berhenti disini")
        return frame

    def eigen_train_data(self):
        imgs = []
        tags = []
        index = 0
        for (subdirs, dirs, files) in os.walk(out_path):
            for subdir in dirs:
                img_path = os.path.join(out_path, subdir)
                for fn in os.listdir(img_path):
                    path = img_path + '/' + fn
                    tag = index
                    imgs.append(cv2.imread(path, 0))
                    tags.append(int(tag))
                index += 1
        (imgs, tags) = [np.array(item) for item in [imgs, tags]]
        
        self.model.train(imgs, tags)
        self.model.save(folder_path+'eigen_trained_data.xml')
        print("Training Dataset Selesai")
        return

if __name__ == '__main__':
    trainer = TrainEigenFaces()
    trainer.capture_training_images()
    trainer.eigen_train_data()
    print("Tekan 'q' untuk mengakhiri program")