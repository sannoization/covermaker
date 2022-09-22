

def run():
    # print(cv2.__version__)
    background = cv2.imread('bg.jpg')
    overlay = cv2.imread('image.png')


    red = "красный"
    blue = "синий"
    green = "зеленый"
    # color1 = input()
    # color2 = input()
    #
    # if color1 != red or color1 != blue or color1 != green:
    #     print("ошибка")

    print("введите заголовок")
    # header_string = input("введите заголовок \n")
    header_string = "Лучший студенческий совет НГТУ \n им. Р. Е. Алексеева 2022"
    subheader_string = "Студенческий совет НГТУ"
    date_string = "13 октября"

    white = (255, 255, 255)
    header_coords = (475, 389)
    subheader_coords = (475, 700)
    date_coords = (1653, 700)

    result = cv2.addWeighted(background, 0.5, overlay, 0.5, 0)

    bold_font_path = "./Montserrat-ExtraBold.ttf"
    main_font_path = "./Montserrat-SemiBold.ttf"

    header = ImageFont.truetype(bold_font_path, 85)
    main_font = ImageFont.truetype(main_font_path, 49)

    img_pil = Image.fromarray(result)
    draw = ImageDraw.Draw(img_pil)
    draw.text(header_coords, header_string, font=header, fill=(255, 255, 255, 0))
    draw.text(subheader_coords, subheader_string, font=main_font, fill=(255, 255, 255, 0))
    draw.text(date_coords, date_string, font=main_font, fill=(255, 255, 255, 0))
    result = np.array(img_pil)

    cv2.imshow("result", result)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('res.jpg', result)


if __name__ == '__main__':
    import sys
    import os
    from PIL import Image, ImageFont, ImageDraw
    import cv2
    import numpy as np
    sys.path.append(os.path.join(sys.path[0], 'venv/'))
    run()
