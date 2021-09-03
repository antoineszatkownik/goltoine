import numpy as np
import cv2
import os
import glob
import sys

rootpath = '/Users/Antoine/Desktop/goltoine'
os.chdir(rootpath)

taille = 10

im1 = cv2.imread("img.jpg")
im2 = cv2.imread("img9_bis.jpg")
im3 = cv2.imread("img2_bis.jpg")
im4 = cv2.imread("img4_bis.jpg")
im5 = cv2.imread("img6_bis.jpg")
im6 = cv2.imread("img1_bis.jpg")
im7 = cv2.imread("img8_bis.jpg")
im8 = cv2.imread("img5_bis.jpg")
listimages = [im1,im2,im3,im4,im5,im6,im7,im8]
listvalue = [0,1,10,11,100,101,110,111]
listofframes = []

def nextcel(g,pos):   #game of life rules
    value = 0
    t = g.shape[0]
    i = pos[0]       #current position (=cell)
    j = pos[1]
    lx = [i-1,i,i+1]     #neighborhood (square) of current position
    ly = [j-1,j,j+1]
    livingaround = 0
    for x in lx:
        for y in ly:
            if 0 <= x  and x < t and 0 <= y and y < t and (x != i or y!= j):   #visit neighborhood by staying inside the grid
                livingaround = livingaround + g[x,y]  #someone is in the neighborhood
    if g[i,j] == 0:  #if current position is dead
        if livingaround == 3:   #if current pos has 3 neighboor alive
            value = 1   #then current position is alive
        else:
            value = 0
    else:
        if livingaround != 2 and livingaround != 3:
            value = 0
        else:
            value = 1  #if current pos has 2 or 3 neighboor alive then it is alive
    return value
        
def nextgrille(g):   #next grid
    gnext = np.zeros(np.shape(g))
    t = g.shape[0]
    for i in range (t):
        for j in range (t):
            gnext[i,j] = nextcel(g,(i,j))
    return gnext

mul = im2.shape[0]
def grilletoimage(g, num, name):
    t = g.shape[0]
    img = np.zeros(np.array(g.shape)*mul)   #a cell is an image
    for i in range (0,t-1):
        for j in range (0,t-1):
            if g[i,j] == 0:  #if dead black
                #cv2.rectangle(img, (mul*i,mul*j), (mul*i + +mul, mul*j + mul), 0)
                rec(img, (mul*i,mul*j), (mul*i + +mul, mul*j + mul), 0)   #create for each cell in grid a rectangle of the size of the image activated or not
            else: #if alive white
                #cv2.rectangle(img, (mul*i,mul*j), (mul*i + +mul, mul*j + mul), 255)
                rec(img, (mul*i,mul*j), (mul*i + +mul, mul*j + mul), 255)
    cv2.imwrite(name + str(num) + '.png', img)

def rec(v, p1,p2, value):  #equivalent of cv2.rec but for value specified by the "value" variable
        v[p1[0]:p2[0],p1[1]:p2[1]] = np.ones(v[p1[0]:p2[0],p1[1]:p2[1]].shape)*value

def ginitgen(t): #create 3 rdm matrices with values in {0,1}
    ginit = np.random.rand(3,taille,taille)
    for a in range(t):
        for b in range(t):
            for c in range(3):
                if ginit[c,a,b] < 0.5:
                    ginit[c,a,b] = 0
                else:
                    ginit[c,a,b] = 1
    return ginit

grille = np.array(ginitgen(taille))
grille1 = grille[0]
grille2 = grille[1]
grille3 = grille[2]


def grilletopatchwork(g, num, name):
    t = g.shape[0]
    img = np.zeros((g.shape[0]*mul, g.shape[0]*mul, 3)) #each cell is an image
    for i in range (0,t-1):
        for j in range (0,t-1):
            if abs(g[i,j]-0) < 0.5:  #codage binaire
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im1)
            if abs(g[i,j]-1) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im2)
            if abs(g[i,j]-10) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im3)
            if abs(g[i,j]-11) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im4)
            if abs(g[i,j]-100) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im5)
            if abs(g[i,j]-101) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im6)
            if abs(g[i,j]-110) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im7)
            if abs(g[i,j]-111) < 0.5:
                img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(im8)
    cv2.imwrite(str(num) + '.png', img)
    listofframes.append(img)

nbframe = 60
for num in range (0,nbframe):
    grillef = np.array(grille1 + 10*grille2 + 100*grille3)   #3 grilles pour 2**3 images possibles
    grilletoimage(grille1, num, 'grillea')
    grilletoimage(grille2, num, 'grilleb')
    grilletoimage(grille3, num, 'grillec')
    grilletopatchwork(grillef, num, 'goltoine')
    grille1 = np.array(nextgrille(grille1))
    grille2 = np.array(nextgrille(grille2))
    grille3 = np.array(nextgrille(grille3))


img_array = []
array_bis = glob.glob('C:/Users/Antoine/Desktop/goltoine/set/*.png')

def sortKeyFunc(s):
    return int(os.path.splitext(os.path.basename(s))[0])

array_bis.sort(key=sortKeyFunc)


# set of images to vid (i.e. stop motion)

for filename in array_bis:
    print(filename)
    imgbis = cv2.imread(filename)
    height, width, layers = imgbis.shape
    size = (width,height)
    img_array.append(imgbis)
 
 
out = cv2.VideoWriter('goltoinevid.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()








    
    
        

