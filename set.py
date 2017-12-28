#setup file 


from setuptools import setup

setup(
    name="ung",               
    version='5.0',             
    py_modules=['ung'],        
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ung=ung:gates        
    ''',
)