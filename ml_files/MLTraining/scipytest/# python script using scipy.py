# python script using scipy
# for image manipulation
# from scipy.misc import imread, imsave, imresize

# import imageio.v2 as imageio

# from imageio import imread, imsave

#read a jpeg image into a numpy array 
img =imread('C:/Users/SONY/Documents/ml files/cat.jpg') #image path as saved on my device
print(img.dtype, img.shape)

#tinting the image
img_tint = img*[1,0.45,0.3]

#saving the tinted image
imsave('C:/Users/SONY/Documents/ml files/cat_tinted.jpg', img_tint)

#resizing the tinted image to a definite size say 300x300 pixels
img_tint_resize = imresize(img_tint,(300,300))

#saving the resized tinted image

imsave('C:/Users/SONY/Documents/ml files/resized_cat_tinted.jpg',img_tint_resize)

