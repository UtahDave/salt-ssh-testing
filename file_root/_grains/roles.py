#!/usr/bin/env python
import os
import re
import subprocess

def get_roles():
  grains = dict()
  # Initialize empty list
  grains['roles'] = list()
  m_id = None
  r_id = None

  # Get minion id
  if os.path.isfile("/etc/salt/minion"):
    fd_minion = open("/etc/salt/minion", "r")
    for line in fd_minion:
      # Ignore comment lines
      if re.match("^#", line):
        continue
      else:
        line = line.strip().split(":")
        if line[0] == 'id':
          m_id = line[1].strip()
          break
    fd_minion.close()

  if m_id == None:
    if os.path.isfile("/etc/salt/minion_id"):
      fd_minion = open("/etc/salt/minion_id", "r")
      # Minion ID is FQDN, only need hostname
      for line in fd_minion:
        line = line.strip().split(".")
        m_id = line[0]
      fd_minion.close()

    else:
      # Use hostname for minion id
      m_id = subprocess.Popen(["hostname", "-s"], stdout=subprocess.PIPE)
      m_id = m_id.communicate()[0].strip()

  if m_id != None:
    # Get minion roles
    if os.path.isfile("/var/cache/salt/minion/roles"):
      fd_roles = open("/var/cache/salt/minion/roles", "r")
      match = 0
      for line in fd_roles:
        if match == 1:
          break
        # Ignore comment lines
        elif re.match("^#", line):
          continue
        else:
          (r_id, roles) = line.strip().split(":")
          roles = roles.split(",")
          for role in roles:
            role = role.strip()
            # Role ID must match Minion ID for roles
            if r_id == m_id:
              grains['roles'].append(role)
              match = 1
      fd_roles.close()

  return grains
