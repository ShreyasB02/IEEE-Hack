#!/usr/bin/env python
# coding: utf-8

# 

# In[252]:


#get_ipython().system('pip install cryptography')


# In[253]:


import cv2
import pytesseract
import os
from PIL import Image
import sys
import numpy as np
import pandas as pd
from cryptography.fernet import Fernet


# ## 00: Opening an Image

# In[216]:


import cv2
from matplotlib import pyplot as plt
image_file = "D:/PES/Projects/silicon_rush/image_to_text/mymodel/data/labrep1_hack_camera2.jpg"
im_data = plt.imread(image_file)
img = cv2.imread(image_file)


# In[217]:


#https://stackoverflow.com/questions/28816046/
#displaying-different-images-with-actual-size-in-matplotlib-subplot
def display(im_data):
    dpi = 80
#     im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()


# In[218]:


display(im_data)


# ## 01: Inverted Images

# In[219]:


inverted_image = cv2.bitwise_not(img)
# cv2.imwrite("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/inverted.jpg", inverted_image)


# In[220]:


display(inverted_image)


# ## 02: Rescaling

# In[ ]:





# In[ ]:





# ## 03: Binarization

# In[221]:


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[222]:


gray_image = grayscale(img)
# cv2.imwrite("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/gray.jpg", gray_image)


# In[138]:


# display("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/gray.jpg")


# In[223]:


thresh, im_bw = cv2.threshold(gray_image, 100, 100, cv2.THRESH_BINARY)
# cv2.imwrite("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/bw_image.jpg", im_bw)


# In[142]:


# display("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/bw_image.jpg")


# ## 04: Noise Removal

# In[224]:


def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)


# In[225]:


no_noise = noise_removal(im_bw)
# cv2.imwrite("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/no_noise.jpg", no_noise)


# In[226]:


# display("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/no_noise.jpg")


# ## Dilation and Erosion

# In[227]:


def thin_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)


# In[228]:


eroded_image = thin_font(gray_image)
# cv2.imwrite("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/eroded_image.jpg", eroded_image)


# In[229]:


# display("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/eroded_image.jpg")


# In[230]:


def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)


# In[231]:


dilated_image = thick_font(no_noise)
# cv2.imwrite("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/dilated_image.jpg", dilated_image)


# In[233]:


display(dilated_image)


# In[ ]:





# 

# In[ ]:





# In[36]:





# In[42]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[46]:





# In[ ]:





# In[51]:





# In[235]:


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[53]:


# def get_string(img_path):
#     # Read image with opencv
#     img = cv2.imread(img_path)
# #     cv2.imshow("thres.png", img)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
#     # Convert to gray
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Apply dilation and erosion to remove some noise
#     kernel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)

#     # Write the image after apply opencv to do some ...
# #     cv2.imshow("thres.png", img)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
#     cv2.imwrite("thres.png", img)
#     # Recognize text with tesseract for python
#     result = pytesseract.image_to_string(Image.open("thres.png"))
#     os.remove("thres.png")

#     return result


# In[56]:


# with open("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/readme.txt", 'w') as f:
#     f.write(get_string("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/no_borders.jpg"))


# In[236]:


# print(pytesseract.image_to_string(Image.open("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/dilated_image.jpg")))


# In[237]:


print(pytesseract.image_to_string(dilated_image))


# In[238]:


with open("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/readme.txt", 'w') as f:
    f.write(pytesseract.image_to_string(dilated_image))


# In[239]:


a_file = open("D:/PES/Projects/silicon_rush/image_to_text/mymodel/sample_tests/readme.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
    
  list_of_lists.append(stripped_line)

a_file.close()

print(list_of_lists)


# In[240]:


for i in range(len(list_of_lists)):
    if "Test" in list_of_lists[i]:
        start=i
    if "Page" in list_of_lists[i]:
        end=i
        
final = list_of_lists[start:end:1]
print(final)


# In[241]:


# import re
# def custom_split(s):
#     temp = re.compile("([a-zA-Z]+)([0-9]+)([a-zA-Z]+)([0-9]+)")
#     res = temp.match(s).groups()
#     return list(res)


# In[247]:


from collections import defaultdict
d=defaultdict(list)
split_list=[]
column_headers= final[0]
for i in final[4::]:
    k=i.split(' ')
    if k[1].isalpha():
        key=k[0]+k[1]
        val1=k[2]
        val2=k[3]
        val3=k[4]
        val4=k[6]
    else:
        key=k[0]
        val1=k[1]
        val2=k[2]
        val3=k[3]
        val4=k[5]
    d[key].extend([val1,val2,val3,val4])    
  
# print(d['Potassium'])


# In[244]:


# print("acid".isalpha())


# In[245]:


final_split=[]
for key in d.keys():
    split_list=[]
    split_list.append(key)
    split_list.extend(d[key])
    final_split.append(split_list)
# print(final_split)


# In[248]:




df = pd.DataFrame(data=final_split,columns=['Test Name','Results','Units','LowRange','HighRange'])


# In[249]:


df.head()


# In[251]:


df.to_csv('report.csv')


# In[258]:


def encrypt(csv_file):
    

    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
       filekey.write(key)

    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
       filekey.write(key)

    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(csv_file, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open('encrypted_report.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# In[259]:


def decrypt(csv_file):
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
 
    fernet = Fernet(key)

    # opening the encrypted file
    with open(csv_file, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('decrypted_report.csv', 'wb') as dec_file:
        dec_file.write(decrypted)


# In[260]:


# encrypting

encrypt('report.csv')


# In[261]:


#decrypting
decrypt('encrypted_report.csv')


# In[ ]:




