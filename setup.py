import setuptools

LONG_DESCRIPTION = ""

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="parseinteger",
    version="0.1.0",
    author="Josh Hernandez",
    author_email="i.am.mr.josh.hernandez@gmail.com",
    description="Parse integer strings in any base and convert them into any other base.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/josh-hernandez-exe/parseinteger",
    packages=setuptools.find_packages(),
    install_requires=[
        "six",
    ],
)
