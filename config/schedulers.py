# -*- python -*-
# ex: set syntax=python:

####### SCHEDULERS

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers.forcesched import ForceScheduler
from buildbot.schedulers.timed import Periodic
from buildbot.schedulers.timed import Nightly
from buildbot.changes.filter import ChangeFilter

def schedulers_single(item):
	""" Check branch for commits"""

	singled = SingleBranchScheduler(  name='singled-'+item['branch'],
	                                change_filter = ChangeFilter(branch=item['branch']),
	                                builderNames=item['name'],
	                                treeStableTimer=30,)
	return (singled)

def schedulers_force(item):
	""" Force build button at web project """

	forcing = ForceScheduler(       name='forced-'+item['branch'],
	                                builderNames=item['name'])
	return (forcing)

def schedulers_nightly(item):
	""" Every day at 0:00 """

	nightly = Nightly(    name='nightly-'+item['branch'],
	                        change_filter = ChangeFilter(branch=item['branch']),
	                        branch=item['branch'],
	                        builderNames=item['name'],
	                    	hour=0, minute=0,
	                        # every 2 hours: hour=range(0, 24, 2),
	                        )
	return (nightly)

def schedulers_periodic(item):
	""" Every 24h after buildbot-master start """

	daily = Periodic(       name='daily-'+item['branch'],
	                        builderNames=item['name'],
	                        periodicBuildTimer=24*60*60)
	return (daily)


def get_schedulers(build_names):
	""" Creates schedulers for each branch and list of builds """

	schedulers = []

	temp = []
	for build_name in build_names:
		temp.extend(build_name['scheduler'])
	sched_names = list(set(temp))

	branches = list(set([item['branch'] for item in build_names]))

	#scheduler_names = []
	for sched_name in sched_names:
		for branch in branches:
			build_names_branch = [item['name'] for item in build_names if (item['branch'] == branch) and (item['scheduler'].count(sched_name) == 1)]
			if not len(build_names_branch) == 0:
				#scheduler_names.append(dict(scheduler=sched_name, name=build_names_branch, branch=branch))
				temp =  dict(name=build_names_branch, branch=branch)
				if sched_name == 'single':
					schedulers.append(schedulers_single(temp))
				elif sched_name == 'periodic':
					schedulers.append(schedulers_periodic(temp))
				elif sched_name == 'force':
					schedulers.append(schedulers_force(temp))
				elif sched_name == 'nightly':
					schedulers.append(schedulers_nightly(temp))
				else:
					pass

	return schedulers


"""
## from: https://github.com/mlakewood/Buildbot-rollout

from buildbot.schedulers.trysched import Try_Jobdir
from buildbot.schedulers.trysched import Try_Userpass

# try example
    try_job = Try_Jobdir(   name="try_job",
                            builderNames=["12.04-" + build + '_try'],
                            jobdir="jobdir")
"""

