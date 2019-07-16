Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-hue/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/hue/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_Hue.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_Hue
    :alt: Build Status

CircuitPython helper library for Philips Hue Lights.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython SimpleIO <https://github.com/adafruit/Adafruit_CircuitPython_SimpleIO>`_
* `Adafruit CircuitPython ESP32SPI <https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-hue/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-hue

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-hue

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-hue

Usage Example
=============

Load bridge username and IP Address from secrets.py file:

.. code-block:: python

    username = secrets['hue_username']
    bridge_ip = secrets['bridge_ip']
    my_bridge = Bridge(wifi, bridge_ip, username)

Enumerate all lights on the bridge

.. code-block:: python

    lights = my_bridge.get_lights()

Turn on a light

.. code-block:: python

    my_bridge.set_light(1, on=True)

Turn off a light

.. code-block:: python

    my_bridge.set_light(1, on=False)

Set a light to the color yellow (RGB)

.. code-block:: python

        color = my_bridge.rgb_to_hsb([255, 255, 0])
        my_bridge.set_light(1, hue=int(color[0]), sat=int(color[1]), bri=int(color[2]))

Set a group of lights to a predefined scene

.. code-block:: python

        my_bridge.set_group(1, scene='AB34EF5')

Set a group of lights to a predefined color

.. code-block:: python

        my_bridge.set_group(1, color)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Hue/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-hue --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
