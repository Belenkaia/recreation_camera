import os


class constants:
    # work_dir = os.getcwd()
    frames_folder = 'frams'
    current_frame_name = 'image.jpg'
    current_frame_path = os.path.join(frames_folder, current_frame_name)

    models_folder = 'models'
    inference_graph_path = os.path.join(models_folder, 'frozen_inference_graph.pb')
    coco_config_path = os.path.join(models_folder, 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    recreation_server_endpoint = 'http://192.168.1.64:8080/recreation/api/data'
    device_type = 0
    zone_id = 3204

const = constants()