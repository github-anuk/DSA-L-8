class Queuee:
    def __init__(self):
      self.queue=[]
    def display(self):
      print(self.queue)
    def enqueue(self,food):
      self.queue.append(food)
    def dequeue(self):
      if len(self.queue)>0:
        self.queue.pop(0)
      else:
        print("GIVE QUEUE FOOD ITS HUNGRY")
    def HOW_MUCH_QUEUE_HAS_ATE(self):
      print(len(self.queue))
queueue=Queuee()
queueue.enqueue(1)
queueue.enqueue(2)
queueue.enqueue(3)
queueue.enqueue(4)
queueue.enqueue(5)
queueue.enqueue(6)

queueue.display()
queueue.HOW_MUCH_QUEUE_HAS_ATE()

queueue.dequeue()
queueue.display()
queueue.HOW_MUCH_QUEUE_HAS_ATE()