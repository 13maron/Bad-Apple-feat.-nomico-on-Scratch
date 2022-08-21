# coding: utf-8 (maybe)
# class作るべきだったかも

width, height = 80, 60

def quantize(path="data.txt", amount=4): # pathは圧縮するテキストのパス, amountはどれだけ量子化するか(4だと4分の1)
	text = open(path, "r")
	quantized = open("quantized.txt", "w")
	q = []
	for line in text:
		quantizedLine = ""
		for i in range(width):
			quantizedLine += hex(int(int(line[i*2:i*2+2], 16)/(16*16/amount))*amount)[2:]
		quantized.writelines(quantizedLine + "\n")
	text.close()
	quantized.close()

def compress(path="quantized.txt"):
	text = open(path, "r")
	compressed = open("compressed.txt", "w")
	frame = ""
	for line in text:
		frame += line[:-1]
		if len(frame) == width*height:
			lineComp = ""
			pointer = 0
			while pointer < width*height:
				current = frame[pointer:pointer+1]
				nexCurr = frame[pointer+1:pointer+2]
				sameCntr = 1
				pointer += 1
				while current == nexCurr:
					pointer += 1
					nexCurr = frame[pointer:pointer+1]
					sameCntr += 1
				if sameCntr == width*height:
					lineComp = current + "00"
				elif sameCntr > 255: # 連続する個数を表す数値が3バイト以上になるのを防止
					while sameCntr > 255:
						lineComp += current + "ff"
						sameCntr -= 255
					lineComp += current + hex(sameCntr)[2:].zfill(2)
				else:
					lineComp += current + hex(sameCntr)[2:].zfill(2)
					
			compressed.writelines(lineComp + "\n")
			frame = ""
	
	text.close()
	compressed.close()
