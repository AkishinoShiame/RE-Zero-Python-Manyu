#!/usr/bin/python3
import argparse  # Command line parsing
#import textwrap # pretty text layout of support descriptrion
import csv

# argparse global
GlobalArg = argparse.ArgumentParser(prog="CSV変換君(*'▽')"#)
#GlobalArg = argparse.ArgumentParser(
                                    ,usage='使用例；csv2prettyDetailCSV.py input.csv output.csv'#)
#GlobalArg = argparse.ArgumentParser(
                                    ,description="""オリジナルCSVファイルを綺麗な形式に変換するツール。
                                    詳細の使い方は'csv2prettyDetailCSV.py input.csv output.csv。'""")
#GlobalArg = argparse.ArgumentParser(usage='使用例；csv2prettyDetailCSV.py input.csv output.csv')

GlobalArg.add_argument('in_file',help='希望変換ファイルの保存場所。' )
GlobalArg.add_argument('out_file',help='変換完成ファイルの保存場所。' )
#GlobalArg.add_argument('-h',help='使用例；csv2prettyDetailCSV.py input.csv output.csv')
#GlobalArg.add_argument('-help',help='使用例；csv2prettyDetailCSV.py input.csv output.csv')

filename = GlobalArg.parse_args()

#check origional file total
fil = open(filename.in_file, 'r')
total = len(fil.readlines())
fil.close()


with open(filename.in_file, 'r') as f:
    reader = csv.reader(f)
    FL = True

    # for write use
    wf = open(filename.out_file, 'w')
    #writer = csv.writer(wf, lineterminator='\n')
    # for write use

    #for process count
    process = 1
    
    print("進行状況（現在/全部）:　", process, "/", total)
    for row in reader:
        #print("進行状況（現在/全部）:　", process, "/", total)
        if FL == True:
            Frow = row[0] + ", " + row[1] + ", " + row[2] + ", ver, date, " + row[3] + ", " + row[4] + ", " + row[5] + "\n"
            wf.write(Frow)
            # ------ print(Frow)
            FL = False
            process += 1
            continue
        # Define fixed item ↓
        CPname = row[0]
        CPcpu = row[1]
        APPlst_raw = row[2]
        CPip = row[3]
        CPos = row[4]
        CPreport = row[5]

        APPlst = APPlst_raw.splitlines() 
        for item in APPlst:
            rawlst = item.replace("|",',')
            context_row = '"' + CPname + '","' + CPcpu + '",' + rawlst + ',"' + CPip + '","' + CPos + '","' + CPreport + '"\n'
            wf.write(str(context_row))
            # ------ print(context_row)
            process += 1
        #print("test1:", row[0])
        #process += 1
        print("進行状況（現在/全部）:　", process, "/", total)
    #finalized
    wf.close()
    print("変換成功！")
