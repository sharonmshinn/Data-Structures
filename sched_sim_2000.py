
from linkqueue import Queue

class Task:

    tasks_created = 0

    def __init__(self,workload,arrival_time):
        self.id = Task.tasks_created
        Task.tasks_created += 1
        self.workload = workload
        self.remaining_workload = workload
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time
        
    def do_work(self):
        self.remaining_workload -= 1

    def is_done(self):
        return self.remaining_workload == 0

    def __repr__(self):
        return f"Task{self.id}: {self.remaining_workload}/{self.workload}"

def simulate(arrival_queue,quantum):
    process_queue = Queue()

    tick = 0
    active_task = None

    while active_task or not arrival_queue.is_empty() or not process_queue.is_empty():
        
        # add tasks from arrival queue
        while not arrival_queue.is_empty() \
              and tick == arrival_queue.first().get_arrival_time():
            arriving_process = arrival_queue.dequeue()
            print(f"Tick {tick}: {arriving_process} arrives")
            process_queue.enqueue(arriving_process)

        # do the thing
        if active_task is None and not process_queue.is_empty():
            active_task = process_queue.dequeue()
            print(f"Tick {tick}: {active_task} enters processor")
            print(f"\tQueue state: {process_queue}")
            quantum_left = quantum
        
        if active_task is not None:
            active_task.do_work()
            quantum_left -= 1
            if active_task.is_done():
                print(f"Tick {tick}: {active_task} completes")
                active_task = None
            elif quantum_left == 0:
                print(f"Tick {tick}: {active_task} completes its quantum")
                process_queue.enqueue(active_task)
                active_task = None
        
        tick += 1
    

def main():
    arrival_queue = Queue()
    arrival_queue.enqueue(Task(50,0))
    arrival_queue.enqueue(Task(50,0))
    arrival_queue.enqueue(Task(70,5))
    arrival_queue.enqueue(Task(20,10))
    arrival_queue.enqueue(Task(20,15))
    arrival_queue.enqueue(Task(50,20))
    arrival_queue.enqueue(Task(20,25))
    simulate(arrival_queue,8)

if __name__ == "__main__":
    main()
