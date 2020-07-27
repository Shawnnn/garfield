Garfield, an incrementally improving dialog system for learning.

* `/versions`: diectory containing versions from older iterations.
* `/bots`: package containing all talking bots, inlcuding the base class `Bot`.
* `garfield.py`: system entry, integrator of all talking bots.

## Third-party Dependencies

* `pip install termcolor simpleeval`

## How to run?

* `python garfield.py` or `python -m garfield`

## How to test individual bot?

* `python -m bots.calc_bot`
