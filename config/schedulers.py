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

def get_schedulers(build_names):

	schedulers = []

	branches = list(set([item['branch'] for item in build_names]))

	for branch in branches:
		build_names_branch = [item['name'] for item in build_names if item['branch'] == branch]
		schedulers_setup(schedulers, branch, build_names_branch)

	return schedulers

def schedulers_setup(schedulers, branch_name, build_names_branch):

	singled = SingleBranchScheduler(  name='singled-'+branch_name,
	                                change_filter = ChangeFilter(branch=branch_name),
	                                builderNames=build_names_branch,
	                                treeStableTimer=60,)

	forcing = ForceScheduler(       name='forced-'+branch_name,
	                                builderNames=build_names_branch)

	two_hours = Nightly(    name='twohours-'+branch_name,
	                        change_filter = ChangeFilter(branch=branch_name),
	                        branch=branch_name,
	                        builderNames=build_names_branch,
	                        hour=range(0, 24, 2),
	                        )

	daily = Periodic(       name='daily-'+branch_name,
	                        builderNames=build_names_branch,
	                        periodicBuildTimer=24*60*60)

	# comment/uncomment to disable/enable
	schedulers.append(singled)
	schedulers.append(forcing)
	schedulers.append(two_hours)
	schedulers.append(daily)

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

