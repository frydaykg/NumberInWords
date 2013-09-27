from russianNamer import RusssianNamer

def test(num, s):
	namer = RusssianNamer()
	result = namer.name(num)
	if result == s:
		return 'Correct for %d -- %s' % (num, result)
	else:
		return 'Failed for %d. %s instead of %s' % (num, result, s)

print test(1, 'один')
print test(13, 'тринадцать')
print test(45, 'сорок пять')
print test(234, 'двести тридцать четыре')
print test(567, 'пятьсот шестьдесят семь')
print test(1234, 'одна тысяча двести тридцать четыре')
print test(123456, 'сто двадцать три тысячи четыреста пятьдесят шесть')
print test(343000123, 'триста сорок три миллиона сто двадцать три')
print test(4444, 'четыре тысячи четыреста сорок четыре')
