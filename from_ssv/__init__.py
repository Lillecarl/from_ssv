"""Top-level package for from_ssv."""

__author__ = """Carl Hjerpe"""
__email__ = 'git@lillecarl.com'
__version__ = '0.1.0'

from munch import munchify
from typing import Any

def from_ssv(input: str, **kwargs) -> list[Any]:
  # Split input lines
  lines = input.splitlines()
  # Create header index
  header = { idx: name for idx, name in enumerate(lines[0].split()) }

  # Strip headers of whitespace
  if kwargs.get('stripheaders'):
    header = { k: v.strip().replace(" ", "") for k, v in header.items() }
  # turn headers into their lower counterpart
  if kwargs.get('tolower'):
    header = { k: v.lower() for k, v in header.items() }

  # Remove header from lines
  lines.pop(0)

  # Return list of munched dicts with header
  return [munchify({name: line.split()[idx] for idx, name in header.items()}) for line in lines]

