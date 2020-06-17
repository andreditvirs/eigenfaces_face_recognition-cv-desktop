import numpy as np
import cv2
import sys
import os

FREQ_DIV = 150   #frequency divider for capturing training images
RESIZE_FACTOR = 4
NUM_TRAINING = 3

class TrainEigenFaces:
    def __init__(self):
        cascPath = "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.face_dir = 'testing'
        self.face_name = 'andre'
        self.path = os.path.join(self.face_dir, self.face_name)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        self.model = cv2.face.EigenFaceRecognizer_create()
        self.count_captures = 0
        self.count_timer = 0

    def capture_training_images(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            self.count_timer += 1
            ret, frame = video_capture.read()
            inImg = np.array(frame)
            outImg = self.process_image(inImg)
            cv2.imshow('Video', outImg)

            # When everything is done, release the capture on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_capture.release()
                cv2.destroyAllWindows()
                return

    def process_image(self, inImg):
        frame = cv2.flip(inImg,1)
        resized_width, resized_height = (100, 100)        
        if self.count_captures < NUM_TRAINING:
            color = cv2.cvtColor(frame, 0) 
            color_resized = cv2.resize(color, (int(color.shape[1]/RESIZE_FACTOR), int(color.shape[0]/RESIZE_FACTOR)))        
            faces = self.face_cascade.detectMultiScale(
                color_resized,
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

                face = color[y:y+h, x:x+w]
                face_resized = cv2.resize(face, (resized_width, resized_height))
                img_no = sorted([int(fn[:fn.find('.')]) for fn in os.listdir(self.path) if fn[0]!='.' ]+[0])[-1] + 1
                
                if self.count_timer%FREQ_DIV == 0:
                    cv2.imwrite('%s/%s.png' % (self.path, img_no), face_resized)
                    self.count_captures += 1
                    print("Captured image: ", self.count_captures)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, self.face_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1,(0, 255, 0))
        elif self.count_captures == NUM_TRAINING:
            print("Data telah ditambahkan ke "+self.face_name+". Tekan 'q' untuk mengakhiri program.")
            self.count_captures += 1

        return frame           

if __name__ == '__main__':
    trainer = TrainEigenFaces()
    trainer.capture_training_images()
    print("Silahkan memilih menu kembali")