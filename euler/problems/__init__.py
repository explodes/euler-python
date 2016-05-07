import glob
import os
import re

# I tried to make this as ridiculous as possible. I'm sorry but I just couldn't resist.
# After it was built and working, I thought, I could do this in one line...
# I know it's bad. But it feels right.
#
# Load all problem modules (eulerXX.py) in order so the registry can collect modules.
[__import__('euler.problems.euler%d' % num) for num in
 sorted(int(re.search('euler(?P<num>\d+)\.py$', filename).group('num')) for filename in
        glob.iglob(os.path.join(os.path.dirname(__file__), 'euler*.py')))]
