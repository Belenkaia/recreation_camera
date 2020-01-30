import os
import pathlib

images_dir_path = os.path.abspath(os.getcwd()) + '/images'
scp_command = 'sshpass -p "password" scp pi@192.168.1.102:proba/* ' + images_dir_path

def download_images_script():

    os.system(scp_command)


def get_number_of_image(filename):
    return int(filename[-13:-4])


def find_last_shot_addr():
    path_img = pathlib.PosixPath(images_dir_path + '/')
    files_list = os.listdir(path_img)
    last_file = (0, '')
    for addr in files_list:
        #print(get_number_of_image(addr))
        number_of_file = get_number_of_image(addr)
        if number_of_file > last_file[0]:
            last_file = (number_of_file, addr)
    return last_file[1]


#print(find_last_shot_addr())
