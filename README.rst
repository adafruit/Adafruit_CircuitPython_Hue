Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-hue/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/hue/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Hue/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Hue/actions/
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

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
    python3 -m venv .venv
    source .venv/bin/activate
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

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/hue/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Hue/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
