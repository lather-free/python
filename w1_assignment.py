import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

def openimg(imgpath):
    img=cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return False
    return img

#wait for a key, and escape the main figure widnow
def escapeimg():
    key=cv2.waitKey()
    if key == 27:
        cv2.destroyAllWindows()

'''
print image information, such as data type, shape and so on...
for shape, the format is (rows, cols, channels)
'''
def printimginfo(img):
    print('img data type is:',img.dtype)
    print('img size is:',img.shape)

'''
create a window that show a image:
imgtitle:   title of the window
img:        image data of the image
windowtype: type of the window, default is keepration
'''
def create_window(imgtitle, img, windowtype=cv2.WINDOW_KEEPRATIO):
    cv2.namedWindow(imgtitle, windowtype)
    cv2.imshow(imgtitle, img)

'''
show the gray value of the original image.
imgpath:    path of the image
imgtitle:   window title of the image
'''
def show_gray(imgpath, imgtitle='gray'):
    img_gray = cv2.imread(imgpath, 0)
    if img_gray.any == None:
        print('img  {} does not exist!'.format(imgpath))
        return
    create_window(imgtitle,img_gray)
    printimginfo(img_gray)
    print(img_gray)

'''
get the gray value of the original image.
img:        the original image
ch:         channel of the gray
return: gray_img
'''
def get_gray(img, ch=0):
    img_gray = img[:,:,ch]
    return  img_gray

'''
show the original image.
imgpath:    path where the image is stored
imgtitle:   title of the window which shows the image
'''
def show_or(imgpath, imgtitle='orignal'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img:{}'.format(imgpath))
        return
    create_window(imgtitle, img)
    printimginfo(img)

'''
crop of a img.
x:  start row number
y:  start col number
height: rows of the new img
width:  cols of the new img
'''
def show_crop(imgpath, x=0,y=0,height=30000, width=30000, imgtitle='img_crop'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img: {} dose not exist'.format(imgpath))
        return

    ##crop
    img_crop=img[x:height, y:width]
    create_window(imgtitle,img_crop)
    printimginfo(img_crop)

'''
get crop of a image.
img:    the original image.
x:      start row of new img
y:      start col of new img
h:      height of img
w:      width of img
'''
def get_crop(img,x=0,y=0, h=30000, w=30000):
    img_crop=img[x:h, y:w]
    return img_crop


'''
show three images of the orignal img in gray map of blue,green and red
imgpath:    path of the image
imgtitle:   title of the image
'''
def show_colorsplit(imgpath,imgtitle='img_colorsplit'):
    img=cv2.imread(imgpath)
    if img.any == None:
        print('img: {} dose not exist'.format(imgpath))
        return
    img_b, img_g, img_r = cv2.split(img)
    create_window(imgtitle+'red', img_r)
    printimginfo(img_r)
    create_window(imgtitle+'green', img_g)
    printimginfo(img_g)
    create_window(imgtitle+'blue', img_b)
    printimginfo(img_b)

'''
get a random lighten RGB image
img: the original image
algorithm:
first generate a rand_value for (R,G,B) channel
for each gray_value of RGB:
    if rand_value > 0 then enhance the light value:
        if gray_value > limits then 
            new_gray_value=255
        else if gray_value <= limits then
            new_gray_value = rand_value + gray_value
    else if rand_value <0 then decrease the light vaule:
        if gray_value < limits then
            new_gray_value = 0 
        else if gray_value >= limits then
            new_gray_value = gray_value + rand_value (because rand_value<0, so the lightness of gray is decreased)
'''
def random_light_color(img):
    # brightness
    B, G, R = cv2.split(img)

    b_rand = random.randint(-50, 50)
    if b_rand == 0:
        pass
    elif b_rand > 0:
        lim = 255 - b_rand
        B[B > lim] = 255
        B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)
    elif b_rand < 0:
        lim = 0 - b_rand
        B[B < lim] = 0
        B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)

    g_rand = random.randint(-50, 50)
    if g_rand == 0:
        pass
    elif g_rand > 0:
        lim = 255 - g_rand
        G[G > lim] = 255
        G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)
    elif g_rand < 0:
        lim = 0 - g_rand
        G[G < lim] = 0
        G[G >= lim] = (g_rand + G[G >= lim]).astype(img.dtype)

    r_rand = random.randint(-50, 50)
    if r_rand == 0:
        pass
    elif r_rand > 0:
        lim = 255 - r_rand
        R[R > lim] = 255
        R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)
    elif r_rand < 0:
        lim = 0 - r_rand
        R[R < lim] = 0
        R[R >= lim] = (r_rand + R[R >= lim]).astype(img.dtype)

    img_merge = cv2.merge((B, G, R))
    return img_merge

'''
show a random light image.
imgpath:    path of the original image
imgtitle:   title of the image window
'''
def show_random_light_color(imgpath, imgtitle='changed_img'):
    img=cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))

    changed_img = random_light_color(img)

    create_window(imgtitle, changed_img)
    printimginfo(changed_img)

'''
get a gamma adjust image.
image:  the original image
gamma:  the gamma factor
'''
def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

