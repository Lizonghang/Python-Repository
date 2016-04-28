# coding=utf-8
import sys, shelve

def store(db):
	'''
	Query user for data and store it in the shelf object
	'''

	pid = raw_input('Enter unique ID number: ')
	person = {}
	person['name'] = raw_input('Enter name: ')
	person['age'] = raw_input('Enter age: ')
	person['phone'] = raw_input('Enter phone number: ')

	db[pid] = person

def get(db):
	'''
	Query user for ID and desired field, and fetch the corresponding data from the shelf object
	'''

	pid = raw_input('Enter ID number: ')
	field = raw_input('Which to know? (name, age, phone): ').strip().lower()
        try:
            print field.capitalize() + ':' + db[pid][field]
        except KeyError:
            print u'无效的ID'

def help():
	print 'The available commands are:'
	print 'store   : Stores information about a person'
	print 'lookup  : Looks up a person from ID number'
	print 'quit    : Save changes and exit'
	print '?	   : Print these help message'

def command():
	return raw_input('Enter command (? for help): ').strip().lower()

def main():
    '''
    潜在的陷阱:
        shelve.open函数返回的对象并不是普通的映射，如下面例子所示:

        >>> import shelve
        >>> s = shelve.open('database.dat')
        >>> s['x'] = ['a', 'b', 'c']
        >>> s['x'].append('d')
        >>> s['x']
        ['a', 'b', 'c']
        
        当在shelve对象中查找的元素的时候，这个对象都会根据已经存储的版本进行重新构建，当将元素赋给某个键的时候它就被存储了。上述例子中执行的操作如下:
        · 列表['a', 'b', 'c']存储在键x下
        · 获得存储的表示，并且根据它来创建新的列表，而'd'被添加到这个副本中。修改的版本还没有被保存
        · 最终，再次获得原始版本-----没有'd'
        
        为了正确的使用shelve模块修改存储的对象，必须将临时变量绑定到获得的副本上，并且在它被修改后重新存储这个副本:
        >>> temp = s['x']
        >>> temp.append('d')
        >>> s['x'] = temp
        >>> s['x']
        ['a', 'b', 'c', 'd']
        
        Python2.4之后的版本还有个解决方法:将open函数的writeback参数设置为true.如果这样做，所有从shelve读取或者赋值到shelve的数据结构都会保存在内存(缓存)中，并且只有在关闭shelve的时候才写回到磁盘中。如果处理的数据不大，并且不想考虑这些问题，那么将writeback设为true(确保在最后关闭了shelve)的方法还是不错的.
    '''
    
	database = shelve.open('database.dat')
	try:
		while True:
			cmd = command()
			if cmd == 'store':
				store(database)
			elif cmd == 'lookup':
				get(database)
			elif cmd == '?':
				help()
			elif cmd == 'quit':
				return
	finally:
		database.close()

if __name__ == '__main__':
	main()
