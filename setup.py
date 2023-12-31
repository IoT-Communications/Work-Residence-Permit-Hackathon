from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in work_residence_permit_management/__init__.py
from work_residence_permit_management import __version__ as version

setup(
	name="work_residence_permit_management",
	version=version,
	description="Work and Residence Permit Management System",
	author="IoT Communications (Pty) Ltd",
	author_email="info@iotcomms.co.bw",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
