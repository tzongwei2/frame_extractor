import os
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f",default = "0", help="every nth to extract")
parser.add_argument("-out",default ="output", help="output folder name")
args = parser.parse_args()

video_path = "videos"

if not os.path.exists(args.out):
    os.makedirs(args.out)
    
def extract(video):
    # filename = os.path.splitext(video)[0] #remove the extension from the name
    global ncount
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    n = int(fps)
    
    if(args.f == "0"):
        pass
    else:
        n = int(args.f)

    count=0
    while True:
        read,frame = cap.read()
        if not read:
            cap.release()
            break

        if(count%(2*n) == 0): #save every nth frame
            cv2.imwrite(args.out +"\\" + str(ncount) + ".jpg",frame)
            ncount+=1

        count+=1
        

if __name__ == "__main__":
    ncount =0
    print("extracting images. . .")
    for file in os.listdir(video_path):
        f = os.path.join(video_path, file)
        print("extracting video")
        extract(f)
    print("extracted.")








