import face_recognition
import cv2 as cv

path = input("nom de fichier (complet) a analyser :")
img = face_recognition.load_image_file(path)
floc = []
floc = face_recognition.face_locations(img)

for face in floc:
	top, right, bottom, left = face
	start_point = (left, top)
	end_point = (right, bottom)
	color = (255, 0, 255)
	thickness = 15
	img = cv.rectangle(img, start_point, end_point, color, thickness)
cv.namedWindow("img", cv.WINDOW_NORMAL) 
cv.imshow("img", img[..., ::-1])
cv.waitKey(0)
cv.destroyAllWindows()
