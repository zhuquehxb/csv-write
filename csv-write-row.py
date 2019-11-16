#python3.8
__AUTHOR_ = 'wangyong'
import csv
import os
import random

'''
 脚本功能：
 一次性读取csv文件中所有内容，然后清空该文件，关闭文件句柄。
 对文件内容进行处理，添加一列，然后按行逐次写入到该csv文件中。
 原本是用于nmon结果分析功能，打印各采样点数据的，个人觉得该方法没有按列写入好。
'''
filepath = os.getcwd()
csvfile_old = filepath + '\\test.csv'
#csvfile_new = filepath + '\\test_new.csv'
#print(csvfile_old + '\n' + csvfile_new)

csvnum = 0

csvfile = open(csvfile_old, 'r+')
rows = csvfile.readlines()		#一次性读取所有文件内容
csvfile.seek(0)
csvfile.truncate()		#清空文件，与seek(0)配合使用，否则可能出现truncate()无效
csvfile.close()		#关闭文件句柄

for line in rows:
	data_list = line.strip('\n').split(',')
	csv_add = random.randrange(88, 99, 2)
	data_list.append(str(csv_add))		#向读取的行最后序列添加一个随机数，或者其他字段
	#按行逐次写入到该csv文件中
	with open(csvfile_old, 'a', newline='') as f:		#还是在原来的文件中写入
		data_w = csv.writer(f)
		#print(data_list)
		data_w.writerow(data_list)
	f.close()
	svnum = csvnum + 1