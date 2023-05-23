# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 18:08
# @Author  : Kenny Zhou
# @FileName: check_file.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com


import struct


# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
def typeList():
	return {
		"FFD8FF": "jpg",
		"89504E47": "png",
		"47494638": "gif",
		"49492A00": "tif",
		"424D": "bmp",
		"41433130": "dwg",
		"38425053": "psd",
		"7B5C727466": "rtf",
		"3C3F786D6C": "xml",
		"68746D6C3E": "html",
		"44656C69766572792D646174653A": "eml",
		"CFAD12FEC5FD746F": "dbx",
		"2142444E": "pst",
		"D0CF11E0": "xls.or.doc",
		"5374616E64617264204A": "mdb",
		"FF575043": "wpd",
		"252150532D41646F6265": "eps.or.ps",
		"255044462D312E": "pdf",
		"AC9EBD8F": "qdf",
		"E3828596": "pwl",
		"504B0304": "zip",
		"52617221": "rar",
		"57415645": "wav",
		"41564920": "avi",
		"2E7261FD": "ram",
		"2E524D46": "rm",
		"000001BA": "mpg",
		"000001B3": "mpg",
		"6D6F6F76": "mov",
		"3026B2758E66CF11": "asf",
		"4D546864": "mid",
		"4D5A": "pe"
	}


# 字节码转16进制字符串
def bytes2hex(bytes):
	num = len(bytes)
	hexstr = u""
	for i in range(num):
		t = u"%x" % bytes[i]
		if len(t) % 2:
			hexstr += u"0"
		hexstr += t
	return hexstr.upper()


# 获取文件类型
def filetype(filename):
	binfile = open(filename, 'rb')  # 必需二制字读取
	tl = typeList()
	ftype = 'unknown'
	for hcode in tl.keys():
		numOfBytes = len(hcode) // 2  # 需要读多少字节
		binfile.seek(0)  # 每次读取都要回到文件头，不然会一直往后读取
		hbytes = struct.unpack_from("B" * numOfBytes, binfile.read(numOfBytes))  # 一个 "B"表示一个字节
		f_hcode = bytes2hex(hbytes)
		if f_hcode == hcode:
			ftype = tl[hcode]
			break
	binfile.close()
	return ftype


if __name__ == '__main__':
	print(filetype(
		"/Users/kennymccormick/Downloads/1628676275407691777.jpg"))
