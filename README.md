# What is goltoine ?

***goltoine*** is an algorithm that generates a video in .avi format. GoL stands for Game of Life, it is a game of life where a cell is not a black or white pixel but an image among a set of images that should be considered as an alphabet. Those images are elementary motives painted with acrylics, elementary because the pattern of the motif is meant to stay simple (thus two different colors is a good choice), not too complex (with the outline) since what is sought is to make emerge a global pattern with some complexity out of a bunch of low complexity elementary motives. By generating a dynamical global pattern we hoped to find some kind of meaning conveyed by the arrangements between the cells, they act as some sorts of lego like ideograms.

The interpretation of the result is of course left out to the viewer ;)

Here is the alphabet being used : <br />
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img1_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img2_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img3_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img4_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img5_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img6_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img7_bis.jpg)
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/img8_bis.jpg)

Example of a sequence of iterations : <br />
![alt text](https://github.com/antoineszatkownik/goltoine/blob/main/data/goltoinevid%20(3).gif)

***Note 1 :*** You can use a blank square as an element of the alphabet to clear things out, which is being done above. <br />
***Note 2 :*** You can use a different alphabet (the element of the alphabet have dimension 64*64) but of the same size (8), otherwise you will have to use a different encryption and it should be an alphabet of size 2**n for n a strictly positive integer corresponding to the number of grids used for the encryption.

# About the code

At each iteration of the goltoine, a cell represented as a letter in the alphabet is encoded by 3 bits given by 3 simultaneous black and white Game of Life (=GoL). More precisely : <br />

Let <img src="https://render.githubusercontent.com/render/math?math=\Omega"> be the alphabet of acrylic images, <img src="https://render.githubusercontent.com/render/math?math=$n$"> the number of simultaneous GoL (i.e. grid) and <img src="https://render.githubusercontent.com/render/math?math=$t$"> the size in the <img src="https://render.githubusercontent.com/render/math?math=$X$"> or <img src="https://render.githubusercontent.com/render/math?math=$Y$"> dimension of the grid of a GoL. <br />
In the goltoine's grid, each letter at the position <img src="https://render.githubusercontent.com/render/math?math=$x$"> corresponds to a <img src="https://render.githubusercontent.com/render/math?math=$n$"> -tuple <img src="https://render.githubusercontent.com/render/math?math=$(a_1,...,a_n) \in \{0,1\}^n$"> such that for <img src="https://render.githubusercontent.com/render/math?math=$M_{goltoine}$">, the underlying grid of the goltoine (which is a <img src="https://render.githubusercontent.com/render/math?math=$t \times t$"> matrix), we have <p align="center"> <img src="https://render.githubusercontent.com/render/math?math=$M_{goltoine}(x) = \sum_{k \in \{1,...,n\}} a_k \times 2^{k-1}$"> </p>  
<p align="left"> The sum is a linear combination of the <img src="https://render.githubusercontent.com/render/math?math=$n$"> simultaneous GoL, taking value in <img src="https://render.githubusercontent.com/render/math?math=$\{0,...,2^{n}-1\}$">. Thus <img src="https://render.githubusercontent.com/render/math?math=$|\Omega|=2^{n}$"> </p>


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
