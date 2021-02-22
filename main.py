import cv2
from pyzbar import pyzbar


# Main loop for reading function
def barcode_reader(frame):

    # Decodes QR / Barcodes from frame
    barcodes = pyzbar.decode(frame)
    cv2.putText(frame, "Recognized text: ", (10, 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)

    for barcode in barcodes:
        x, y, w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')

        # Put a rectangle at the detected code and displays decoded text
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, barcode_info, (10, 40), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 255), 1)

    return frame


if __name__ == '__main__':

    # Open camera
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = barcode_reader(frame)
        cv2.imshow('QR / BARCODE READER', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
