#Libraries for image processing 
import cv2 as cv
import numpy as np
import pandas as pd
#Class which holds methods for features extraction
class features_extraction():
    '''cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()'''
    #Constructor to initialize image for feature extraction
    def __init__(self,image):
        self.img = image
    #This functio will return First Diagonal of matrix
    def diag_one(self):
        a,b = self.img.shape
        diagnal = np.zeros(a)
        k = 0
        for i in range(100):
            diagnal[k] = self.img[i][i]
            k += 1
        return diagnal
    #This function will return Second Diagonal of matrix
    def diag_two(self):
        a,b = self.img.shape
        diagnal = np.zeros(a)
        k = 0
        l = 99
        for i in range(100):
            diagnal[k] = self.img[i][l]
            k += 1
            l -= 1
        return diagnal
    #This fucntion will return sum of first thirty columns
    def Sum_first_thirty_col(self):
        sum = 0
        for i in range(100):
            for j in range(30):
                sum = sum + img[i][j]
        return sum 
    #This function will return sum last thirty columns
    def Sum_last_thirty_col(self):
        sum = 0
        for i in range(100):
            for j in range(70,100,1):
                sum = sum + img[i][j]
        return sum
    #This function will return sum first thirty rows
    def Sum_first_thirty_rows(self):
        sum = 0
        for i in range(30):
            for j in range(100):
                sum = sum + img[i][j]
        return sum
    #This function will return sum last thirty rows
    def Sum_last_thirty_rows(self):
        sum = 0
        for i in range(70,100,1):
            for j in range(100):
                sum = sum + img[i][j]
        return sum


if __name__ == "__main__":
    #Image is loaded for feature extraction 
    img = cv.imread('apple.jpg',0)
    #Initialzing the object for feature extraction 
    object1 = features_extraction(img)
    #Getting First Diagonal of matrix
    diag_1 = object1.diag_one()
    #Getting Second Diagonal of matrix
    diag_2 = object1.diag_two()
    #Sum First Diagonal
    sum_1 = np.sum(diag_1)
    #Sum Second Diagonal 
    sum_2 = np.sum(diag_2)
    #Average of First Diagonal
    avg_1 = sum_1/100
    #Average of Second Diagonal
    avg_2 = sum_2/100
    print(avg_1)
    print(avg_2)
    #Sum of first thirty columns
    sum_first_thirty_col = object1.Sum_first_thirty_col()
    #Average of first thirty colums
    avg_first_thirty_col = sum_first_thirty_col/3000
    #Sum of last thirty columns
    sum_last_thirty_col = object1.Sum_last_thirty_col()
    #Average of  ast thirty colums
    avg_last_thirty_col = sum_last_thirty_col/3000
    #Sum of first thirty rows
    sum_first_thirty_rows = object1.Sum_first_thirty_rows()
    #Average of first thirty rows
    avg_first_thirty_rows = sum_first_thirty_rows/3000
    #Sum of first thirty rows
    sum_last_thirty_rows = object1.Sum_last_thirty_rows()
    #Average of first thirty rows
    avg_last_thirty_rows = sum_last_thirty_rows/3000
    print(avg_first_thirty_col)
    print(avg_last_thirty_col)
    print(avg_first_thirty_rows)
    print(avg_last_thirty_rows)
    #Writing data in dictionary 
    data = {'Average Diagonal one':[avg_1],'Average Diagonal two':[avg_2],'Sum of Diagonal one':[sum_1],
            'Sum of Diagonal Two':[sum_2],'Average First Thirty Columns':[avg_first_thirty_col],
            'Average Last thirty columns':[avg_last_thirty_col],'Average First thirty Rows':[avg_first_thirty_rows],
            'Average Last thirty rows':[avg_last_thirty_rows]}
    dataframe = pd.DataFrame(data)
    dataframe.to_csv("Extracted Features.csv")

 
