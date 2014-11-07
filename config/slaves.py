# -*- python -*-
# ex: set syntax=python:

####### BUILDSLAVES

from buildbot.buildslave import BuildSlave

def get_slaves():
	slaves = []

	slaves.append(BuildSlave('example-slave', 'pass'))
	
	return slaves




"""
def get_slaves(slaves_list):
	slaves = []

	for slave in slaves_list:
		slaves.append(BuildSlave(slave))
	
	return slaves
"""
