from LineLib import LineLib
import glob

class TestBot(LineLib):
	def onInit(self):
		self.token = "" # token to login
		self._commands = []
		self._modules = glob.glob('modules/*.py')
		self.prefix = "-"
		self.sleep = 0.5 # set sleep time hopefully stops banning from line
		self.autoInviteAcceptTimer = 20 # used to call acceptAll() every x seconds

	def onLoginSuccessfull(self):
		print("Connected to Line")
		index = self.reindex()
		if index: pass
		else: print(index)

	def onLoginFailure(self):
		# if token is invalid 
		print("Failed to login")

	def getCommand(self, cmd):
		# gets the command
		cmd = cmd.replace(self.prefix, '')
		print cmd
		for command in self._commands:
			if command.name.lower() == cmd.lower():
				return command
			else:
				return None

	def setCommand(self, *args, **kw):
		# sets the command from module file
		command = Command(*args, **kw)
		if command not in self._commands:
			self._commands.append(command)

	def clearCommands(self):
		self._commands = []


	def reindex(self):
		# reloads the command list
		try:
			self.clearCommands()
			commands = {}
			for file in self._modules:
				execfile(file, commands)
			for key, value in commands.iteritems():
				if key == "init":
					# passing self to function init so we 
					# can dynamically load commands
					value(self)
			return True


		except Exception as e:
			return "%s" % e

	def onMessage(self, recv, user, msg):
		# onMessage basically takes the server responses
		print(user.name, msg.text)
		data = msg.text.split(" ", 1)
		if len(data) ==1:
			cmd, args = data[0], ""
		else:
			cmd, args = data
		if cmd.startswith(self.prefix):
			cmd = self.getCommand(cmd)
			if cmd:
				if cmd.func:
					# if cmd is found we pass the needed params to the assigned command function
					cmd.func(self, recv, user, msg, args)

class Command(object):
	# this is basically for meta data but
	# this could be used for a possible ranking system
	# I recommand using the user id because the name can change 
	def __init__(self, command, desc, func):
		self.name = command
		self.desc = desc
		self.func = func
	

if __name__=="__main__":
	bot = TestBot()
	bot.main()
