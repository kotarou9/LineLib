from line import LineClient, LineGroup, LineContact
import time
from task import _Task

class LineLib(object):
	def __init__(self):
		self._inst = None
		self.token = None
		self.cname = "Ubuntu"
		self.timeStarted = None
		self.sleep = 0.2
		self.autoAcceptInviteTimer = 20
		self.Login()

	def setInterval(self, interval, func, *args, **kw):
		"""
			runs every x seconds
			@interval: seconds until run
                	@func: function to call once interval has been reached 
                	@args: function arguments
			@example1: self.setInterval(3, function, pr1, pr2)
                	@example2: self.setInterval(3, function)
                	returns the task you can use this to cancel using the cancel() method
		"""
		task = _Task(interval, func, *args, **kw)
		task.interval()
		return task

	def setTimeout(self, interval, func, *args, **kw):
		"""
			@interval: seconds until run
			@func: function to call once interval has been reached
			@args: function arguments
			@example1: self.setTimeout(3, function, pr1, pr2)
			@example2: self.setTimeout(3, function)
			returns the task you can use this to cancel using the cancel() method
		"""
		task = _Task(interval, func, *args, **kw)
		task.timeout()
		return task

	def Login(self):
		try:
			self.onInit()
			self._inst = LineClient(authToken=self.token, com_name=self.cname)
			self.timeStarted = float(time.time())
			self.onLoginSuccessfull()
		except:
			self.onLoginFailure()

	def getRooms(self):
		return self._inst.rooms

	def getGroups(self):
		return self._inst.groups

	def getContacts(self):
		return self._inst.contacts
	
	def sendImage(self, recv, url):
		recv.sendImageWithUrl(url)

	def getRecentMessages(self, recv, count):
		return recv.getRecentMessages(count)

	def acceptAll(self):
		for grp in self.getGroups():
			try:
				grp.acceptGroupInvitation()
			except:
				pass
	def main(self):
		task = self.setInterval(self.autoAcceptInviteTimer, self.acceptAll)
		while True:
			task.do_all_tasks() # we use the loop to our avantage :)
			ops = []
			for op in self._inst.longPoll():
				ops.append(op)
			for op in ops:	
				sender = op[0]
				recv = op[1]
				message = op[2]
				self.onMessage(recv, sender, message)
				time.sleep(self.sleep)
	
		def onMessage(self, recv, user, msg):
			pass
			"""
				@recv: needed to send the message. It probably has other uses but, not sure yet.
				@user: this holds the user info 
				@msg: this holds the msg info
			"""
		def onLoginSuccessFull(self):
			pass
			"""
				basically says we were able to connect
			"""
		def onLoginFailure(self):
			pass
			"""
				basically it means we failed to connect
				most likely due to a bad token
			"""
		def onInit(self):
			pass
			"""
				this just allows us to set some params
			"""

		def cred(self):
			return """
This lib is based off of the Line lib created by Taehoon Kim.
Without his creation of the base of this lib line bots would have never started. You can find more information on his creation
here: https://carpedm20.github.io/line/
and here: https://github.com/carpedm20/line
So we thank you.
P.S: There may be some features we left out or didn't add.

"""
