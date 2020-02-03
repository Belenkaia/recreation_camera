import cv2
import filework_functions as ff
import time
from time import sleep
from picamera import PiCamera
import network_cam as nf

camera = PiCamera()
while True:
    camera.start_preview()
    sleep(2)
    camera.capture('../frames/image.jpg')
    camera.stop_preview()


    classNames = {0: 'background', 1: 'person'}


    def id_class_name(class_id, classes):
        for key, value in classes.items():
            if class_id == key:
                return value

    #
    time_start = time.time()
    # Loading model
    model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph_mobile.pb',
                                          'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    image = cv2.imread(ff.find_last_shot_addr())

    image_height, image_width, _ = image.shape

    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
    output = model.forward()

    people_count = 0

    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .28:
            class_id = detection[1]
            class_name = id_class_name(class_id, classNames)
            if class_name == "person":
                people_count += 1
                box_x = int(detection[3] * image_width)
                box_y = int(detection[4] * image_height)
                box_width = int(detection[5] * image_width)
                box_height = int(detection[6] * image_height)
                human_x = int((box_x + box_width) / 2)
                human_y = int((box_y + box_height) / 2)

                '''cv2.circle(image,
                           (human_x, human_y),
                           8,
                           (0, 250, 0),
                           thickness=5)
                cv2.putText(image,
                            str(people_count),
                            (human_x, human_y),
                            cv2.FONT_HERSHEY_COMPLEX,
                            (.001 * image_width),
                            (0, 255, 255),
                            thickness=2)'''
                print("Human number ", people_count, " is in (", human_x, ", ", human_y, ")")
    time_end = time.time()
    print("Time of work in seconds: ", time_end - time_start)
    print("People count: ", people_count)

    nf.post_data(people_count, 0, 3204)

    """cv2.imshow('Processed image', image)
    cv2.imwrite("image_box_text.jpg", image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
