from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='packed of file sorting',
      url='https://github.com/Doalina/Python',
      author='Alina Dobryshyna',
      author_email='alinochka1330@gmail.com',
      license='',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.sort:main']}
      )