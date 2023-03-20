#! /usr/bin/env python

"""Top-level package for from_ssv."""

__author__ = """Carl Hjerpe"""
__email__ = 'git@lillecarl.com'
__version__ = '0.1.0'

from munch import munchify
from typing import Any

def from_ssv(strin: str, **kwargs) -> list[Any]:
  # Split input lines
  lines = strin.splitlines()
  # We make a simple split for the header, if there are headers with spaces we're doomed either way
  header = { idx: name for idx, name in enumerate(lines[0].split()) }
  
  # lower header if configured
  if kwargs.get('tolower') or kwargs.get('lower'):
    header = { k: v.lower() for k, v in header.items() }

  # Store first line, strip leading spaces
  firstline = lines[0].lstrip()

  wordstarts: list[int] = list()

  for i in range(1, len(firstline)):
    curchar  = firstline[i]
    prevchar = firstline[i-1]

    if prevchar == " " and curchar != " ":
      wordstarts.append(i)

  # Add last pos as wordstart too because of how we're slicing
  wordstarts.append(len(firstline))

  lines.pop(0)
  rows = list()

  for line in lines:
    # Strip leading spaces from current data line
    line = line.lstrip()
    # If a line is empty we assume the list is over
    if line.isspace() or len(line) == 0:
      break

    # Set last wordstart to string length. This gives us all data for last column
    wordstarts[-1] = len(line)
    # line dictionary
    linedict: dict[str, str] = dict()
    # First word always starts at 0
    prev = 0
    # Slice line into one item per 
    for k, v in enumerate(wordstarts):
      # Slice line from previous word start to current word start
      lineslice = line[prev:v]
      # Lookup header, insert into dict with header as key and slice as value
      linedict[header[k]] = lineslice.rstrip()
      # Get ready for next word
      prev = v

    # Add munchified entry to 
    rows.append(munchify(linedict))

  return rows

