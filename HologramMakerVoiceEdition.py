#made by Ankan Das, UEM-K
from PIL import Image as p
#for importing the pillow library for image processing
import speech_recognition as sr

xl=['YES','Y','YAP','YAS','YUS','YOS','YEET','YIP','1','YEAH','YEP']
#list of affirmative synonyms lol
a1=sr.Recognizer()
def recog(aud):
    try:
        return a1.recognize_google(aud)
    except sr.UnknownValueError:
        return '-1'
    except sr.RequestError:
        return '-2'
#def for returning voice recognition info
        
def dimensions(imx):
    dim1=list(imx.size)
    wid1=dim1[0]
    ht1=dim1[1]
    return wid1,ht1
#function for measuring dimensions of images
while True:
    c1=0
    x=input("Enter name of file/picture wanted to be edited\n\nPROTIP: You can get path of file by doing the following:\n>While holding down SHIFT, right click(Right Mouse Button click) on the image file\n>A drop down menu appears\n>Clicking on \"Copy as path\" copies the path of the file\n")
    x=list(x)
    try:
        while True:
            x.remove('"')
    except ValueError:
        pass
    x=''.join(x)
    #for removing any kind of " symbols that might be present due to copying of path of file

    #m=input("Did you enter the format of the image as well?\n1/Yes/Y/Yep/Yas/Yus/Yap/Yos/Yeet/Yip->YES\t2 or NOOOOO->NO\n")

    print("(VOICE MODE, just speak it out in 1/Yes)\nDid you enter the format of the image as well?\n1/Yes/Yeah->YES\t2 or NOOOOO->NO\n")

    with sr.Microphone() as source:
        print("Speak please: ")
        print("--------------")
        audio=a1.listen(source)
    print("Cranking that google api...\n")
    resp1=recog(audio)
    print(resp1)#test
    if(resp1=='-1' or resp1=='-2'):
        m=input("(TYPE IT OUT SINCE VOICE DETECTION FAILED)Did you enter the format of the image as well?\n1/Yes/Y/Yep/Yas/Yus/Yap/Yos/Yeet/Yip->YES\t2 or NOOOOO->NO\n")
        if(m=='1' or m.upper()=='YES' or m.upper()=='Y' or m.upper()=='YEP' or m.upper()=='YAP' or m.upper()=='YAS' or m.upper()=='YUS' or m.upper()=='YOS' or m.upper()=='YEET' or m.upper()=='YIP'):
            image1=p.open(x)
        else:
            y=input("Enter format of the picture/file\n")
            image1=p.open(x+'.'+y)
    else:
        resp1=resp1.upper()
        for i in range(len(xl)):
            if(resp1.find(xl[i])!=-1):
                c1=1
                break
    if(c1==1):
        image1=p.open(x)
        print("You said Yes or 1\n")
    else:
        print("You said 'No' so...")
        y=input("Enter format of the picture/file\n")
        image1=p.open(x+'.'+y)
    c1=0#for clearing value for next usage
    #for inputting image and its properties and stuff

    print("(VOICE MODE)Speak the dimension of the file you need(Just 1000 or 1500 would mean 1000x1000 and 1500x1500 resolution respectively)\n")
    with sr.Microphone() as source:
        print("Speak please: ")
        print("--------------")
        audio1=a1.listen(source)
    print("Cranking that google api...\n")
    resp2=recog(audio1)
    #voice detection for resolution input

    if(resp2=='-1' or resp2=='-2'):
        print("VOICE DETECTION FAILED")
        width=int(input("(TYPE IT OUT)Enter dimension(Width/Height) size just as a single integer\n"))
    else:
        op=[]
        for t in range(len(resp2)):
            if(resp2[t].isdigit()):
                op.append(resp2[t])
        op=''.join(op)
        width=int(op)
        print("Resolution set as "+op+"x"+op+"\n")
    height=width
    #height is equal to width because holograms are based on squares' reflections

    widthdash,heightdash=int(width/2.98),int(height/2.98)
    #the value 2.98 has been basically found by toying with the value
    image1=image1.resize((widthdash,heightdash))
    #change the size division factor only in the above statement
    #image1=image1.crop(,180,100,100)).show()

    image2=image1.rotate(90)
    image3=image2.rotate(90)
    image4=image3.rotate(90)
    #rotate the images by 90 degrees to get the desired images everytime for the hologram

    image=p.new("RGB",(width,height),color='black')
    #creates a black screen 'image' of given dimensions

    wid,ht=dimensions(image1)
    #gives the dimensions of the 'image1' for fitting
    image.paste(image1,((int(width/2)-int(wid/2)),0))
    #pastes image1 into black screen 'image'
    wid,ht=dimensions(image2)
    #gives the dimensions of the 'image2' for fitting
    image.paste(image2,(0,int(height/2)-int(ht/2)))
    #pastes image2 into the black screen 'image'
    wid,ht=dimensions(image3)
    #gives the dimensions of the 'image3' for fitting
    image.paste(image3,(int(width/2)-int(wid/2),int(height/2)+int(ht/2)))
    #pastes image3 into the black screen 'image'
    wid,ht=dimensions(image3)
    #gives the dimensions of the 'image4' for fitting
    image.paste(image4,(int(width/2)+int(wid/2),int(height/2)-int(ht/2)))
    #pastes image4 into the black screen 'image'

    print("(VOICE MODE)Wanna see the newly made image?\n1/Yes/Yeah->YES\t2 or NO or NOOOOO->NO\n")
    with sr.Microphone() as source:
        print("Speak please: ")
        print("--------------")
        audio2=a1.listen(source)
    print("Cranking that google api...\n")
    resp3=recog(audio2)
    #recognizing for yes/no for image to be shown
    if(resp3=='-1' or resp3=='-2'):
        print("Audio Detection failed")
        h=input("(TYPE MODE)Wanna see the newly made image?\n1/Yes/Y/Yep/Yas/Yus/Yap/Yos/Yeet/Yip->YES\t2 or NO or NOOOOO->NO\n")
        if(h=='1' or h.upper()=='YES' or h.upper()=='Y' or h.upper()=='YEP' or h.upper()=='YAP' or h.upper()=='YAS' or h.upper()=='YUS' or h.upper()=='YOS' or h.upper()=='YEET' or h.upper()=='YIP'):
            image.show()
    else:
        resp3=resp3.upper()
        for i1 in range(len(xl)):
            if(resp3.find(xl[i1])!=-1):
                c1=1
                break
    if(c1==1):
        image.show()
    #for showing the output image if you desire(but only if you desire, darling)
    r=input("Enter your preferred output filename alongwith format\ne.g., verynice.jpg to keep it in executable/script's folder\nOR\ne.g., \"F:\\test\\11.jpg\" if you wanna save it as 11.jpg in that directory\n")
    r=list(r)
    try:
        while True:
            r.remove('"')
    except ValueError:
        pass
    r=''.join(r)
    #remove " from file output path for easy input
    image.save(r)
    #for finally saving the image as pow
    c1=0
    print("Wanna make another hologram?\nYes/Yeah means Yes, otherwise no!\n")
    with sr.Microphone() as source:
        print("Speak please: ")
        print("--------------")
        audio3=a1.listen(source)
    resp4=recog(audio3)
    if(resp4=='-1' or resp4=='-2'):
        print("Audio detection failed")
        bv=input("Wanna continue making holograms?\nType in 1 or Yes or Y otherwise, press anything else\n")
        if(bv=='1' or bv.upper()=='Y' or bv.upper()=='YES'):
            for i in range(100):
                print("\n")
            continue
        else:
            break
    else:
        resp4=resp4.upper()
        for jl in range(len(xl)):
            if(resp4.find(xl[jl])!=-1):
                c1=1
                break
    if(c1==1):
        for i in range(100):
            print("\n")
        pass
    else:
        break
print("Thanks for using this!\n")
print("Contact me @RektAlter or ankandas2222@gmail.com or github.com/AnkanDas22 for any query\n")
pm=input("Press Enter to exit\n")
