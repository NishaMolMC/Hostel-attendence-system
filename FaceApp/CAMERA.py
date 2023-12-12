from comtypes.client import CreateObject






import cv2 #computer vision
import  face_recognition
cap = cv2.VideoCapture(0)  # physical camera device assigned to  cap




from DBConnection import Db
qry="SELECT * FROM `myapp_student`"
db=Db()
res= db.select(qry)

print(res)


id=[]
imagefeatures=[]
s="D:\\Mca project\\HostelAttendanceSystemwithFaceDetection\\HostelAttendanceSystemwithFaceDetection\\media\\"

for i in res:

    id.append(i['id'])
    p=s+i['Photo'].replace("/media/","")

    known_image = face_recognition.load_image_file(p)
    lnd=face_recognition.face_encodings(known_image)[0]

    import winsound

    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


    imagefeatures.append(lnd)

print(id)
print(imagefeatures)












while True:                          ####  init infinit loop
    ret, frame = cap.read()


    cv2.imwrite("a.jpg",frame)

    unknown_image = face_recognition.load_image_file("a.jpg")
    lnd = face_recognition.face_encodings(unknown_image)

    print(len(lnd))



    for i in lnd:
        s=face_recognition.compare_faces(imagefeatures,i, tolerance=.45)
        print(s)


        for j in range(len(s)):
            if s[j]==True:


                qry="SELECT * FROM `myapp_attendance` WHERE `Date`= CURDATE() AND HOUR(TIME)= HOUR(CURTIME()) AND `SUDENT_ID_id`='"+str(id[j])+"'"
                res2= db.select(qry)
                if len(res2)==0:
                    qry="INSERT INTO `myapp_attendance` (`Date`,`Time`,`SUDENT_ID_id`) VALUES (CURDATE(), CURTIME(), '"+str(id[j])+"')"
                    db.insert(qry)


    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)

    if c == 113:
        break

cap.release()
cv2.destroyAllWindows()