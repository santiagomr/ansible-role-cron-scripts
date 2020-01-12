Ansible role cron_scripts
=========

Ansible role to automate the loading and scheduled execution of scripts.


Requirements
------------

Ansible >= 2.7

Role Variables
--------------

```yaml
  - name: example.sh                # Optional
    state: present                  # Optional
    src: example.sh.j2
    dest: /var/scripts/example.sh
    owner: root
    group: root
    mode: 0500
    special_time: daily             # Optional - annually, daily, hourly, monthly, reboot, weekly, yearly
    # minute: "*"                   # Optional
    # hour: "*"                     # Optional
    # day: "*"                      # Optional
    # weekday: "*"                  # Optional
    # month: "*"                    # Optional
    # cron_file: example            # Optional
    # disabled: no                  # Optional
    # reboot: no                    # Optional
```

Dependencies
------------

No dependencies

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: cron_scripts
      vars:
        cron_scripts_list:
          - name: example.sh
            src: example.sh.j2
            dest: /var/scripts/example.sh
            owner: root
            group: root
            mode: 500
            special_time: daily
```

License
-------

GPL-v3

Author Information
------------------

[@santiagomr](https://github.com/santiagomr)
