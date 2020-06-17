import numpy as np
import cv2
import sys
import os

RESIZE_FACTOR = 4

folder_path = 'D:\\Teknik Informatika\\CV\\Project Akhir\\'

class RecogEigenFaces:
    def __init__(self):
        cascPath = "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.face_dir = folder_path+'dataset_haar\\'
        self.video_file=sys.argv[1]
        self.model = cv2.face.EigenFaceRecognizer_create()
        self.face_names = []

    def load_trained_data(self):
        names = {}
        key = 0
        for (subdirs, dirs, files) in os.walk(self.face_dir):
            for subdir in dirs:
                names[key] = subdir
                key += 1
        self.names = names 
        self.model.read(folder_path+'eigen_trained_data.json')

    def show_video(self):
        video_capture = cv2.VideoCapture(self.video_file)
        frame_width = int(video_capture.get(3))
        frame_height = int(video_capture.get(4))
        out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        while True:
            ret, frame = video_capture.read()
            if ret == True:
                inImg = np.array(frame)
                outImg, self.face_names = self.process_image(inImg)
                cv2.imshow('Face Recognition', outImg)
                out.write(outImg)

                # Jika selesai tekan 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    video_capture.release()
                    out.release()
                    cv2.destroyAllWindows()
                    return
            else:
                return

    def process_image(self, inImg):
        frame = cv2.flip(inImg, 1)
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
        persons = []
        for i in range(len(faces)):
            face_i = faces[i]
            x = face_i[0] * RESIZE_FACTOR
            y = face_i[1] * RESIZE_FACTOR
            w = face_i[2] * RESIZE_FACTOR
            h = face_i[3] * RESIZE_FACTOR
            face = gray[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (resized_width, resized_height))
            confidence = self.model.predict(face_resized)
            if confidence[1]<3500:
                person = self.names[confidence[0]]
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
                cv2.putText(frame, '%s - %.0f' % (person, confidence[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            else:
                person = 'Tidak Dikenal'
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(frame, person, (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            persons.append(person)
        return (frame, persons)


if __name__ == '__main__':
    recognizer = RecogEigenFaces()
    recognizer.load_trained_data()
    print ("Tekan 'q' untuk mengakhiri program")
    recognizer.show_video()

