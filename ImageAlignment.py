# %%
from __future__ import print_function
import cv2
import numpy as np
import os
from PIL import Image
import io
import math
from scipy import ndimage
import json

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15

def itr_ack(page_data):
    count=0
    #print("ITR IMAGE DATA",page_data)
    if "INCOME TAX RETURN".lower() in page_data.lower():
        #print("Income tax return")
        count +=1
    if "Assessment year".lower() in page_data.lower():
        #print("Assessment Year")
        count +=1
    if "E-filing Acknowledgement Number".lower() or "E-tiling Acknowledgement Number".lower() in page_data.lower():
        #print("E-filing")
        count +=1
    if "Deductions under Chapter-VI-A".lower() in page_data.lower():
        #print("Deduction under Chapter-VI-A")
        count +=1
    if "Form No. which has been electronically transmitted".lower() in page_data.lower():
        #print("Form No.which has been electronically transmitted")
        count +=1
    if "Form No. which has been dectronically transmitted".lower() in page_data.lower():
        #print("Form No. which has been dectronically transmitted")
        count +=1
    if "Designation of AO".lower() in page_data.lower():
        #print("Designation of AO")
        count +=1
    if "Original or Revised".lower() in page_data.lower():
        #print("Original or Revised")
        count +=1
    if "E-filing Acknowledgement".lower() or "E-tiling Acknowledgement".lower() in page_data.lower():
        #print("E-filing Acknowledgement")
        count +=1
    if "Self Assessment Tax".lower() in page_data.lower():
        #print("Self Assessmenr Tax")
        count +=1
    if "Agriculture".lower() in page_data.lower():
        #print("Agriculture")
        count +=1
    if "Exempt Income".lower() in page_data.lower():
        #print("Exempt Income")
        count +=1
    if "Net Tax Payable".lower() in page_data.lower():
        #print("Net Tax Payable")
        count +=1
    if "Road/Street/Post Office".lower() in page_data.lower():
        #print("Road/Street/Post Office")
        count +=1
    if "transmitted electronically without digital signature".lower() in page_data.lower():
        #print("Transmitted electronically")
        count +=1
    if "transmitted dectronically without digital signature".lower() in page_data.lower():
        #print("Transmitted dectronically")
        count +=1
    if "centralized processing centre, income tax department, bengaluru 560500".lower() in page_data.lower():
        #3print("Centralized")
        count+=1
    print("ITRCOUNT",count)
    return count

def pay_slip(page_data):
    count=0
    if "Department".lower() in page_data.lower():
        count +=1
    if "Designation".lower() in page_data.lower():
        count +=1
    if "Emp. Code".lower() in page_data.lower():
        count +=1
    if "Employee Code".lower() in page_data.lower():
        count +=1
    if "Employee No".lower() in page_data.lower():
        count +=1
    if "Earning".lower() in page_data.lower():
        count +=1

    if "basic".lower() in page_data.lower():
        count +=1
    if "hra".lower() in page_data.lower():
        count +=1
    if "H.R.A".lower() in page_data.lower():
        count +=1
    if "PAN".lower() in page_data.lower():
        count +=1
    if "Mode of Pay".lower() in page_data.lower():
        count +=1

    if "Gross Pay".lower() in page_data.lower():
        count +=1
    if "Net Pay".lower() in page_data.lower():
        count +=1
    if "Gorss Salary".lower() in page_data.lower():
        count +=1
    if "Net Salary".lower() in page_data.lower():
        count +=1
    if "location".lower() in page_data.lower():
        count +=1
    if "doj".lower() in page_data.lower():
        count +=1
    if "Date oF Joining".lower() in page_data.lower():
        count +=1
    if "Payable Days".lower() in page_data.lower():
        count +=1
    if "Emp Code".lower() in page_data.lower():
        count +=1
    if "Emp ID".lower() in page_data.lower():
        count +=1

    if "Paid Days".lower() in page_data.lower():
        count +=1
    if "Payslip".lower() in page_data.lower():
        count +=1
    if "Pay Slip".lower() in page_data.lower():
        count +=1

    if "Total Earnings".lower() in page_data.lower():
        count +=1
    if "Joining Date".lower() in page_data.lower():
        count +=1
    if "Total Deductions".lower() in page_data.lower():
        count +=1
    if "Earnings".lower() in page_data.lower():
        count +=1
    if "Deductions".lower() in page_data.lower():
        count +=1
    if "Take Home Pay".lower() in page_data.lower():
        count +=1
    if "Payroll".lower() in page_data.lower():
        count +=1
    if "Employee Number".lower() in page_data.lower():
        count +=1
    if "Net Amount".lower() in page_data.lower():
        count +=1
    if "Parmanent Acount Number".lower() in page_data.lower():
        count +=1
    print("PAYSLIPCOUNT",count)
    return count


