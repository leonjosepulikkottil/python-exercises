#setup file 


from setuptools import setup

setup(
    name="ugates",               
    version='10.0',             
    py_modules=['ugates'],        
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ugates=ugates:gates        
    ''',
)