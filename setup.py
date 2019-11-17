import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


required=[ 'requests', 'six' ]
if ((sys.version_info[0]) < 3) or ((sys.version_info[0] == 3) and (sys.version_info[1] < 4)):
    required.append('enum34')
localized_message_files = [ 'locale/en/LC_MESSAGES/docloud.mo']
setup(
  name = 'docloud',
  packages = ['docloud'],
  package_dir={'docloud': 'docloud'},
  package_data = { 'docloud' : localized_message_files },
  include_package_data = True,
  version = '1.0.375',
  description = 'The IBM Decision Optimization on Cloud Python client',
  author = 'The IBM Decision Optimization on Cloud team',
  author_email = 'docloud-monitoring-prod@wwpdl.vnet.ibm.com',
  url = 'https://onboarding-oaas.docloud.ibmcloud.com/software/analytics/docloud/',
  keywords = ['docloud', 'rest', 'optimization'],
  license = "Apache License 2.0",
  install_requires = required,
  classifiers = ["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "Intended Audience :: Science/Research",
                 "Operating System :: Unix",
                 "Operating System :: MacOS",
                 "Operating System :: Microsoft",
                 "Operating System :: OS Independent",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Scientific/Engineering :: Mathematics",
                 "Topic :: Software Development :: Libraries",
                 "Topic :: System",
                 "Topic :: Other/Nonlisted Topic",
                 "License :: OSI Approved :: Apache Software License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.4"],
)