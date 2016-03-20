import time
def print_hi():
	print "hi"
class _Task:
        _task = list()
        def __init__(self, int=None, function=None, *args, **kw):
                self.int = int
                self.function = function
                self.args = args
                self.kw = kw
                self.now = time.time()
                self.mode = "timeout"

        def set(self):
                self._task.append(self)

        def timeout(self):
                self.set()

        def remove(self):
                self._task.remove(self)

        def cancel(self):
                if self in self._task:
                        self.remove()

        def interval(self):
                self.mode = "interval"
                self.set()

        def killall(self):
                for task in self._task:
                        task.cancel()

        def do_all_tasks(self):
                for task in self._task:
                        if task.mode == "interval":
                                now = int(time.time() - task.now)%60
				if now >= task.int:
					task.function(*task.args, **task.kw)
					task.now = time.time()


			elif task.mode == "timeout":
                                now = int(time.time() - task.now)%60
                                if now >= task.int:
                                        task.cancel()
                                        task.function(*task.args, **task.kw)
