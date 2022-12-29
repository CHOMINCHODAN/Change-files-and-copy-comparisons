import os
import glob
import shutil

# 구상 방법

# 20220907_170124_23.png 이게 문자열
# 07 날짜를 바꾸고 싶으면
# 202209 / 07_ / 170124_23.png 3개로 자르고
# 02 -> 다른 문자열 넣어주고
# 다시 합치기

dir_path = '/media/rastech/T7/test_file/camera/'

filelist_1 = os.listdir(dir_path)
print(filelist_1)

aa = dir_path + 'aaa.png'
ndd = os.rename( aa , dir_path+'07'+'.png')

# for png_f in filelist_1:
#
#     new_png = dir_path_1hz + png_f
#     print(new_png)
#
#     yymm = dir_path_1hz + png_f[0:6]
#     print(os.path.realpath(yymm))
#
#     dd = dir_path_1hz + png_f[6:8]
#     print(os.path.realpath(dd))
#
#     ss = dir_path_1hz + png_f[8:]
#     print(os.path.realpath(ss))
#
#     ndd = os.rename( 'new_png' , '07')
#
#
#     # print(os.path.realpath(ndd))
#     newfile = yymm + dd + ss
#     print(os.path.realpath(newfile))


#  리스트 형태올 출력 된거 확인하였다.
# 타입 print를 통해서 타입이 list 인걸 확인 함
# len를 통해서 list 갯수 확인
# 변수 주고 그다음에  i[] arry에서 날짜 (일자) 자리수까지 출력 7번째
# 타입을 변경해준다.
# 일부만 변경해서 그런가 에러 메세지 발견..



