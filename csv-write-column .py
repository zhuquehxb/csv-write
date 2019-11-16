#python3.8
__AUTHOR__ = 'wangyong'

import csv
import random
import datetime

'''
	脚本用途：
	其主要目的用于对nmon原始文件的分析功能上，对cpu、内存、磁盘、网络等每个采样点进行计算后打印，帮助性能测试工程师分析测试过程中的服务器资源利用情况。
	根据实际情况需要，也可以用于其他用途
	利用python环境自带的csv开发包，实现数据按列写入到excel文件，但是又不想去下载其他excel开发插件（主要是懒），摸索了半天才找到这个简单的方案来实现按列写入。
'''

csvnum = 0
max_num = 100     #根据要统计的行数，根据实际情况定义
timestr = '2019-11-16 09:57:48'		#从nmon原始结果中分析得到nmon开始监控时间点
TIME = []
CPU = []
MEM = []
DISK = []
NET = []

TIME_format = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')

for csvnum in range(0, max_num):
	#初始化TIME列，便于手动绘制折线图
	time_end = (TIME_format + datetime.timedelta(seconds=10)).strftime("%H:%M:%S")		#timedelta()为增加或者减少时间，可以按hours、minutes、seconds来改变时间点
	TIME.append(str(time_end))

	CPU.append(str(random.randrange(70, 80, 2)))		#这里用随机值只是举个例子，具体根据实际情况来使用
	MEM.append(str(random.randrange(75, 90, 2)))
	DISK.append(str(random.randrange(600, 700, 2)))
	NET.append(str(random.randrange(600, 800, 2)))

	csvnum = csvnum + 1
	timestr = TIME[-1]		#获取TIME list最后序列，然后进行时间初始化
	TIME_format = datetime.datetime.strptime(timestr, '%H:%M:%S')

print(TIME)
print(CPU)
print(MEM)
print(DISK)
print(NET)

with open('write-col.csv', 'w', newline='') as csvfile:
	w_clo = csv.writer(csvfile)
	w_clo.writerow(['采样时间', 'CPU利用率(%)', '内存利用率(%)', '磁盘(io/s))', '网络(KB/S))'])
	w_clo.writerows(zip(TIME, CPU, MEM, DISK, NET))		#使用zip把TIME，CPU, MEM, DISK_IO, NET_KBS等4个list的数据按列存放，根据需要后面可加入其它列，比如cpu-usr、cpu-sys、disk-read、disk-write
	w_clo.writerow([''])
	w_clo.writerow(['注意：请性能测试工程师根据实际情况手动制作曲线图'])
	csvfile.close()