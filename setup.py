from setuptools import setup, find_packages

setup(
    name='aimodelspy',
    version='0.1.0',
    short_description='A Python package for managing multiple AI models',
    long_description='A Python package for managing multiple AI models. This package provides a simple interface for using multiple AI models in a single project. Extension of project: LLM_rs package, part of testing and deployment of decel ai along with rvectors',
    packages=find_packages(),
    install_requires=[
        # 'openai',  
    ],
    entry_points={
        'console_scripts': [
            'your-package-cli=your_package.cli:main',
        ],
    },
)
