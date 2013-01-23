PassGenerator
=============

This simple python script generate a diversity of random passwords relying on user's parameters. The password is not saved by this program, though it may be kept in your terminal session.

Running
-------

This program runs in Python 2, so if you use Python 3 it may not work. You need to grant the file PassGenerator.py permission to run directly. To do so, you can enter:

  `chmod 755 PassGenerator.py`

To run the program, now just type:

  `./PassGenerator.py [options]`

Options
-------

There are some option generating the password, explained as follows:

  **-d size**
    Defines the length of the password. (Default size=6)

  **-l**
    Excludes characters [a-zA-Z] from password.

  **-n**
    Exclude numbers from password.

  **-o**
    Exclude miscellaneous characters.

Author
------

  gerson23.
