# -*- python -*-
# ex: set syntax=python:

####### BUILDERS

from buildbot.config import BuilderConfig
from . import buildsteps

def get_builders(build_names, working_dir, repo_url):

	builders = []

	for build_name in build_names:
		base = BuilderConfig(	name=build_name['name'],
                          slavenames=build_name['slaves'],
                          factory=buildsteps.get_buildsteps(build_name['branch'], working_dir+'-'+build_name['branch'], repo_url))
		builders.append(base)

	return builders

"""
## from: https://github.com/mlakewood/Buildbot-rollout

    builders.append(
        BuilderConfig(name="12.04-" + name,
          slavenames=['slave'], slavebuilddir=build_dir,
          factory=buildsteps.get_buildsteps(build_dir + "/build")))
    
    builders.append(
        BuilderConfig(name="12.04-" + name + '_try',
          slavenames=['slave'], slavebuilddir=build_dir,
          factory=buildsteps.get_buildsteps(build_dir + "/build")))

    builders.append(
        BuilderConfig(name="12.04-" + name + '_sprint',
          slavenames=['slave'], slavebuilddir=build_dir,
          factory=buildsteps.get_buildsteps(build_dir + "/build")))
"""
