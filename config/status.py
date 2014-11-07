# -*- python -*-
# ex: set syntax=python:

####### STATUS TARGETS

from buildbot.status import html
from buildbot.status.web import auth, authz


def get_status(users):

	status = []

	authz_cfg=authz.Authz(
		# change any of these to True to enable; see the manual for more
		# options
		auth=auth.BasicAuth(users),    
        	gracefulShutdown = False,
        	forceBuild = 'auth', # use this to test your slave once it is set up
        	forceAllBuilds = False,
        	pingBuilder = False,
        	stopBuild = False,
        	stopAllBuilds = False,
        	cancelPendingBuild = False,
		)

	status.append(html.WebStatus(http_port=8010, authz=authz_cfg))

	return status




"""
## from: https://github.com/mlakewood/Buildbot-rollout

from buildbot.status.mail import MailNotifier

    mn = MailNotifier(fromaddr="buildbot@rollout.com", 
                      sendToInterestedUsers=False, mode='all',
                      extraRecipients=['dev@rollout.com'],
                      useTls=True, relayhost="smtp.gmail.com", smtpPort=587, smtpUser="dev@rollout.com", smtpPassword="rollout")

    status.append(mn)
"""