def f16_partA(page_data):
     #print("page_dataFI6",page_data)
    count=0
    if "FORM NO. 16[See rule 31(1)(a)]".lower() in page_data.lower():
        count +=1
    if "Certificate under Section 203 of the Income-tax Act".lower() in page_data.lower():
        count +=1
    if "Certificate under Section 203 of the Income tax Act".lower() in page_data.lower():
        count +=1
    if "Name and address of the Employer".lower() in page_data.lower():
        count +=1
    if "Name and address of the Employee".lower() in page_data.lower():
        count +=1
    if "Book Identification Number".lower() in page_data.lower():
        count +=1
    if "Challan Identification Number ".lower() in page_data.lower():
        count +=1
    if "PAN of the Deductor".lower() in page_data.lower():
        count +=1
    if "TAN of the Deductor".lower() in page_data.lower():
        count +=1
    if "PAN of the Employee".lower() in page_data.lower():
        count +=1
    if "See rule 31".lower() in page_data.lower():
        count +=1
    if "Income-tax Act, 1961".lower() in page_data.lower():
        count +=1
    if "PART A".lower() in page_data.lower():
        count +=4
    if "PARTA".lower() in page_data.lower():
        count +=4
    if "PART-A".lower() in page_data.lower():
        count +=4
    if "Last updated on".lower() in page_data.lower():
        count +=1
    if "Summary of amount paid".lower() in page_data.lower():
        count +=1
    if "Deducted at Source".lower() in page_data.lower():
        count +=1

    return count

def f16_partB(page_data):
    #print("page_dataf16partB",page_data)
    count=0
    if "PART-B".lower() in page_data.lower():
        #print("PART-B")
        count +=4
    if "PART B".lower() in page_data.lower():
        #print("PART B")
        count +=4
    if "PARTB".lower() in page_data.lower():
        #print("PART B")
        count +=4
    if "Details of Salary paid and any other income and tax deducted".lower() in page_data.lower():
        #print("PART B")
        count +=4
    if "Less:Allowance".lower() in page_data.lower():
        #print("PART B")
        count +=2
    if "Gross Salary".lower() in page_data.lower():
        #print("Gross Salary")
        count +=2
    if "Gross total income".lower() in page_data.lower():
        #print("Gross Total Income")
        count +=2
    if "Deductions under chapter VIA".lower() in page_data.lower():
        #print("Deduction under chapter VIA")
        count +=1
    if "Deductible Amount".lower() in page_data.lower():
        #print("Deductible Amount")
        count +=1
    if "Tax on total income".lower() in page_data.lower():
        #print("Tax on Total Income")
        count +=1
    if "Tax Payable".lower() in page_data.lower():
        #print("Tax Payable")
        count +=1
    if "Gross Amount".lower() in page_data.lower():
        #print("Gross Amount")
        count +=1
    if "Salary as per provisions contained in sec.17".lower() in page_data.lower():
        #print("Salary")
        count +=1
    if "Deduction".lower() in page_data.lower():
        #print("Salary Deductions")
        count +=1
    if "Details of Salary Paid".lower() in page_data.lower():
        #print("Details of Salary")
        count +=1
    if "profits in lieu of salary under section 17".lower() in page_data.lower():
        #print("profits in lieu of salary under section 17")
        count +=1
    if "allowance to the extent exempt us 10".lower() in page_data.lower():
        #print("allowance to the extent exempt us 10")
        count +=1
    if "allowance to the extent exempt under section 10".lower() in page_data.lower():
        #print("allowance to the extent exempt us 10")
        count +=1
    #print("PARTB COUNT",count)
    return count

def image_file_type_1(image_data):
    res_json={}
    if f16_partA(image_data.lower()) >9:
        res_json["parta_pageno"]=1
    if f16_partB(image_data.lower()) >8:
        res_json["partb_pageno"]=1
    if itr_ack(image_data.lower()) >8:
        res_json["itr_pageno"]=1
    if pay_slip(image_data.lower()) >6:
        res_json["payslip_pageno"]=1
    
    print("page Image type:",res_json)
    return res_json

