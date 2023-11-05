from setuptools import setup, find_packages

v = '0.2.1'

setup(
    name='antlr4-tools',
    version=v,
    py_modules=['antlr4_tool_runner'],
    install_requires=[
        "install-jdk"
    ],
    url='http://www.antlr.org',
    license='BSD',
    author='Terence Parr',
    author_email='parrt@antlr.org',
    entry_points={'console_scripts': [
        'antlr4=antlr4_tool_runner:tool',
        'antlr4-parse=antlr4_tool_runner:interp'
    ]
    },
    description='Tools to run ANTLR4 tool and grammar interpreter/profiler'
)
