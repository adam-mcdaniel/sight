# Run the following command to install package:
# pip install --user .
from setuptools import setup

def readme():
    try:
      with open('README.md') as f:
          return f.read()
    except:
      return "# sight"

setup(name='sight',
    version='0.1.2',

    long_description=readme(),
    long_description_content_type='text/markdown',

    description='A library for Vision Processing',
    url='http://github.com/adam-mcdaniel/small-vision',
    author='Adam McDaniel',
    author_email='adam.mcdaniel17@gmail.com',
    license='Apache-2.0',
    install_requires=[
        'opencv-python'
    ],
    packages=['sight'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    ],
)