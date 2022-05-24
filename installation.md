# Installations
## Dependencies
To build the NLLoc program make sure gcc, make, jdk, gmt, taup are installed and updated. If not installed, install with commands:

	sudo apt update
	sudo apt install gcc make gmt openjdk
	sudo snap install taup
References:
Taup: http://www.seis.sc.edu/TauP/

## TauP_NLL
Get TauP_NLL.jar file from http://alomax.free.fr/nlloc/java/TauP_NLL.jar
Add the path of the jar file to java CLASSPATH variable :

		export CLASSPATH="/home/../TauP_NLL.jar:$CLASSPATH"

To make this change permanent add the above command at the end of .bashrc file located at /home directory.
## NLLoc
Get the source code from http://alomax.free.fr/nlloc/soft7.00/index.html and extract it.

Go to the src folder where Makefile is located let it be "/home/../src" then Build the program with command:
make all

To run the program from other directories add the current path to the PATH variable.

	export PATH="/home/../src:$PATH"
	
To add directory to path for permanently add following at the end of .bashrc or .profile
file located in /home directory :

	if [ -d "/home/../src" ] ; then
	export PATH="/home/../src:$PATH"
	fi

## SeismicityViewer
Download SeismicityViewer jar file http://alomax.free.fr/seismicity/SeismicityViewer50.jar
Add the path of jar file to java CLASSPATH variable :
	
	export CLASSPATH="/home/../SeismicityViewer50.jar:$CLASSPATH"

To make this change permanent add the above command at the end of .bashrc file located at /home directory.

## PyGMT

Get MiniConda installer from https://docs.conda.io/en/latest/miniconda.html install using:

	bash “installerFileName”

Create an environment:

	conda create -n myenv --channel conda-forge pygmt
	conda activate myenv

Install numpy, scipy, pygmt, jupyter-notebook:

	conda install numpy pandas pygmt 
	pip install scipy jupyter-notebook

	pip install -U notebook-as-pdf
	pyppeteer-install

To deactivate conda environment:

	conda deactivate

To stop the auto-activation of the conda environment:

	conda config --set auto_activate_base false
