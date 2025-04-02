from setuptools import setup

setup(
    name='ASDtools',
    version='0.1',
    author='Autumn Stephens',
    author_email='aust8150@colorado.edu',
    packages=['ASDtools'],
    install_requires=['astropy',
                      'astroquery',
                      'Fraction',
                      'ipython!=8.17.1,<9.0.0,>=8.13.0',
                      'matplotlib',
                      'numpy<2',
                      'pandas',
                      'periodictable',
                      'roman',
                      'sympy',
                      'tqdm'],
)