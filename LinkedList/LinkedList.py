class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def append(self, image):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = image
		else:
			self.head = image

	def get_position(self, position):
		pointer = 1
		current = self.head
		while current.next:
			if position == pointer:
				return current
			else:
				current = current.next
				pointer += 1
				if current.next == None and position == pointer:
					return current

	def len_link(self):
		temp = self.head
		count=0
		while temp:
			count+=1
			temp = temp.next
		return count