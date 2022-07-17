import cv2
from cv2 import FONT_ITALIC
import numpy
img=cv2.imread('solar-system.heic')
cv2.waitKey(0)
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_ITALIC,
            1.0,
            (225,225,225)
            )
cv2.putText(img,
            "Mercury",
            (141,187),
            cv2.FONT_ITALIC,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "Venus",
            (214,251),
            cv2.FONT_ITALIC,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "Earth",
            (304,170),
            cv2.FONT_ITALIC,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "Mars",
            (402,258),
            cv2.FONT_ITALIC,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "Jupiter",
            (568,212),
            cv2.FONT_ITALIC,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "Saturn",
            (796,224),
            cv2.FONT_ITALIC,
            0.5,
            (225,225,225)
            )
cv2.putText(img,
            "Uranus",
            (923,213),
            cv2.FONT_ITALIC,
            0.5,
            (0,0,1000)
            )
cv2.putText(img,
            "Neptune",
            (1146,200),
            cv2.FONT_ITALIC,
            0.5,
            (0,0,1000)
            )



  
cv2.imshow('output',img)
cv2.imwrite("Solar_systemwithname.jpg",img)