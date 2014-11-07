# -*- python -*-
# ex: set syntax=python:

####### BUILD STEPS

import time
from buildbot.process.factory import BuildFactory
from buildbot.steps.source.git import Git
from buildbot.steps.shell import ShellCommand


def get_buildsteps(branch_name, working_dir, repo_url):

    factory = BuildFactory()

    # step 1
    factory.addStep(ShellCommand(   command=["pwd"],
                                    name='display_working_folder',
				))
    # step 2
    factory.addStep(Git(    name="git_fetch",
				            workdir=working_dir,
                            #haltOnFailure=True,
                            repourl=repo_url,
                            mode='full',
                            method='fresh',
                            branch=branch_name,
                            submodules=False,
                            description=['git_fetch description'],
                            descriptionDone=['git_fetch done'],
                        ))
    # step 3
    factory.addStep(ShellCommand(	name='py.test_1',
					               description=['py.test_1 description'],
					               descriptionDone=['py.test_1 done'],
					               workdir=working_dir,
					               haltOnFailure=False,
					               env={'PYTHONPATH': working_dir, 'LC_ALL' :'en_GB.UTF-8', 'LANG' : 'en_GB.UTF-8'}, 
					               command=['py.test', '-v', 'tests/'],
                                ))
    # step 4
    factory.addStep(ShellCommand(   name='py.test_2',
                                    description=['py.test_2 description'],
                                    descriptionDone=['py.test_2 done'],
                                    workdir=working_dir,
                                    haltOnFailure=False,
                                    env={'PYTHONPATH': working_dir, 'LC_ALL' :'en_GB.UTF-8', 'LANG' : 'en_GB.UTF-8'}, 
                                    command=['py.test', '--junitxml=../reports/xunit/' + time.strftime('%Y-%m-%d-%H:%M:%S') + '-punit.xml', 'tests/'],
                                ))
    return factory

"""
## from: https://github.com/mlakewood/Buildbot-rollout

    repo = Git(repourl="https://github.com/mlakewood/Buildbot-rollout.git", branch='master')
    virt_env = working_dir + '/virt/lib'
    slave_python = working_dir + '/virt/bin/python'
    env = {"LD_LIBRARY_PATH": virt_env}

    build_steps.addStep(repo)

    # # Pip install the python packages from requirements.txt
    # command = '%s/virt/bin/pip install -r requirements.txt' % working_dir
    # build_steps.addStep(ShellCommand(workdir=working_dir, description="Install packages", command=command.split(" ")))

    # Run the tests through coverage to get test coverage at the same time
    command = "../virt/bin/coverage run --include=src -m unittest discover -vf tests"
    build_steps.addStep(ShellCommand(workdir=working_dir + '/rollout', description="rollout Unit Tests", command=command.split(" ")))

    # Output the coverage report
    command= "virt/bin/coverage report --omit=*tests* -m"
    build_steps.addStep(ShellCommand(workdir=working_dir, description="API Unit Test Coverage Report", command=command.split(" ")))

    # Run pylint. P
    command = "pylint %s/rollout --rcfile=rollout/.pylintrc" % (working_dir)
    build_steps.addStep(PyLint(workdir=working_dir, description="API pylint", command=command.split(" ")))

    command = "./jslint js/*"
    build_steps.addStep(ShellCommand(workdir=working_dir + '/rollout', description="Insight JSLint code", command=command)) 

    return build_steps
"""
