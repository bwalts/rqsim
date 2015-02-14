class Consumer(object):

	service_time = 1
	wait_time = 0
	
	def __init__(self, service_time):
		self.service_time = service_time
	
if __name__ == '__main__':
	a_consumer = Consumer(4)
	a_consumer.wait_time += 1
	
	print ("created a consumer with service time of " +
		repr(a_consumer.service_time) +
		" and set its wait time to " +
		repr(a_consumer.wait_time))