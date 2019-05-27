import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="muDIC",
    version="0.1.0",
    author="PolymerGuy",
    author_email="sindre.n.olufsen@ntnu.no",
    description="A digital image correlation toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PolymerGuy/muDIC",
    packages=setuptools.find_packages(),
    install_requires=[
        'numba',
        'scipy == 1.2.1',
        'matplotlib',
        'numpy',
        'Pillow',
        'dill',
        'nose',
        'scikit-image',
        'muDIC'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
