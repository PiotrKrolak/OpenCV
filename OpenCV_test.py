# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html#py-display-image
# Dokumentacja - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html

import cv2
import numpy as np
import matplotlib as plt

#########
# zmienne
#########

photo = 'pcb_ds.jpg'
film = 'red_panda_snow.mp4'

###################
# definicje funkcji
###################

def picture(photo, color = True):
    """
    Display image of loaded photo.
        @photo - directory of photo
        @color - Color(True) or Gray(False)
    if color == False then it save gray version of oryginal photo as "name_gray.jpg"
    """
    img = cv2.imread(photo, color) # drugi argument laduje zdjecie w odcieniach szarosci(GRAY)
    cv2.imshow('image', img)

    cv2.waitKey(0)

    if color == False:
        cv2.imwrite(photo[0:-4] + '_gray.jpg',img)
        cv2.destroyAllWindows()
    else:
        cv2.destroyAllWindows()


def camera():
    """Turn on you'r camera"""

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == 27: # jeżeli escape to zamknij
            break

    cap.release()
    cv2.destroyAllWindows()


def video(move):
    """
    Turn on Video
        @move - path to video
    """

    cap = cv2.VideoCapture(move)

    fourcc = cv2.VideoWriter_fourcc(*"XVID") # Kodek do formatu zapisu
    out = cv2.VideoWriter("flipped_red_panda.avi", fourcc, 25, (640, 360)) # zapis filmu - nazwa pliku, kodek, klatki/s, rozmiar filmu

    while True:
        ret, frame = cap.read()
        frame2 = cv2.flip(frame, 1) # argument 1 lub 0 obracaja obraz wzgledem ox lub oy

        #print(frame2.shape) # wyświetla wielkość obrazu

        cv2.imshow("frame", frame)
        cv2.imshow("flipping", frame2)

        key = cv2.waitKey(30) # nimber of frame per ms - how fast video will be displayed
        if key == 27: # jeżeli escape to zamknij
            break

    cap.release()
    cv2.destroyAllWindows()



###################
# wywolanie funkcji
###################

# picture(photo, False)
# camera()
video(film)


#######
# Testy
#######

# help(picture)
