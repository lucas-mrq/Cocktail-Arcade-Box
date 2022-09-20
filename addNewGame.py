import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import shutil
import time

newGame=str(input("Quel est le nom de votre nouveau jeu ? ")).lower()
#newGame="guess"

def appendLauncher(gameName):
    
    f = open("Launcher.py", "r")
    programme=f.read()

    programme2=programme.split("\n")

    programme2=[programme2[0]]+["from "+gameName+"."+gameName[0].upper()+gameName[1:]+" import "+gameName[0].upper()+gameName[1:]+"_Game"]+programme2[1:]
    programme2.append(programme2[-4][0:11]+"\""+gameName+"\":")
    programme2.append(programme2[-4][0:2]+gameName+" = "+gameName[0].upper()+gameName[1:]+"_Game()")
    programme2.append(programme2[-4][0:2]+gameName+".game()")
    programme2.append("")

    f.close()

    f = open("Launcher.py", "w")

    newLauncher="\n".join(programme2)

    f.write(newLauncher)

    f.close()

def appendImage(gameName):
    
    imagePos=[[95,345],[280,115],[280,343],[95,115],[95,345]]
    
    f = open("menu/Menu.py", "r")
    programme=f.read()

    for i in range(len(programme)-10):
        if programme[i:i+8]=="newGame=":
            numeroFutur=int(programme[i+8])-1

    f.close()

    green1=[0.70980394,0.9019608,0.11372549]
    green2=[0.13333334,0.69411767,0.29803923]

    imageSrc = np.copy(plt.imread("new/img/"+gameName+'.png'))

    print(imageSrc[0][0])

    if len(imageSrc)<len(imageSrc[1]):
        reverse=imageSrc.copy()
        imageSrc=np.zeros((len(imageSrc[0]),len(imageSrc),len(imageSrc[0][0])))
        for i in range(len(imageSrc)):
            for j in range(len(imageSrc[0])):
                if (i==0 or j==0 or i==len(imageSrc)-1 or j==len(imageSrc[0])-1) or (i==2 and j>1 and j<len(imageSrc[0])-2) or (j==2 and i>1 and i<len(imageSrc)-2) or (i==len(imageSrc)-3 and j>1 and j<len(imageSrc[0])-2) or (j==len(imageSrc[0])-3 and i>1 and i<len(imageSrc)-2):
                    if len(imageSrc[0][0])==4:
                        imageSrc[i][j]=np.array(green1+[1])
                    else:
                        imageSrc[i][j]=np.array(green1)
                elif (i==1 and j>0 and j<len(imageSrc[0])-1) or (j==1 and i>0 and i<len(imageSrc)-1) or (i==len(imageSrc)-2 and j>0 and j<len(imageSrc[0])-1) or (j==len(imageSrc[0])-2 and i>0 and i<len(imageSrc)-1):
                    if len(imageSrc[0][0])==4:
                        imageSrc[i][j]=np.array(green2+[1])
                    else:
                        imageSrc[i][j]=np.array(green2)
                else:
                    imageSrc[i][j]=reverse[j][i].copy()

        for i in range(int(len(imageSrc))):
            for j in range(int(len(imageSrc[0])/2)):
                wait=imageSrc[i][j].copy()
                imageSrc[i][j]=imageSrc[i][-j-1].copy()
                imageSrc[i][-j-1]=wait.copy()

    if numeroFutur==0:
        menuName='menu/img/menu1.png'
    else: 
        menuName='menu/img/menu2.png'

    imageOut = np.copy(plt.imread(menuName))

    plt.imsave("menu/img/"+gameName+".png",imageSrc)
    imgGray = cv2.imread('menu/img/'+gameName+'.png',0)
    cv2.imwrite("testSrcGray.png", imgGray)

    imageSrc = np.copy(plt.imread("testSrcGray.png"))

    os.system("rm testSrcGray.png")

    for i in range(len(imageSrc)):
        for j in range(len(imageSrc[0])):
            imageSrc[i][j]=1-imageSrc[i][j]

    for i in range(imagePos[numeroFutur][1],imagePos[numeroFutur][1]+len(imageSrc)):
        for j in range(imagePos[numeroFutur][0],imagePos[numeroFutur][0]+len(imageSrc[0])):
            imageOut[i][j]=imageSrc[i-imagePos[numeroFutur][1]][j-imagePos[numeroFutur][0]].copy()

    plt.imsave(menuName,imageOut)


def appendMenu(gameName):
    
    f = open("menu/Menu.py", "r")
    programme=f.read()

    for i in range(len(programme)-10):
        if programme[i:i+8]=="newGame=":
            numeroFutur=str(int(programme[i+8])+1)
            programme=programme[:i+8]+numeroFutur+programme[i+9:]

        if programme[i:i+12]=="newArchive=\"":
            j=i+12
            while programme[j]!="\"":
                j+=1
            programme=programme[:j]+","+gameName+programme[j:]

        
    for i in range(len(programme)-10):
        if programme[i:i+6]=="futur"+numeroFutur:
            programme=programme[:i]+gameName+programme[i+6:]
        if programme[i:i+6]=="Futur"+numeroFutur:
            programme=programme[:i]+gameName[0].upper()+gameName[1:]+programme[i+6:]

    f.close()

    f = open("menu/Menu.py", "w")

    f.write(programme)

    f.close()


def appendFile(newGame):
    f = open("menu/Menu.py", "r")
    programme=f.read()

    start=1
    for i in range(len(programme)-10):
        if programme[i:i+8]=="newGame=":
            numeroFutur=str(int(programme[i+8])+1)
            programme=programme[:i+8]+numeroFutur+programme[i+9:]
        if programme[i:i+11]=="newArchive=":
            start=0
            listeFolder=[]
            fichier=""
        elif start==0 and programme[i+11]=="\"":
            start=1
            listeFolder.append(fichier)
        elif start==0 and programme[i+11]==",":
            listeFolder.append(fichier)
            fichier=""
        elif start==0:
            fichier=fichier+programme[i+11]

    os.system("mkdir Archive_"+numeroFutur)

    print(listeFolder)
    print([6,len(listeFolder)])

    for i in range(4,6):
        os.system("cp "+listeFolder[i]+" Archive_"+numeroFutur+"/"+listeFolder[i])

    for i in range(4):
        os.system("rsync -avx "+listeFolder[i]+"/ Archive_"+numeroFutur+"/"+listeFolder[i]+"/")

    for i in range(6,len(listeFolder)):
        os.system("rsync -avx "+listeFolder[i]+"/ Archive_"+numeroFutur+"/"+listeFolder[i]+"/")

def renameFolder(newGame):
    os.system("mv new "+newGame)

    os.system("mkdir img")
    os.system("mkdir new")
    os.system("rsync -avx img/ new/img/")    
    os.system("rmdir img")

appendFile(newGame)
appendLauncher(newGame)
appendMenu(newGame)
appendImage(newGame)
renameFolder(newGame)
