import setuptools

setuptools.setup(
    name="circleseqPCR",
    version="0.1.0",
    url="https://github.com/DamLabResources/playAround",

    author="Cheng-Han Chung",
    author_email="cc3423@drexel.edu",

    description="Circle-Seq for PCR",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)