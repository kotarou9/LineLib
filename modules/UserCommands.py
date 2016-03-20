def say(self, recv, user, msg, args):
    recv.sendMessage("[%s]" % args)
