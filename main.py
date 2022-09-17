import gspread
import random
import sys
from imageai.Detection import ObjectDetection
from PIL import Image
import matplotlib.pyplot as plt

#pip install gspread
#pip install imageAI
#pip install opencv-python
#pip install Pillow

def randomCell():
    letters = ['A','B','C','D']
    sa = gspread.service_account("../input/service-accountjson/matchem-362801-3cbdd30a04e9.json")
    sh = sa.open("MatchEm")
    wks = sh.worksheet("Prompt2")
    random_number = random.randint(1, 31)
    random_number1 = random.randint(0, 3)
    random_letter = letters[int(random_number1)]
    #print(str(random_letter)) to debug if needed
    #print(str(random_number))
    value1 = wks.acell(str(random_letter) + str(random_number)).value
    return value1
    
def findProb(aImg):
    obj_detect = ObjectDetection()
    obj_detect.setModelTypeAsYOLOv3()
    obj_detect.setModelPath("../input/yoloh5/yolo.h5")
    obj_detect.loadModel()
    detected_obj = obj_detect.detectObjectsFromImage(
    input_image= str(aImg),
    output_image_path="file_name.png"
)

    for obj in detected_obj:
        value = (obj["name"] + "-" +str(obj["percentage_probability"]),obj["box_points"])
        print(value)
        #return obj["name"]
    #plt.savefig("file_name.png")
    #plt.show()
    
 def createLeaderboard(numUser):
    score = 0
    users = numUser
    userdata = []
    userphoto = ['../input/fruitsample/oragn.jpeg','../input/fruitsample/pear.jpeg','../input/fruitsample/pineaplpe.png']
    scoreslist = []
    for i in range(0,users):
        userdata.append(randomCell())
    try:
        for j in range(0,len(userdata)):
            score = 0 
            if findProb(str(userphoto[j])) in (userdata[j]):
                score += 500
                scoreslist.append(score)
                print("Great Job! Your total score is", str(score), "!")
            elif findProb(str(userphoto[j])) not in (userdata[j]):
                scoreslist.append(0)
                print("Try again! Your total score is", str(score), "!")
                #scoreslist.append(0)
    except:
        scoreslist.append(0)
        print("Try again! Your total score is", str(score), "!")
        
    print("                              ")
    print("CURRENT LEADERBOARD STANDINGS!")
    print("------------------------------")
    
    for i in range(numUser):
        print("User",i+1, "score:",scoreslist[i])
        
createLeaderboard(3)
findProb(str(PATH TO IMAGE))
randomCell()

