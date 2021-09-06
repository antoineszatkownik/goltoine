# What is goltoine ?

***goltoine*** is an algorithm that generates a video in .avi format. GoL stands for Game of Life, it is a game of life where a cell is not a black or white pixel but an image among a set of images that should be considered as an alphabet. Those images are elementary motives painted with acrylics, elementary because the pattern of the motif is meant to stay simple (thus two different colors is a good choice), not too complex (with the outline) since what is sought is to make emerge a global pattern with some complexity out of a bunch of low complexity elementary motives. By generating a dynamical global pattern we hoped to find some kind of meaning conveyed by the arrangements between the cells, they act as some sorts of lego like ideograms.

The interpretation of the result is of course left out to the viewer ;)

Here is the alphabet being used : <br />
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img1_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img2_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img3_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img3_bis%20(2).jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img4_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img5_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img6_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img8_bis.jpg)

Example of a sequence of iterations : <br />
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/goltoinevid%20(3).gif)

***Note 1 :*** You can use a blank square as an element of the alphabet to clear things out, which is being done above. <br />
***Note 2 :*** You can use a different alphabet (the element of the alphabet have dimension 64*64) but of the same size (8), otherwise you will have to use a different encryption and it should be an alphabet of size 2**n for n a strictly positive integer corresponding to the number of grids used for the encryption.

# How to use

Simply change the names of the paths.
Create a folder named "goltoine", put the goltoine.py code in it and the elements of the alphabet, create in "goltoine" folder a folder named "set", this is where the iterations will be saved.

***What you can change :*** <br />
the number of iterations with the "nbframe" variable <br />
the size of the grid with the variable "taille" <br />
the frame rate per second with the "fps" variable (the gif was made with fps=10) <br />
the alphabet (see Note 2)

# Next

What could be next :

-add rotations 

Credits to Jean Macquet
