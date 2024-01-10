import cv2
import numpy as np

# Load the certificate background image using cv2
certificate_image = cv2.imread("certification_image.png")

#Add Full Name dynamically
full_name = "john Doe"
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 1.5
color = (0, 0, 0)
thickness = 2

# Detrmine the text position
text_width, text_height = cv2.getTextSize(full_name, font, font_size, thickness)[0]
x = int((certificate_image.shape[1] - text_width) / 2) # center the text horizontally
y = int((certificate_image.shape[0] + text_width) / 2) # center the text vertically

#Add the text to the image
cv2.putText(certificate_image, full_name, (x,y), font, font_size, color, thickness)

#Add Logo dynamically
#logo = cv2.imread("logo.png")
#cv2.imshow("logo", logo)

#Add Date dynamically
date = "January 1, 2024"
x = int((certificate_image.shape[1] - text_width) / 4) # center the text horizontally
y = int((certificate_image.shape[0] + text_width) / 4) # center the text vertically
cv2.putText(certificate_image, date, (x,y), font, font_size, color, thickness)

#Save the final certificate image
cv2.imwrite("final_certificate.png", certificate_image)

#Display the final certificate image
cv2.imshow("certificate", certificate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()