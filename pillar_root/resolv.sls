resolv:
  search:
    - 'example.com'
    - 'ent.example.com'
  {% if 'dmz' in grains.('roles', '') %}
  servers:
    - '192.168.1.103'
  {% else %}
  servers:
    - '192.168.5.33'
    - '192.168.5.34'
  {% endif %}
