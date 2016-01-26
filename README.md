# dupweb: a simple web interface for duplicity backups

## Overview

## Installation

### Install necessary OS packages:
  * Fedora:
    * `dnf install duplicity`
  * FreeBSD:
    * `pkg install duplicity`
  
### Python setup
  * `git clone https://github.com/sinner-/dupweb`
  * `virtualenv -p /usr/bin/python2.7 dupweb`
  * `cd dupweb`
  * `pip install -r requirements.txt`

### Standalone daemon (development only)
  * (from inside dupweb directory)
  * `source bin/activate`
  * `bin/python dupweb.py`
