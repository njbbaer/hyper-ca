from setuptools import setup, find_packages

setup(name='hyperca',
      version='0.1',
      description='A fast implementation of cellular automata using 2D convolution',
      url='https://github.com/njbbaer/hyper-ca',
      author='Nathaniel Baer',
      author_email='njbbaer@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'matplotlib',
          'pypng',
      ]
)