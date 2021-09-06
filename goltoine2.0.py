import numpy as np
import cv2
import os
import glob
import sys

rootpath = '/Users/Antoine/Desktop/Connaissance/goltoine'
os.chdir(rootpath)

path='C:/Users/Antoine/Desktop/Connaissance/goltoine/set'

taille = 10   #size of grid
fps=10   #framerate per second
nbframe = 60 #number of frame
n=3  #number of grid
alphabet_size=8

letters_dic={}   # 'x' : element of alphabet   where x is a number ranging fron 0 to 7, and element of alphabet is acrylic image
for x in range(alphabet_size):
    letters_dic["{}".format(x)]=cv2.imread("img{}_bis.jpg".format(x+1))

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

mul = letters_dic['7'].shape[0]    #horizontal dimension of acrylic image
def grilletoimage(g, num, name):
    t = g.shape[0]
    img = np.zeros(np.array(g.shape)*mul)   #a cell is an image
    for i in range (0,t):
        for j in range (0,t):
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
    ginit = np.random.rand(n,taille,taille)
    for a in range(t):
        for b in range(t):
            for c in range(n):
                if ginit[c,a,b] < 0.5:
                    ginit[c,a,b] = 0
                else:
                    ginit[c,a,b] = 1
    return ginit

grille = np.array(ginitgen(taille)) #creation of 3 rdm matrices with values in {0,1}, initialization step

grille_dic = {}  #store grid in dic, should be considered as n-tuple where element of tuple are grid
for x in range(n):
    grille_dic["grille{}".format(x+1)] = grille[x]

def grilletopatchwork(g, num, name):
    t = g.shape[0]
    img = np.zeros((g.shape[0]*mul, g.shape[0]*mul, 3)) #each cell is an image

    for i in range (0,t):
        for j in range (0,t):
            img[mul*i:mul*i+mul,mul*j:mul*j+mul,:] = np.array(letters_dic['{}'.format(int(g[i][j]))])
            #g[i][j] is a number ranging from 0 to 7

    cv2.imwrite(os.path.join(path , str(num) + '.png'), img)
    listofframes.append(img)

for num in range (0,nbframe): #create patchwork for each iteration of GoL

    for x in range(n): #loop on the number of grid
        grilletoimage(grille_dic["grille{}".format(x+1)], num, 'grille{}_'.format(x+1)) # create 3 different GoL in black and white
        grille_dic["grille{}".format(x+1)]=np.array(nextgrille(grille_dic["grille{}".format(x+1)])) #update each GoL (computation of next iteration)

    sum=0  # sum for 1<=k<=n of GoL_grid_k*2**(k-1), it is a conversion from binary to decimal
    for k in range(n):
        sum+=grille_dic["grille{}".format(k+1)]*2**k
    grillef = np.array(sum)   #3 grids for 2**3 possible images, final grid is inear combination of 3 GoL

    grilletopatchwork(grillef, num, 'goltoine') #name of acrylic image = str(sum)


# set of images to vid (i.e. stop motion)
img_array = []
array_bis = glob.glob(path+ '/*.png')

def sortKeyFunc(s):
    return int(os.path.splitext(os.path.basename(s))[0])

array_bis.sort(key=sortKeyFunc)

for filename in array_bis:
    print(filename)
    imgbis = cv2.imread(filename)
    height, width, layers = imgbis.shape
    size = (width,height)     #not needed it is in fact = (64*taille,64*taille)
    img_array.append(imgbis)
 
out = cv2.VideoWriter('goltoinevid.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, (64*taille,64*taille))
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()








    
    
        

