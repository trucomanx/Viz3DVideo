#!/usr/bin/python3

"""
Subpackage for surface visualizations (viz3dvideo.surf).

Provides functions to animate surfaces by following a camera path
or by rotating around the object.
"""

from .path import animate_path
from .rotate import animate_rotate

__all__ = ["animate_path", "animate_rotate"]
