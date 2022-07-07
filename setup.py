from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pure_water_prod_app/__init__.py
from pure_water_prod_app import __version__ as version

setup(
	name="pure_water_prod_app",
	version=version,
	description="This app can be used to manage the production process of pure water from end-to-end. It was designed and developed to work in conjuction with the manufacturing module of erpnxt and built on top of the frappe framework.",
	author="ArdentPros (OptimaERP)",
	author_email="optimaerp@outlook.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
