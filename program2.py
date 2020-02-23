import cv2

images = ['JPEG_example_JPG_RIP_100.jpg','Lighthouse.jpg','photo.jpg','kangaroos.jpg']


# print(type(img))
# print(img)
# print(img.shape)
for img in images :
    python_image = cv2.imread(img, 0)
    #height = img.shape[0]
    #width = img.shape[1]
    resize_height = int(python_image.shape[0]/2)
    resize_Width = int(python_image.shape[1]/2)
    resize_python_image =cv2.resize(python_image, (resize_Width,resize_height))
    name = 'new' + img
    cv2.imwrite(name, resize_python_image)

print('done')

#cv2.imwrite("JPEG_example_JPG_RIP_100.jpg",resize_image)
# cv2.imshow('JPEG_example_JPG_RIP_100.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllwindows()