print("Input filename: ")
f = input()

class VideoConvert:
	def __init__(self, filename):
		self.filename = filename

		self.file = open(filename, 'rb')
		self.data = self.file.read()

		self.modFile = open("modified_" + filename, 'wb')

		jpegStart = self.data.find(b'\xff\xd8') #start section of a jpeg
		jpegEnd = self.data.find(b'\xff\xd9') #end section of a jpeg
		print(str(jpegStart) + " - " + str(jpegEnd))
		while jpegStart != -1 and jpegEnd != -1:
			print(str(jpegStart) + " - " + str(jpegEnd))
			
			length = jpegEnd - jpegStart + 2
			self.modFile.write(str(length).encode('utf-8'))
			self.modFile.write(self.data[jpegStart:jpegEnd+2])

			self.data = self.data[jpegEnd+2:]
			jpegStart = self.data.find(b'\xff\xd8')#start section of a jpeg
			jpegEnd = self.data.find(b'\xff\xd9') #end section of a jpeg
VideoConvert(f)
input()
