import namer

class RusssianNamer(namer.Namer):
	digs = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
	digsRod = ['', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
	
	elevens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемьнадцать', 'девятнадцать']
	decs = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдеcят', 'восемьдесят', 'девяносто']
	hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
	
	highNames = {6:'миллион', 9:'миллиард', 12:'триллион', 15:'квадриллион', 18:'квинтиллион', 21:'секстиллион', 24:'септиллион', 27:'октиллион', 30:'нониллион', 33:'дециллион'}

	def __getDecsName(self, num, isRod = False):
		myDigs=[]
		
		if isRod:
			myDigs = self.digsRod
		else:
			myDigs = self.digs

		if num<10:
			return myDigs[num]
		elif num<20:
			return self.elevens[num - 10]
		else:
			return self.decs[num/10] + ' ' + myDigs[num%10]

	def __getHundredsName(self, num, isRod = False):
		if num/100:
			return '%s %s' % (self.hundreds[num/100], self.__getDecsName(num%100, isRod))
		return self.__getDecsName(num % 100, isRod)
			
	def __getThousandsName(self, num):
		if num % 10 == 1 and num % 100 != 11:
			return '%s тысяча' % self.__getHundredsName(num, isRod = True)
		elif num % 10 in (2, 3, 4) and num % 100 not in (12, 13, 14):
			return '%s тысячи' % self.__getHundredsName(num, isRod = True)
		else:
			return  '%s тысяч' % self.__getHundredsName(num)

	def __getHighsName(self, num, power):
		isRod= False		
		if num % 10 == 1 and num % 100 != 11:
			suffix = ''
		elif num % 10 in (2, 3, 4) and num % 100 not in (12, 13, 14):
			suffix = 'а'
			isRod = True
		else:
			suffix = 'ов'
			
		return '%s %s%s' % (self.__getHundredsName(num, isRod = isRod), self.highNames[power], suffix)

	def name(self, num):
		if num<=0 or num>=10**36:
			return None
			
		result = []
		for power in range(max(self.highNames), min(self.highNames)-1, -3):
			n = (num / 10**power) % 1000
			if n:
				result.append(self.__getHighsName(n, power))

		if (num / 1000) % 1000:
			result.append(self.__getThousandsName((num / 1000) % 1000))

		if num % 1000:
			result.append(self.__getHundredsName(num % 1000))
		
		if result:
			return ' '.join(result)
