buildbot-bootstrap
==================

This is a simple way of bootstraping [Buildbot](http://buildbot.net/) first configuration.

The structure of these configuration files allows to:

* Pull from 1 Git repo (master.cfg > repo_url).
* Add branches to our builds (master.cfg > build_names.append...)
* Add selected schedulers to our builds (master.cfg > build_names.append...)
* Use the same buildsteps for all branches (buildsteps.py > factory...).
* Connected to 1 slave only (slaves.py > slaves.append...)


Check out my YouTube [channel](http://www.youtube.com/playlist?list=PLF3EgRIVV_yRY_JCjSRfNFKAzt65Mng3P) for updated videos.

Parts of this code are forked from [Mark Lakewood github](https://github.com/mlakewood/Buildbot-rollout). I recommend you to check out his video:

* [Buildbots Rollout! Video](https://www.youtube.com/watch?v=7HLtPKU0-vE)

Please fork, use and comment this repo ;)