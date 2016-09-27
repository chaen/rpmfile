import os
import errno
import pprint
import rpmfile
import sys

rpm = rpmfile.open(sys.argv[1])
pprint.pprint(rpm.headers)

for m in rpm.getmembers():
  print m.name
  continue
  try:
    os.makedirs(os.path.join('sub', os.path.dirname(filename)))
  except OSError as exc:
    if exc.errno != errno.EEXIST:
      raise 
  with open(os.path.abspath('./sub/' + filename), 'wb') as f:
    f.write(rpm.extractfile(m).read())

