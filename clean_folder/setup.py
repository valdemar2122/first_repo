from setuptools import setup

setup(
    name='clean_folder',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'cleanfolder = clean_folder.clean_folder.sort_soft:main'
        ]
    }
)