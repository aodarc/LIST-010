import requests
import uuid

urlList = ['http://www.mmf.lnu.edu.ua/media/k2/items/cache/537eafaab0a4c0a227d88cc02e4492cf_XL.jpg',
			'https://habr.com/post/210238/' ,
			'http://docs.python-requests.org/en/master/_static/requests-sidebar.png',
			'http://www.mmf.lnu.edu.ua/ar/1743',
			'http://www.mmf.lnu.edu.ua/images/stories/articles/181015m28.jpg',
			'https://images.unsplash.com/photo-1535498730771-e735b998cd64?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80']

typeList = ['image/jpeg','image/png']

class ImageDownloader:

	DEFAULT_TYPES = ['image/jpeg','image/png','image/jpg', 'image/gif', 'image/psd']
	DEFAULT_MAX_FILE_SIZE = 5242880

	def __init__(self, urlList = [], typeList = DEFAULT_TYPES, size = DEFAULT_MAX_FILE_SIZE):
		self.urlList = urlList
		self.typeList = typeList
		self.size = size

	def sizeChecker(self, size):
		if int(size or 0) <= self.size:
			return True
		else:
			print('File size is too large')
			return  False

	def typeChecker(self, filetype):
		return True if filetype in self.typeList else False

	def saveImage(self, url):
		response = requests.get(url)
		img_data = response.content
		rType = response.headers.get('Content-Type')
		rSize = response.headers.get('Content-Length')
		isSizeValid = self.sizeChecker(rSize)
		isTypeValid = self.typeChecker(rType)

		if (response.status_code == 200) and isSizeValid and isTypeValid:
			filename = 'file_' + str(uuid.uuid4())
			with open(filename + '.jpg', 'wb') as file:
				file.write(img_data)
		else:
			print ("It's not image" )

	def saveImages(self, urlList = []):
		urlList = urlList or self.urlList
		for url in urlList:
			self.saveImage(url)

downloader1 = ImageDownloader(urlList, typeList)
downloader1.saveImages()