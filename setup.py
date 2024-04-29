import setuptools
import re

with open('enkanetwork/__init__.py') as f:
	"""
		Get version from utils.py
		Ref: https://github.com/Rapptz/discord.py/blob/52f3a3496bea13fefc08b38f9ed01641e565d0eb/setup.py#L9
	"""
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)

setuptools.setup(
	name="enkanetworkv2.py",
	version=version,
	author="DeviantUa",
	author_email="deviantapi@gmail.com",
	description="Library for fetching JSON data from site https://enka.network/",
	long_description=open("README.md", "r", encoding="utf-8").read(),
	long_description_content_type="text/markdown",
	url="https://github.com/DEViantUA/EnkaNetworkV2.py",
	keywords = ['enkanetwork.py', 'enkanetwork', 'enka.network', 'genshinapi', 'enkanetworkV2', 'enkanetworkV2.py'],
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		"pydantic",
		"aiohttp",
		"cachetools",
	],
	python_requires=">=3.6",
	include_package_data=True
)

