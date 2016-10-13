# salt-ssh-testing
pillar and file_roots for testing salt-ssh

example master and roster configs included.

master => /etc/salt/master
roster => /etc/salt/roster

After setting up a master using the master and roster file above try running
the following commands:

salt-run fileserver.update
salt-ssh '*' saltutil.refresh_pillar
salt-ssh '*' state.sls roles
salt-ssh '*' state.sls resolv

