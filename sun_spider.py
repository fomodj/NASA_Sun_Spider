import requests
import os
import datetime
import time
import random

folder_path = 'K:/DownSpace/sun_images/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹

start = '2019-06-07'
end = '2020-06-08'

datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
dateend = datetime.datetime.strptime(end, '%Y-%m-%d')

while datestart < dateend:
	datestart += datetime.timedelta(days=1)
	data = str(datestart.strftime('%Y/%m/%d/'))
	data1 = data.replace('/', '')
	url = 'https://sdo.gsfc.nasa.gov/assets/img/browse/' + data + data1 + '_001500_1024_HMIIC.jpg'

	response = requests.get(url)
	con = response.content
	img_name = folder_path + str(data1) +'.jpg'

	with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
		file.write(con)
		file.flush()
		file.close()  # 关闭文件
	time.sleep(random.randint(1,3))
	print('日期为{}的太阳图片下载完毕！'.format(data1))
print("{}至{}的太阳图片已爬取完成！！！".format(start,end))
