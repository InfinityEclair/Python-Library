import os
import datetime
while True:
    dir = input("検索したいディレクトリ:")
    try:
        files = os.walk(dir)
#        for s,t,u in files:
#            print("親:"+s)
#            for File in u:
#                print("ファイル:"+File)
        break
    except Exception as e:
        print(e)
while True:
    targ = input("検索したい曜日(0:月曜,1:火曜,2:水曜,3:木曜,4:金曜,5:土曜,6:日曜)")
    try:
        targ = int(targ)
        if 0<= targ <= 6:
            break
        else:
            print("曜日を1-6の数字で入れてください！")
    except:
        print("数字で入力してください！")

for s,t,u in files:
    print(s)
    for Files in u:
        try:
            if datetime.datetime.fromtimestamp(os.stat(s+"/"+Files).st_mtime).weekday() == targ:
                print(s+"/"+Files)
        except FileNotFoundError:
                print(s+"/"+Files+"というファイルが検出されましたが壊れているようです？")
        except Exception as e:
                print("エラー:"+e)