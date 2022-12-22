from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dt_mcs_custom_v13/__init__.py
from dt_mcs_custom_v13 import __version__ as version

setup(
	name="dt_mcs_custom_v13",
	version=version,
	description="DT-MCS-Custom-v13",
	author="Dipane Technologies Pvt Ltd",
	author_email="dev1@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
