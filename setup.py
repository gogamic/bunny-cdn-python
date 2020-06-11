import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bunnycdn", 
    version="0.0.3",
    author="Raghav Mri",
    author_email="raghav@gogamic.com",
    description="A python Module for Bunny Cdn API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gogamic/bunny-cdn-python",
    packages=setuptools.find_packages(),
    keywords = ['Bunny-CDN-API', 'CDN', 'Bunny-cdn'],   

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6',
)