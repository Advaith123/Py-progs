# import cv2
# import matplotlib.pyplot as plt
# path = r"C:\Users\USER\Desktop\Project\Sample Images\dots.jpg"
# gray = cv2.imread(path, 0)
# # plt.imshow(gray)
# # plt.show()
# th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
# cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
# #filtering by area
# s1 = 3
# s2 = 20
# xcnts = []
# for cnt in cnts:
#         if s1<cv2.contourArea(cnt)<s2:
#             xcnts.append(cnt)
# print("\nDots number: {}".format(len(xcnts)))
def bubbleSort(arr):
    n = len(arr)


    for i in range(n):

        for j in range(0, n - i - 1):


            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),