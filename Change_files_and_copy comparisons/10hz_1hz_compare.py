import csv
import os.path
import shutil

# f = open('out.csv', 'w')
# csv_filename = 'out.csv'
# for (root, directories, files) in os.walk(dir_path):
#     for file in files:
#         file_path = os.path.join(root, file)
#         print(file_path)

# 비교 png
dir_path_10hz_png = '/media/rastech/Elements/2022_09_05/rosbag2_2022_09_14-15_54_56_E/lidar/'
dir_path_1hz_png = '/media/rastech/T7/all_정제데이터/DCC/정제데이터(20220914_DCC)/rosbag2_2022_09_14-15_54_56_E/lidar/'

# 비교 pcd
# dir_path_10hz_pcd = '/media/rastech/T7/test_file/10hz_pcd/'
# dir_path_1hz_pcd = '/media/rastech/T7/test_file/1hz_pcd/'


filelist_10_png = os.listdir(dir_path_10hz_png)
filelist_1_png = os.listdir(dir_path_1hz_png)

# filelist_10_pcd = os.listdir(dir_path_10hz_pcd)
# filelist_1_pcd = os.listdir(dir_path_1hz_pcd)

# 10hz =/ 1hz png
for i in filelist_1_png: # 1hz
    if i not in filelist_10_png: # 10hz 리스트와 비교

        ni = dir_path_1hz_png + i  # 상대 경로 변경

        shutil.copy( ni, '/media/rastech/T7/copy_png_pcd/') # 항상 for문 안에 넣는거 주의 디렉토리 위치 정하고 복사해서 넣지


        # print(os.path.realpath(ni))  # 경로 확인
        print(i)

# for i in filelist_1_pcd:  # 1hz
#     if i not in filelist_10_pcd:  # 10hz 리스트와 비교
#
#         ni = dir_path_1hz_pcd + i  # 상대 경로 변경
#
#         shutil.copy(ni, '/media/rastech/T7/test_copy_pcd/')  # 항상 for문 안에 넣는거 주의 디렉토리 위치 정하고 복사해서 넣지
#
#         # print(os.path.realpath(ni))  # 경로 확인
#         print(i)