def image_file_type(image_data,doc):
    res_json={}
    value = fi.find_part_b(doc)
    #print(value)
    if f16_partA(image_data.lower()) >9:
        res_json["parta_pageno"]=1
#    if f16_partB(image_data.lower()) >8
#        res_json["partb_pageno"]=1
    if itr_ack(image_data.lower()) >8:
        res_json["itr_pageno"]=1
    if pay_slip(image_data.lower()) >6:
        res_json["payslip_pageno"]=1
    if value != "No match":
        res_json["partb_pageno"]=value
    #print("page Image type:",res_json)
    return res_json


def remove_vertical_line(img):
    if len(img.shape) != 2:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    gray = cv2.bitwise_not(gray)
    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 15, -2)
    vertical = np.copy(bw)
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize =rows // 80
    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
    # Apply morphology operations
    vertical = cv2.erode(vertical, verticalStructure)
    vertical = cv2.dilate(vertical, verticalStructure)
    #cv2.imwrite("C:/OCR/vertical_lines_extracted.jpg", vertical)
    vertical_inv = cv2.bitwise_not(vertical)
    #cv2.imwrite("C:/OCR/inverse_extracted.jpg", vertical_inv)

    masked_img = cv2.bitwise_and(gray, gray, mask=vertical_inv )
    masked_img_inv = cv2.bitwise_not(masked_img)
    #cv2.imwrite("C:/OCR/masked_img.jpg", masked_img_inv)
    return masked_img_inv

def remove_vertical_line_lic(img):
    if len(img.shape) != 2:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    gray = cv2.bitwise_not(gray)
    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 15, -2)
    vertical = np.copy(bw)
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize =rows // 60
    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
    # Apply morphology operations
    vertical = cv2.erode(vertical, verticalStructure)
    vertical = cv2.dilate(vertical, verticalStructure)
    #cv2.imwrite("C:/OCR/vertical_lines_extracted.jpg", vertical)
    vertical_inv = cv2.bitwise_not(vertical)
    #cv2.imwrite("C:/OCR/inverse_extracted.jpg", vertical_inv)

    masked_img = cv2.bitwise_and(gray, gray, mask=vertical_inv )
    masked_img_inv = cv2.bitwise_not(masked_img)
    #cv2.imwrite("C:/OCR/masked_img.jpg", masked_img_inv)
    return masked_img_inv


def rotate_an_image(img_before,im_original):
    #print(img_before)
    #print(im_original)
    img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    #lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=100)
    angles = []
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)
        #print(angle)
    median_angle = np.median(angles)
    #print ("Angle is {}", format(median_angle))
    img_rotated = ndimage.rotate(im_original, median_angle)
    #cv2.imwrite("C:/OCR/masked_img_rotate.jpg", img_rotated)
    return img_rotated

def rotate_image_by_angle(im_original,median_angle):
    img_rotated = ndimage.rotate(im_original, median_angle)
    #cv2.imwrite("C:/OCR/masked_img_rotate.jpg", img_rotated)
    return img_rotated


def alignImages(im1, im2):
    # Convert images to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    cv2.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h

def assemble_word(word):
    assembled_word=""
    for symbol in word.symbols:
        assembled_word+=symbol.text
    return assembled_word

def find_word_location_json(document,word_to_find):
    res_json={}
    final_word=""
    match_count=0
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    #final_word+=assembled_word.lower()
                    if (assembled_word.lower()==word_to_find.lower()):
                        #max_y=max(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
                        res_json[str(match_count)]=word.bounding_box
                        match_count=match_count+1
                        #return word.bounding_box

    return res_json

def find_word_location_json_by_maxY(document,word_to_find,max_y_limit):
    res_json={}
    final_word=""
    match_count=0
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    #final_word+=assembled_word.lower()
                    if (assembled_word.lower()==word_to_find):
                        max_y=max(word.bounding_box.vertices[0].y,word.bounding_box.vertices[1].y,word.bounding_box.vertices[2].y,word.bounding_box.vertices[3].y)
                        if max_y < max_y_limit:
                            res_json[str(match_count)]=word.bounding_box
                            match_count=match_count+1
                            #return word.bounding_box

    return res_json

def find_word_location_json_by_minY(document,word_to_find,min_y_limit):
    res_json={}
    final_word=""
    match_count=0
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    #final_word+=assembled_word.lower()
                    if (assembled_word.lower()==word_to_find):
                        max_y=max(word.bounding_box.vertices[0].y,word.bounding_box.vertices[1].y,word.bounding_box.vertices[2].y,word.bounding_box.vertices[3].y)
                        if max_y > min_y_limit:
                            res_json[str(match_count)]=word.bounding_box
                            match_count=match_count+1
                            #return word.bounding_box

    return res_json