'''
show gamma image.
imgpath:    path of the image
gamma:      gamma vaule
imgtitle:   title of the adjusted image.
'''
def show_gamma_img(imgpath, gamma=1.0, imgtitle='gamma_adj'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return
    img_gamma = adjust_gamma(img, gamma)
    create_window(imgtitle, img_gamma)
    printimginfo(img_gamma)

'''
show the histogram of a image
img:    the image data
'''
def show_img_hist(img):
    plt.hist(img.flatten(), 256, [0, 256])
    plt.show()

'''
show the histogram of a image. 
imgpath:    path of the image
notrion: this will show the merged histgram of RGB channels
'''
def show_hist(imgpath):
    img=cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return
    plt.hist(img.flatten(), 256, [0,256])
    plt.show()

'''
show the equalization of RGB image.
imgpath:    path of the image
imgtitle:   title of the image window
algorithm:
first: get the data of all the R,G,B channels
second: do the equalization for each of the R,G,B channel
'''
def show_equalized_img(imgpath, imgtitle='equalized'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return
    img_b=cv2.equalizeHist(img[:,:,0])
    img_g=cv2.equalizeHist(img[:,:,1])
    img_r=cv2.equalizeHist(img[:,:,2])
    img_eq=cv2.merge((img_b,img_g,img_r))
    show_img_hist(img_eq)
    create_window(imgtitle,img_eq)
    printimginfo(img)

'''
show the equalization of YUV image.
imgpath:    path of the image
imgtitle:   title of the image window
algorithm:
first: convert the RGB image into YUV image.
second: do the equalization for the Y channel
third: convert the YUV image into RGB image and show
additionally: the histogram of the equalized image is show.
'''
def show_equalized_yuv(imgpath, imgtitle='equalized_yuv'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img_bgr=cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)
    show_img_hist(img_bgr)
    create_window(imgtitle,img_bgr)
    printimginfo(img_bgr)

'''
show a continous rotation of a image, after continous rotarion, the image information will not loss.
img:    the original image
rc:     position of rotation center, where (x, y), 
        x: is indicated as row ratio of rotation center.
        y: is indicated as column ratio of rotation center
angle:  angle of the rotation in clockwise
transtimes: times that do the rotarion.
imgtitle:   title of the image window.
return:     the final img.
tips:
usage of getRotationMatrix2D: 
    (x,y):  denotes the angle system position.
    angle:  angle in degress
    scale:  scale of the original image

img.shape denotes (rows, columns, channels)
'''
def show_rotation_img(img, rc=(.5,.5), angle=30, transtimes=1,imgtitle='rotation1'):
    scale = 1
    #scale the original image
    Msclae2 = cv2.getRotationMatrix2D((img.shape[1] * .5, img.shape[0] * .5), 0, 2)
    Mscaledot5 = cv2.getRotationMatrix2D((img.shape[1]*.5,img.shape[0]*.5),0,.5)
    img = cv2.warpAffine(img, Mscaledot5, (int(img.shape[1] * scale), int(img.shape[0] * scale)))

    rotate = cv2.getRotationMatrix2D((img.shape[1] * rc[1], img.shape[0] * rc[0]), angle, scale)
    tmpimg = img        #carry the .5 scaled img.
    tmpimg1 = tmpimg    #carry the rotated and 2 scaled img.

    cnt = 0
    while cnt < transtimes:
        tmpimg = cv2.warpAffine(tmpimg, rotate, (int(img.shape[1] * scale), int(img.shape[0] * scale)))
        tmpimg1 = cv2.warpAffine(tmpimg, Msclae2, (int(img.shape[1] * scale), int(img.shape[0] * scale)))

        cnt += 1
        create_window(imgtitle + str(cnt), tmpimg1)
        printimginfo(tmpimg1)
    return tmpimg1

'''
similar with show_rotation_img, but image information will loss after continous rotarion.
'''
def show_rotation_img1(img, rc=(.5,.5), angle=30, transtimes=1,imgtitle='rotation1'):
    scale = 1
    rotate = cv2.getRotationMatrix2D((img.shape[1] * rc[1], img.shape[0] * rc[0]), angle, scale)
    tmpimg = img        #carry the .5 scaled img.

    cnt = 0
    while cnt < transtimes:
        tmpimg = cv2.warpAffine(tmpimg, rotate, (int(img.shape[1] * scale), int(img.shape[0] * scale)))

        cnt += 1
        create_window(imgtitle + str(cnt), tmpimg)
        printimginfo(tmpimg)
    return tmpimg

'''
show a continous rotation of a image
imgpath:    path of the original image
rc:     position of rotation center, where (x, y), 
        x: is indicated as row ratio of rotation center.
        y: is indicated as column ratio of rotation center
angle:  angle of the rotation in clockwise
transtimes: times that do the rotarion.
imgtitle:   prefix of the title of the image window.
return:     the final img.
'''
def show_rotation(imgpath, rc=(.5,.5), angle=30, transtimes=1,imgtitle='rotation'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return
    tmpimg = show_rotation_img(img,rc,angle,transtimes,imgtitle)
    return tmpimg

'''
show scale operation of a img
imgpath:    path of the original image
rc:         center of scale image, (x,y) where x denotes row ratio, y denotes column ratio
scale:      scale
transtimes: define how much time to do the scale
imgtitle:   prefix of the scaled image window
tips:
in scale operation, angle is zero.
'''
def show_scale(imgpath, rc=(.5,.5), scale=1, transtimes=1,imgtitle='scale'):
    angle = 0
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return

    tmpimg = img
    rotate = cv2.getRotationMatrix2D((img.shape[1] * rc[1], img.shape[0] * rc[0]),angle, scale)

    cnt = 0
    while cnt < transtimes:
        tmpimg = cv2.warpAffine(tmpimg, rotate, (int(img.shape[1]), int(img.shape[0])),borderValue=(155,100,155))
        cnt += 1
        create_window(imgtitle + str(cnt), tmpimg)
        printimginfo(tmpimg)
    return tmpimg

'''
show a tranlated image
imgpath:    path of the original image
transm:     (x,y) denotes trans direction of original image, where:
                x: denote distance in pixel towards right or left, if x>=0: right, if x < 0:left
                y: denote distance in pixel towards down or up, if y>=0:down, if y<0:up 
tips:
use affine transform to implement the translation.                
'''
def show_affine_translate(imgpath, transm=(0,0), imgtitle='affine'):
    img = cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist'.format(imgpath))
        return
    rows,cols,ch = img.shape
    print('orignal rows,cols,ch:',rows,cols,ch)
    poss = np.float32([[0,0],[cols-1,0],[0,rows-1]])
    #posd = np.float32([[transm[0], transm[1]], [cols - 1+transm[0], transm[1]], [transm[0], rows - 1+transm[1]]])
    posd = np.float32([[0,0],[28-1,0],[0,28-1]])
    transM=cv2.getAffineTransform(poss, posd)
    #tmp_img=cv2.warpAffine(img,transM, (cols,rows),borderValue=(100,150,100))
    tmp_img = cv2.warpAffine(img, transM, (28, 28), borderValue=(100, 150, 100))
    create_window(imgtitle, tmp_img)
    printimginfo(tmp_img)

'''
get the random perspective image and transform matrix of a image.
img:    the original image
tips:
for the perspective, you should provide:
 1) 4 source points which are not on the same line for any three points.
 2) 4 dst points 
'''
def random_warp(img):
    height, width, channels = img.shape
    # warp:
    random_margin = 600
    x1 = random.randint(-random_margin, random_margin)
    y1 = random.randint(-random_margin, random_margin)
    x2 = random.randint(width - random_margin - 1, width - 1)
    y2 = random.randint(-random_margin, random_margin)
    x3 = random.randint(width - random_margin - 1, width - 1)
    y3 = random.randint(height - random_margin - 1, height - 1)
    x4 = random.randint(-random_margin, random_margin)
    y4 = random.randint(height - random_margin - 1, height - 1)

    dx1 = random.randint(-random_margin, random_margin)
    dy1 = random.randint(-random_margin, random_margin)
    dx2 = random.randint(width - random_margin - 1, width - 1)
    dy2 = random.randint(-random_margin, random_margin)
    dx3 = random.randint(width - random_margin - 1, width - 1)
    dy3 = random.randint(height - random_margin - 1, height - 1)
    dx4 = random.randint(-random_margin, random_margin)
    dy4 = random.randint(height - random_margin - 1, height - 1)

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
    M_warp = cv2.getPerspectiveTransform(pts1, pts2)
    img_warp = cv2.warpPerspective(img, M_warp, (width, height))
    return M_warp, img_warp

'''
show the perspectived image according to the given path
imgpath:    path of the original image
imgtitle:   title of the perspectived image window
'''
def show_perspective(imgpath, imgtitle='perspective'):
    img=cv2.imread(imgpath)
    if img.any == None:
        print('img {} dose not exist!'.format(imgpath))
        return
    transM, tmp_img=random_warp(img)
    create_window(imgtitle, tmp_img)
    printimginfo(tmp_img)


g_path='D:/Users/GaoTao/Documents/pictures/IMG_20190605_095917.jpg'
#show_gray(g_path)
show_or(g_path)
#show_crop(g_path, 0,0,2000,2000)
#show_colorsplit(g_path,'cp')
#random_light_color()
#show_random_light_color(g_path)
#show_gamma_img(g_path,.8)
#show_hist(g_path)
#show_equalized_img(g_path)
#show_equalized_yuv(g_path)
#tmp_img = show_rotation(g_path,(.5,.5),40,9)
#tmp_img=show_scale(g_path,(.5,.0),.5,1)
#tmp_img=show_rotation_img(tmp_img,(.5,.5),45,1,'rotate')
#show_affine(g_path)
show_affine_translate(g_path,(1000, 100),'trans1')
#show_affine_translate(g_path,(-1000, 100),'trans2')
#show_affine_translate(g_path,(-1000, -100),'trans3')
#show_perspective(g_path)

escapeimg()

