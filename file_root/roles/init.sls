/var/cache/salt/minion/roles:
  file.managed:
    - mode: '0644'
    - user: root
    - group: root
    - source: salt://roles/files/roles
    - mkdirs: True
    - template: jinja

#refresh_grains:
  #module.run:
    #- name: saltutil.sync_grains
    #- require:
      #- file: /var/cache/salt/minion/roles
    #- onchanges:
      #- file: /var/cache/salt/minion/roles
