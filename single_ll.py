#define the basic data structure node
class node(object):
	def __init__(self, key, value):
		self.data=value
		self.key=key
		self.next=None

#define the linked list structure
class ll(object):
	def __init__(self):
		self.head=None

	def insert(self,key,node_value):
		new_node=node(key,node_value)
		new_node.next=self.head
		self.head=new_node

	def delete(self):
		current=self.head
		self.head=current.next
		del current

	def reverse(self):
		prev=None
		current=self.head
		while(current is not None):
			next=current.next
			current.next=prev
			prev=current
			current=next
		self.head=prev

	#do not use keyword print	
	def print_ll(self):
		current=self.head
		while (current is not None):
			print current.data,
			current=current.next


	def search(self,key):
		current=self.head
		while(current is not None):
			if (key == current.key):
				print current.data
				return
			else:
				current = current.next
		print "NOT FOUND"
		return




