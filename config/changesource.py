# -*- python -*-
# ex: set syntax=python:

####### CHANGESOURCES

# the 'change_source' setting tells the buildmaster how it should find out
# about source code changes.  Here we point to the buildbot clone of pyflakes.

#from buildbot.changes.gitpoller import GitPoller
#c['change_source'] = GitPoller(
#        'git://github.com/buildbot/pyflakes.git',
#        workdir='gitpoller-workdir', branch='master',
#        pollinterval=300)

from buildbot.changes.gitpoller import GitPoller

def get_source(repo_url, branch_name):
	return GitPoller(	repourl=repo_url,
						branch=branch_name,
						pollInterval=300,
			)





