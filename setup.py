import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='py3rcon',  

     version='1.0',

     scripts=['pyrcon.py'] ,

     author="Wiktor Metryka",

     author_email="jestemkiosk@gmail.com",

     description="API wrapper for RCON.",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/Jestemkioskiem/py3rcon",

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
