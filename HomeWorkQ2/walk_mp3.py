import os, hashlib

def openFile(fileName):
	try:
		f1 = open(fileName, mode='rb')
		data = f1.read()
		#enc_data = data.encode()
		f1.close()
		return data #enc_data
	except Exception as e:
		print(e)

def mp3List(proot):
	mp3_list = []
	try:
		for (root, dirs, files) in os.walk(proot):
			for file in files:
				if file.endswith('.mp3'):
					path = os.path.join(root, file)
					mp3_list.append(path)
		return mp3_list
	except Exception as e:
		print(e)

def checksumDuplicate(mp3_list):
	d = {}

	for song in mp3_list:
		enc_data = openFile(song)
		md5 = hashlib.md5(enc_data)
		md5_res = md5.hexdigest()
		if md5.hexdigest() not in d:
			d[md5_res] = [song]
		else:
			d[md5_res].append(song)
		
	for k, v in d.items():
		if len(v) > 1:
			print()
			print('DUPLICATES')
			for x in v:	
				print(x)

root_path = input('enter root folder path: ') #root folder in which search is to be done

if os.path.isdir(root_path):
	mp3_list = mp3List(root_path) 
	print('**** list of .mp3 files ****')
	for i in mp3_list:
		print(i)
	print('\n')
else:
	print('wrong path entered')

checksumDuplicate(mp3_list)