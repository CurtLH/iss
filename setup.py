from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='iss',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Where is the International Space Station?",
    author="Curtis Hampton",
    author_email='curtLhampton@gmail.com',
    url='https://github.com/CurtLH/iss',
    packages=['iss'],
    entry_points={
        'console_scripts': [
            'iss=iss.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='iss',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
