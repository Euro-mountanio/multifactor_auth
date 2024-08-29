from pyzbar.pyzbar import decode
import numpy as np
import cv2 
import pyzbar.pyzbar

class QRcode:
    def __init__(self):
        pass
    def reader(img):
        for barcode in decode(img):
                barcodeData = barcode.data.decode('utf-8')
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts], True, (255,0,255),5)
                pts2 = barcode.rect
                #cv2.putText(img, barcodeData,(pts2[0]),(pts2[1]),0.9,(255,0,255), 2)
                data = barcodeData.data
                return data
    def decoder(img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.pyzbar.decode(gray_img)
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcode_info = barcode.data.decode('utf-8')
            cv2.putText(img, barcode_info, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)

            #print(barcode_info)

        return img
