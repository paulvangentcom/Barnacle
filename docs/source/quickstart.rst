**********
Quickstart
**********

Installation
============

github
~~~~~~
`Download latest release here <https://github.com/paulvangentcom/Barnacle>`_

:code:`python setup.py install`


Basic Example
=============
The package is easy to use. Load the module, select a preset, and it's good to go.

.. code-block:: python
	
	import barnacle #import module

	bar = barnacle.random() #either initialize bar object with a random animation
	bar = barnacle.load('zombie') #or with a specific preset (see docs for full list)

	for i in range(0, 101): #whatever loop you run
		bar.draw(i, 100) #give it current step, total steps, and the bar draws itself.
		#some time consuming task here
		

:code:`draw` expects two arguments:

- *currentstep*: The current step that needs to be drawn
- *totalsteps*: The total steps expected to be taken

Alternatively you can also get the bar as a string, in case you want more control:

.. code-block:: python

	for i in range(0, 101): #whatever loop you run
		bar_string = bar.update_bar(i, 100) #give it current step, total steps, and the bar draws itself.
		#now you are free to do anything you want with the string object, print it, eat it, cook it, whatever!
		
		#some time consuming task here


.. _kerasplugin:
		
Keras Plugin
============
Barnacle started off as a Keras plugin to make my long model fitting hours more bearable. This functionality is still available. Usage is also simple:

.. code-block:: python

	import keras #import keras first
	from barnacle import barnacle_keras #import barnacle keras plugin

	#you can select a preset and mode
	barnacle_keras.Progbar.preset = 'tableflip' #see docs for full list of presets, 'random' for random
	barnacle_keras.Progbar.random = True #whether to select a random progress bar every epoch

	#override Keras progbar class in memory
	keras.callbacks.Progbar = barnacle_keras.Progbar

	#build your model and fit as you usually would

		

Presets
=======
		
Find out what presets are available:

.. code-block:: python

	import barnacle
	#what presets are included?
	barnacle.print_presets()