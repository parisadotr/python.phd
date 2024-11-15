dataproc, A postprocessing code for CAMEA neutron spectroscopy data
-------------------------------

Installation:
-------------
git clone git@github.com:arisadotr/CAMEA_dataprocess_main.git

cd CAMEA_dataprocess_main

pip install . 



Test installation:
------------------
dataproc


Run unit tests (requires pytest):
---------------------------------

cd tests

pytest --cov=pydec *py



Test code style quality (requires pylint and pycodestyle):
----------------------------------------------------------

pylint pydec tests example

pycodestyle */*.py


Run example:
------------

cd example

./run_me.sh


