#This example will load libraries to have a visual output.
#Replace your apikey and the phone number you want to fetch the picture for


import cv2
import numpy as np
import sys
from io import BytesIO
from PIL import Image
from wascraper import wa_profilepic, wa_picobj

apikey = "replace_with_your_apikey"
phone = 34645785851
resp = wa_profilepic(phone, apikey,"png","high").content
img = np.array(Image.open(BytesIO(resp)))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = wa_picobj(phone, apikey)
detected_value = result['detected']
print("\n\n This is what I've found in the picture\n")
print(detected_value)

print("Click on picture window and press ESC to finish")
cv2.imshow("Sheep", img)
cv2.waitKey(0)
sys.exit() # to exit from all the processes
cv2.destroyAllWindows() # destroy all windows
