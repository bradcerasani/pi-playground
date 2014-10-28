# Mount Raspberry Pi as Disk in OS X

This will allow you to mount your Pi as you would any other disk in OS X.

### Instructions

Install [OSXFUSE](http://osxfuse.github.io/) and [SSHFS](http://osxfuse.github.io/)

Navigate _one directory up_ from the directory you'd like to mount the Pi into

`cd ~/Documents/Development`

Create a folder to mount the Pi in

`mkdir Pi`

Mount the Pi using SSHFS

`sshfs pi@192.168.100.116: Pi`
