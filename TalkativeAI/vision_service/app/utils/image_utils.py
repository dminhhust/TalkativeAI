import numpy as np
import cv2


def bytes_to_image(file_bytes):

    nparr = np.frombuffer(file_bytes, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    return img
