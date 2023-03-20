"""Top-level package for from_ssv."""

__author__ = """Carl Hjerpe"""
__email__ = 'git@lillecarl.com'
__version__ = '0.1.0'

from munch import munchify

def from_ssv(input: str, **kwargs):
  # List we'll return
  ssvlist: list[any] = list() # type: ignore
  # All returned lines
  lines = input.splitlines()
  # Get indexed header identifiers
  header = { key: value for key, value in enumerate(lines[0].split()) }

  # If stipheaders is true we trim away everything that isn't alphanumeric
  for k, v in header.items():
    if kwargs.get('stripheaders'):
      header[k] = ''.join(v for v in header[k] if v.isalnum())
    if kwargs.get('tolower'):
      header[k] = header[k].lower()


  # Remove header from processing
  lines.pop(0)

  # Go through all lines
  for line in lines:
    # Split line into array
    linesplit = line.split()
    # Create dict to stuff data into
    ssvdict: dict[str, str] = dict()

    # Loop header with index, add to dict with header value as key and line value as value
    for idx, name in header.items():
      ssvdict[name] = linesplit[idx]

    # muncify dict (dict with object style access) and add to list
    ssvlist.append(munchify(ssvdict))

  return ssvlist

