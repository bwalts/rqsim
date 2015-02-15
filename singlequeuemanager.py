from Queue import Queue

class SingleQueueManager(object):
	
	__producers = 0
	__free_producers = 0
	__num_ticks = 0
	__q = Queue()
	__consumers = ""
	
	def __init__(self, num_producers, num_ticks):
		self.__producers = ["a"] * num_producers
		self.__free_producers = num_producers
		self.__num_ticks = num_ticks

	def add_consumers(self, consumers, consumer_bag):
		self.__consumers = consumers
		
	def run_simulation(self):
		for i in range(1, (__num_ticks + 1)):
			# deal with producers
			for producer in producers:
				if (producer == "a"):
					next
				else:
					producer.service_granted += 1
					if (producer.is_satisfied()):
						producer = "a"
						__free_producers += 1
			
			# deal with the queue
			if (not q.empty()):
				for producer in producers:
					if ((producer == "a") & (not q.empty())):
						producer = q.get()
			
			# check for incoming consumers and handle
			consumers_this_round = shift(__consumers)
			for consumer in consumers_this_round:
				if (__free_producers > 0):
					freeproducer_index = __producers.index("a")
					__producers[freeproducer_index] = consumer
					__free_producers -= 1
				else:
					q.add(consumer)
					
					
				
			