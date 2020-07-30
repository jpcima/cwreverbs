#!/usr/bin/env python

SAMPLE = "ramp.wav"
#SAMPLE = "*sine"
#SAMPLE = "impulse.wav"
OSCILLATOR = "on"
#OSCILLATOR = "off"
REVERB_INPUT = 100
REVERB_TONE = 100
REVERB_DAMP = 0
REVERB_DRY = 50
REVERB_WET = 50
REVERB_PREDELAY = 0
REVERB_SIZES = [0, 50, 100]
REVERB_TYPES = [
    "large_hall",
    "mid_hall",
    "small_hall",
    "large_room",
    "mid_room",
    "small_room",
]


open('sfz/dry.sfz', 'w').write("""
<region>
sample=%s
oscillator=%s
""" % (SAMPLE, OSCILLATOR))

for type in REVERB_TYPES:
    for size in REVERB_SIZES:
        open('sfz/%s_size=%d.sfz' % (type, size), 'w').write("""
<region>
sample=%s
oscillator=%s

<effect>
type=fverb
reverb_input=%d
reverb_tone=%d
reverb_damp=%d
reverb_predelay=%d
reverb_dry=%d
reverb_wet=%d
reverb_size=%d
reverb_type=%s
""" % (SAMPLE, OSCILLATOR,
       REVERB_INPUT,
       REVERB_TONE,
       REVERB_DAMP,
       REVERB_PREDELAY,
       REVERB_DRY,
       REVERB_WET,
       size,
       type))

