# -*- python -*-
# ex: set syntax=python:

####### CHANGESOURCES

from buildbot.changes.gitpoller import GitPoller

def get_source(repo_url, branch_name):
	return GitPoller(	repourl=repo_url,
						branch=branch_name,
						pollInterval=60,
						#workdir=working_dir,
			)





