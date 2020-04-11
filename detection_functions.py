from camera_functions import Camera
import time
from constants import const
import cv2


def capture_and_recognize():
    Camera().capture_and_save(const.current_frame_path, 2)

    classNames = {0: 'background', 1: 'person'}

    def id_class_name(class_id, classes):
        for key, value in classes.items():
            if class_id == key:
                return value

    #
    time_start = time.time()

    image = cv2.imread(const.current_frame_path)
    image_height, image_width, _ = image.shape

    # Loading model
    model = cv2.dnn.readNetFromTensorflow(const.inference_graph_path, const.coco_config_path)
    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
    output = model.forward()

    people_count = 0

    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .2:
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

                cv2.circle(image,
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
                            thickness=2)
                print("Human number ", people_count, " is in (", human_x, ", ", human_y, ")")
    time_end = time.time()
    print("Time of work in seconds: ", time_end - time_start)
    print("People count: ", people_count)
    cv2.imwrite(const.detected_frame_path, image)
    return people_count
