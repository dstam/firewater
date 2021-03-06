#
#   firewater/globals.py    WJ111
#
#   firewater by Walter de Jong <walter@heiho.net> (c) 2012
#
#   firewater COMES WITH NO WARRANTY. firewater IS FREE SOFTWARE.
#   firewater is distributed under terms described in the GNU General Public
#   License.
#

'''firewater global variables'''

VERSION = '1.3-beta'

DEBUG = False
VERBOSE = False

# dictionary holding interface aliases and groups
INTERFACES = {'all': []}

# dictionary with host and network range aliases
HOSTS = {'any': ['0.0.0.0/0'],
         'everybody': ['0.0.0.0/0']}

# dictionary with user-defined ServiceObjects
SERVICES = {}

# static list of known protocols
KNOWN_PROTOCOLS = ('tcp', 'udp', 'ip', 'icmp', 'gre')

# static list of known modules
KNOWN_MODULES = ('iptables')

# currently selected module
MODULE = 'iptables'

# cache of parsed rules
# the final output is generated from this bytecode
BYTECODE = []

# array of defines
DEFINES = []

# EOB
