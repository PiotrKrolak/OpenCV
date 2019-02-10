# OpenCV - https://www.youtube.com/playlist?list=PL6Yc5OUgcoTmTGACTa__vnifNA744Cz-q

import cv2

#########
# zmienne
#########

photo = 'pcb_ds.jpg'


###################
# definicje funkcji
###################

def picture(path):
    """Show image of picture - argument is path to picture"""
    image = cv2.imread(path) # otwiera obraz

    cv2.imshow('photo', image)

    cv2.waitKey(0) # czeka na przycisniecie dowolnego przycisku przed zamknieciem
    cv2.destroyAllWindows()

def picture_gray(path):
    """Create gray jpg image of picture - argument is path to oryginal picture"""
    image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # zamienia obraz na kolor szary

    name_GRAY = path[0:-4] + '_GRAY.jpg'
    cv2.imwrite(name_GRAY, gray_image)


###################
# wywolanie funkcji
###################

# picture('photo')
# picture_gray('photo')

#######
# testy
#######
