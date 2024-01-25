#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import ConfigVariableString, ConfigVariableInt

base = ShowBase()

ConfigVariableString('notify-level-audio').setValue('debug')

ConfigVariableInt('audio-preload-threshold').setValue(5000000)

sound = loader.loadMusic("counting.ogg")

sound.setTime(5)
sound.play()

base.run()
