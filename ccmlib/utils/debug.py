
import os

if 'PYDEBUG' in os.environ:
    from pdb import set_trace as bb
else:
    def bb(): pass