def find_word_location_json_by_maxY_minY(document,word_to_find,max_y_limit,min_y_limit):
    res_json={}
    final_word=""
    match_count=0
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    #final_word+=assembled_word.lower()
                    if (assembled_word.lower()==word_to_find):
                        max_y=max(word.bounding_box.vertices[0].y,word.bounding_box.vertices[1].y,word.bounding_box.vertices[2].y,word.bounding_box.vertices[3].y)
                        if max_y < max_y_limit and max_y>min_y_limit:
                            res_json[str(match_count)]=word.bounding_box
                            match_count=match_count+1
                            #return word.bounding_box

    return res_json


def find_word_location(document,word_to_find,param_one=1):
    res_json={}
    final_word=""
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    final_word+=assembled_word.lower()
                    if param_one==1 and ((assembled_word.lower()==word_to_find) or word_to_find in final_word):
                        return word.bounding_box
                    elif param_one==2 and (assembled_word.lower()==word_to_find):
                        return word.bounding_box

                if word_to_find in final_word:
                    return paragraph.bounding_box

def assemble_word_by_minmax_y(word,y_min,y_max):
    assembled_word=""
    for symbol in word.symbols:
        min_x=min(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
        max_x=max(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
        min_y=min(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
        max_y=max(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
        if(min_y >= y_min and max_y <= y_max):
            assembled_word+=symbol.text
    return assembled_word

def find_word_location_by_minmax_y(document,word_to_find,y_min,y_max):
    final_word=""
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word_by_minmax_y(word,y_min,y_max)
                    final_word+=assembled_word.lower()
                    if param_one==1 and ((assembled_word.lower()==word_to_find) or word_to_find in final_word):
                        return word.bounding_box
                    elif param_one==2 and (assembled_word.lower()==word_to_find):
                        return word.bounding_box
                if word_to_find in final_word:
                    return paragraph.bounding_box

def get_text_by_xy(document,x_min,x_max,y_min,y_max):
    final_word=""
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    min_x=min(word.bounding_box.vertices[0].x,word.bounding_box.vertices[1].x,word.bounding_box.vertices[2].x,word.bounding_box.vertices[3].x)
                    max_x=max(word.bounding_box.vertices[0].x,word.bounding_box.vertices[1].x,word.bounding_box.vertices[2].x,word.bounding_box.vertices[3].x)
                    min_y=min(word.bounding_box.vertices[0].y,word.bounding_box.vertices[1].y,word.bounding_box.vertices[2].y,word.bounding_box.vertices[3].y)
                    max_y=max(word.bounding_box.vertices[0].y,word.bounding_box.vertices[1].y,word.bounding_box.vertices[2].y,word.bounding_box.vertices[3].y)

                    if (min_x > x_min and max_x < x_max) and (min_y>y_min and max_y<y_max):
                        #print("(min_x > x_min and max_x <= x_max) and (min_y>=y_min and max_y<=y_max)=min_x,max_x,min_y,max_y",min_x,max_x,min_y,max_y)
                        assembled_word=assemble_word(word)
                        final_word+=' '+ assembled_word

    return final_word


def find_paragraph_location(document,word_to_find):
    #print("word_to_find paragraph_location",word_to_find)
    final_word=""
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                final_word=""
                for word in paragraph.words:
                    assembled_word=assemble_word(word)
                    final_word+=assembled_word.lower()
                    if(assembled_word.lower()==word_to_find) or word_to_find in final_word:
                        print("paragraph.bounding_box",paragraph.bounding_box)
                        return paragraph.bounding_box
                if word_to_find in final_word:
                    print(paragraph.bounding_box)
                    return paragraph.bounding_box


def crop_image(image_file,x1,y1,x2,y2,filePath):
    try:
        #print("FilePath",filePath)
        image = cv2.imread(image_file)
        w=x1+(x2-x1)
        h=y1+(y2-y1)
    #print(image_file)
        crop_img = image[y1:h,x1:w]
        #print("Crop_Image",crop_img)
        if crop_img!="":
            cv2.imwrite(filePath, crop_img)
    except:
        print("Exception occured at in cropping image","x1",x1,"y1",y1,"x2",x2,"y2",y2)

def resize_image(filename):
    #if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
    img = Image.open(filename) # image extension *.png,*.jpg
    new_width  = 685
    new_height = 1119
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    #print('filename:'+filename)
    img.save(filename) # format may what u want ,*.png,*jpg,*.gif

def resize_mfd_image(filename):
    #if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
    img = Image.open(filename) # image extension *.png,*.jpg
    new_width  = 1020
    new_height = 1406
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    #print('filename:'+filename)
    img.save(filename) # format may what u want ,*.png,*jpg,*.gif

def convert_tif_image(image_path,image_folder):
    img = Image.open(image_path)
    for i in range(img.n_frames):
        img.seek(i)
        filename= str(i)+".jpg"
        img.save(os.path.join(image_folder, filename))


def text_within(document,x1,y1,x2,y2):
    text=""
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        min_x=min(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
                        max_x=max(symbol.bounding_box.vertices[0].x,symbol.bounding_box.vertices[1].x,symbol.bounding_box.vertices[2].x,symbol.bounding_box.vertices[3].x)
                        min_y=min(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
                        max_y=max(symbol.bounding_box.vertices[0].y,symbol.bounding_box.vertices[1].y,symbol.bounding_box.vertices[2].y,symbol.bounding_box.vertices[3].y)
                        if(min_x >= x1 and max_x <= x2 and min_y >= y1 and max_y <= y2):
                            text+=symbol.text
                            if(symbol.property.detected_break.type==1 or
                               symbol.property.detected_break.type==3):
                                text+=' '
                            if(symbol.property.detected_break.type==2):
                                text+='\t'
                            if(symbol.property.detected_break.type==5):
                                text+='\n'
    return text

def remove_an_image_noise(image_folder,image_name):
    image_folder=image_folder
    print("image_folder",image_folder)
    print("image_name",image_name)
    # Read image with opencv
    src_path=os.path.join(image_folder, image_name)
    img = cv2.imread(src_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Write image after removed noise
    noise_file="noise_"+image_name
    noise_path=os.path.join(image_folder, noise_file)
    cv2.imwrite(noise_path, img)
    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # Write the image after apply opencv to do some ...
    #thres_file="thres_"+image_name
    #thres_path=os.path.join(image_folder, thres_file)
    #cv2.imwrite(thres_path, img)


def remove_image_Horizontal_Vertical_Line(img):
    if len(img.shape) != 2:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    gray = cv2.bitwise_not(gray)
    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(bw)
    vertical = np.copy(bw)

    # Specify size on horizontal axis
    cols = horizontal.shape[1]
    horizontal_size = cols / 20
    horizontal_size=int(horizontal_size)

    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))

    # Apply morphology operations
    horizontal = cv2.erode(horizontal, horizontalStructure)
    horizontal = cv2.dilate(horizontal, horizontalStructure)
    # Inverse horizontal image
    horizontal_inv = cv2.bitwise_not(horizontal)
    horiz_masked_img = cv2.bitwise_and(gray, gray, mask=horizontal_inv )
    horiz_masked_img_inv = cv2.bitwise_not(horiz_masked_img)

    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize = rows / 60
    verticalsize = int(verticalsize)

    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))

    # Apply morphology operations
    vertical = cv2.erode(vertical, verticalStructure)
    vertical = cv2.dilate(vertical, verticalStructure)
    # Inverse vertical image
    vertical = cv2.bitwise_not(vertical)
    #cv.imwrite('c:\\ocr\\sp\\image_vertInverse.jpg',vertical)

    masked_img = cv2.bitwise_and(gray, horiz_masked_img, mask=vertical )
    masked_img_inv = cv2.bitwise_not(masked_img)
    #cv2.imwrite("c:\\ocr\\sp\\vert_masked_img.jpg", masked_img_inv)
    return masked_img_inv







if __name__ == '__main__':
    # Read reference image
    #refFilename = "itr_aling_ref.jpg"
    #print("Reading reference image : ", refFilename)
    #imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    #directory="C:/OCR/api_itr_req/"
    #directoryOut="C:/OCR/api_itr_aligned/"
    im = cv2.imread("C:/OCR/sp/noise_test1.jpeg", cv2.IMREAD_COLOR)
    im_remove_vertical=remove_vertical_line_lic(im)
    cv2.imwrite("C:/OCR/sp/noise_test2.jpeg", im_remove_vertical)
    # Print estimated homography
    #print("Estimated homography : \n",  h)


# %%
