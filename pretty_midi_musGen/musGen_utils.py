"""Utility functions for handling MIDI data in an easy to read/manipulate
format

"""
from __future__ import print_function

import mido
import numpy as np
import math
import warnings
import collections
import copy
import functools
import six

from .instrument import Instrument
from .containers import (KeySignature, TimeSignature, Lyric, Note,
                         PitchBend, ControlChange)
from .utilities import (key_name_to_key_number, qpm_to_bpm)
from .pretty_midi import *

# The largest we'd ever expect a tick to be
MAX_TICK = 1e7

def midi_to_array(filepath, normalize_tempo=True, restrict_ts=True):
    """

    :param filepath: file path to midi file
    :param normalize_tempo: if true, all songs will be imported with bpm of 120; else leave tempo alone
    :param restrict_ts: if true, only load songs with time signature of 4/4; else pass
    :return: numpy arrays of 128*2 (128 notes, start time and end time)
    """

    #