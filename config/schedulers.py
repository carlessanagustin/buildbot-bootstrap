# -*- python -*-
# ex: set syntax=python:

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this
# case, just kick off a 'runtests' build

#from buildbot.schedulers.timed import Periodic
#c['schedulers'] = []
#c['schedulers'].append(SingleBranchScheduler(
#                            name="all",
#                            branch='master',
#                            treeStableTimer=None,
#                            builderNames=["runtests"]))

#print c

#periodic = Periodic("every_6_hours", ['slave'], 6*60*60)
#c['schedulers'] = [periodic]

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers.forcesched import ForceScheduler
from buildbot.schedulers.timed import Periodic
from buildbot.schedulers.timed import Nightly
from buildbot.changes.filter import ChangeFilter

def schedulers_single(item):

	singled = SingleBranchScheduler(  name='singled-'+item['name'],
	                                change_filter = ChangeFilter(branch=item['name']),
	                                builderNames=item['branch'],
	                                treeStableTimer=60,)
	return (singled)

def schedulers_force(item):

	forcing = ForceScheduler(       name='forced-'+item['name'],
	                                builderNames=item['branch'])
	return (forcing)

def schedulers_nightly(item):

	two_hours = Nightly(    name='twohours-'+item['name'],
	                        change_filter = ChangeFilter(branch=item['name']),
	                        branch=item['name'],
	                        builderNames=item['branch'],
	                        hour=range(0, 24, 2),
	                        )
	return (two_hours)

def schedulers_periodic(item):

	daily = Periodic(       name='daily-'+item['name'],
	                        builderNames=item['branch'],
	                        periodicBuildTimer=24*60*60)
	return (daily)




def get_schedulers(build_names):

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

