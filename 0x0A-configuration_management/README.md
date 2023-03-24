# 0x0A - Configuration management

Configuration Management is the process of systematically handling changes to a system in a way that it maintains integrity over time.

It is useful for:
   * Automation of new server provisioning
   * Quick recovery from critical events
   * Keep consistency among several servers
   * Version control

We have used [puppet](https://puppet.com/docs/puppet/6/puppet_overview.html) for this project and [puppet-lint](http://puppet-lint.com/) for checking syntax.

## Requirements

* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass **puppet-lint** version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension .pp
