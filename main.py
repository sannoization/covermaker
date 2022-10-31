import sys
import os
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np

def run(heading, date, result_image):
    # print(cv2.__version__)
    background = cv2.imread('bg.jpg')
    overlay = cv2.imread('image.png')

    header_coords = (475, 389)
    date_coords = (1653, 700)

    result = cv2.addWeighted(background, 0.5, overlay, 0.5, 0)

    bold_font_path = "resources/Montserrat-ExtraBold.ttf"
    main_font_path = "resources/Montserrat-SemiBold.ttf"

    header = ImageFont.truetype(bold_font_path, 85)
    main_font = ImageFont.truetype(main_font_path, 49)

    img_pil = Image.fromarray(result)
    draw = ImageDraw.Draw(img_pil)
    draw.multiline_text(header_coords, heading, font=header, fill=(255, 255, 255, 0))
    draw.multiline_text(date_coords, date, font=main_font, fill=(255, 255, 255, 0), align='right')
    result = np.array(img_pil)

    #show result
    # cv2.imshow("result", result)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    cv2.imwrite(result_image, result)
