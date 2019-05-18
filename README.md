# Aicd

An acid pattern MIDI generator Max for Live device based on a maximum likelihood n-gram model.

![Aicd screenshot](https://github.com/mganss/Aicd/raw/master/screenshot.png)

[Demo on YouTube](https://youtu.be/y58dpdHuVms)

Download under [releases](https://github.com/mganss/Aicd/releases) or at [maxforlive.com](http://maxforlive.com/library/device/5158/aicd)

## Features

- Generate variable length patterns (1-64 steps)
- Save generated patterns as presets
- Influence randomness through temperature dial
- Choose velocity of unaccented steps (default 99, accented steps are always 127)
- Fold/zoom sequencer view
- View/edit pitch, velocity, slide, gate independently

## Usage

Drag device into a MIDI track and hit the acid smiley button. Generated patterns enter Live's undo history. 
If you like a pattern, <kbd>Shift-click</kbd> one of the preset boxes to save it as a preset.

### Default pitch

The untransposed C (no up/down) note is generated as MIDI note 36 (called C1 in Ableton, generating 32.7Hz). 
This is also what ABL3 and Phoscyon generate. For some other synths, you'll have to transpose an octave up.

## Model

The model was generated by training on a large number of patterns in ABL3 format (not in this repo) 
using the approach described by Joav Goldberg [here](http://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139).

To generate a model:

1. Run `patterns.csx` in a folder containing pattern files in ABL3 format, producing a single file `input_patterns.txt` 
which contains all patterns in a condensed format suitable for training.
2. Use the `TrainCharLm()` method from `model.csx` to generate a model and write it to a file as JSON:
```C#
// dotnet script .\model.csx -i
var lm = TrainCharLm("input_patterns.txt", 18);
var json = JsonConvert.SerializeObject(lm);
File.WriteAllText("lm.js", "var lm = " + json);
```
