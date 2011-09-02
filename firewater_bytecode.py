#! /usr/bin/env python
#
#	firewater_bytecode.py	WJ111
#
#   firewater by Walter de Jong <walter@heiho.net> (c) 2011
#
#   firewater COMES WITH NO WARRANTY. firewater IS FREE SOFTWARE.
#   firewater is distributed under terms described in the GNU General Public
#   License.
#

class ByteCode:
	'''holds the bytecode from which the output statements will be generated'''
	
	TYPE_RULE = 1
	TYPE_POLICY = 2
	TYPE_CHAIN = 3
	TYPE_ECHO = 4
	TYPE_VERBATIM = 5
	
	TYPES = ('None', 'rule', 'policy', 'chain', 'echo', 'verbatim')
	
	def __init__(self):
		self.type = None
	
	def set_rule(self, filename, lineno, allow, proto, src, src_port, dest, dest_port, iface):
		self.type = ByteCode.TYPE_RULE
		self.filename = filename
		self.lineno = lineno
		self.allow = allow
		self.proto = proto
		self.src = src
		self.src_port = src_port
		self.dest = dest
		self.dest_port = dest_port
		self.iface = iface
	
	def set_policy(self, filename, lineno, chain, policy):
		self.type = ByteCode.TYPE_POLICY
		self.filename = filename
		self.lineno = lineno
		self.chain = chain
		self.policy = policy
	
	def set_chain(self, filename, lineno, chain):
		self.type = ByteCode.TYPE_CHAIN
		self.filename = filename
		self.lineno = lineno
		self.chain = chain
	
	def set_echo(self, filename, lineno, str):
		self.type = ByteCode.TYPE_ECHO
		self.filename = filename
		self.lineno = lineno
		self.str = str
	
	def set_verbatim(self, filename, lineno, arr):
		self.type = ByteCode.TYPE_VERBATIM
		self.filename = filename
		self.lineno = lineno
		self.text_array = arr[:]


# EOB