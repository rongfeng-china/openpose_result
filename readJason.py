import json
from pprint import pprint
import cv2

data_file = open('tmp_files/tmp_json/color_10_keypoints.json') 
data = json.load(data_file)

#pprint(data)
img = cv2.imread('tmp_files/tmp_color/color_10.png')

numPeople = len(data["people"])
for i in range(numPeople):
    x6,y6,c6 =  data["people"][i]["pose_keypoints"][18:21]
    x7,y7,c7 =  data["people"][i]["pose_keypoints"][21:24]
    #print x6
    #print y6
    #print x7
    #print y7
    cv2.line(img,(int(x6),int(y6)),(int(x7),int(y7)),(255,0,0),3)


cv2.imshow('show',img)
cv2.waitKey(0)
