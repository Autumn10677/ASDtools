## ASDtools
This package relies heavily on **<a href="https://astroquery.readthedocs.io/en/latest/nist/nist.html" target="_blank">astroquery.nist's</a>** querying capabilities for loading spectral data for a given element over a range of wavelengths. The main advantage of **ASDtools** is its ability to format astroquery's default output into a formatted DataFrame. Additionally, I have made a handful of helpful tools for visualizing several pieces of the NIST ASD. This package's primary goal is to help users understand and visualize standard conventions in atomic spectroscopy.

## Installation
To install **ASDtools** on your device, run the following command on your system's terminal.
```
pip install ASDtools
```
If you have a previous version of **ASDtools** on your device and would like to upgrade to the latest official release, use the following command.
```
pip install --upgrade ASDtools
```
Currently, **ASDtools** has the following dependencies...
```
'astropy',
'astroquery',
'Fraction',
'ipython!=8.17.1,<9.0.0,>=8.13.0',
'matplotlib',
'numpy<2',
'pandas',
'periodictable',
'roman',
'sympy',
'tqdm'
```