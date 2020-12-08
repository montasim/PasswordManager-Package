from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: Closed/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PasswordManager',
  version='0.0.1',
  description='A simple password generator made with python.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/montasim/PasswordManager-Package',  
  author='Montasim -Al- Mamun',
  author_email='montasimmamun@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='password manager', 
  packages=find_packages(),
  install_requires=[''] 
)
