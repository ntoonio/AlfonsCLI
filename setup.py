import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AlfonsCLI",
    version="0.0.1",
    author="Anton Lindroth",
    author_email="ntoonio@gmail.com",
    description="A package for simple interaction with Alfons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ntoonio/AlfonsCLI.git",
    packages=setuptools.find_packages(),
	install_requires=[
		"AlfonsIoT"
	],
	entry_points = {
		"console_scripts": [
			"alfons = AlfonsCLI.__main__:main",
		],
	}
)
