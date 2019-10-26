import matplotlib.pyplot as plt
from scipy import cluster
import pandas as pd
import numpy as np
from sys import argv

_, *imgpath, n = argv

img = plt.imread(' '.join(imgpath))
n = int(n)
height = 20
w = 50
width = w*n

plt.imshow(img)
plt.show()


red, green, blue = [], [], []
for line in img:
    for pixel in line:
        r, g, b = pixel
        red.append(r)
        green.append(g)
        blue.append(b)
        

df = pd.DataFrame({
    'red': red,
    'green': green,
    'blue': blue
})

print(f'Analysing {len(df)} pixels...')
                   
color_pallete, _ = cluster.vq.kmeans(df.astype('float'), n)
color_pallete = [list(map(lambda x: int(x), color)) for color in color_pallete]

hexcodes = [''.join(list(map(lambda x: hex(x)[2:], color))) for color in color_pallete]
blank_image = np.zeros((height,width,3), np.uint8)

for rgb, hex_ in zip(color_pallete, hexcodes):
    print(rgb, hex_, sep='\t')

for i in range(n):
    blank_image[:, i*w:(i+1)*w] = color_pallete[i]
    
fig, ax = plt.subplots()
plt.imshow(blank_image)
for i in range(n):
    ax.annotate('#'+hexcodes[i],
                xy=(50*i+25, 1), xycoords='data',
                xytext=(-25, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")) 
plt.show()    
