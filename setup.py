# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pycontrolshed',
    version='0.5.1',
    description="BIGIP pycontrol shell edition",
    author='Tim Freund',
    author_email='tim@freunds.net',
    license='GPLv2+',
    url='http://github.com/timfreund/pycontrolshed',
    install_requires=[
        'pycontrol >= 2.0.0',
        'keyring',
    ],
    packages=['pycontrolshed'],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'coverage',
    ],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    pyctrl-member-disable = pycontrolshed.cli:disable_member
    pyctrl-member-enable = pycontrolshed.cli:enable_member
    pyctrl-member-list = pycontrolshed.cli:members
    pyctrl-member-stats = pycontrolshed.cli:show_member_statistics_cmd
    pyctrl-node-enable = pycontrolshed.cli:enable_node
    pyctrl-node-disable = pycontrolshed.cli:disable_node
    pyctrl-node-status = pycontrolshed.cli:show_node_status
    pyctrl-pools = pycontrolshed.cli:pools
    pyctrl-shell = pycontrolshed.cli:shell
    """,
)
