from glob import glob
import cv2

pngs = glob('C:/Users/Blue Bird/Desktop/New folder/*.png')
# use glob('./**/*.png', recursive=True) for all sub folders.

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)


