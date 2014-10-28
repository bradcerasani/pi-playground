# Mount Raspberry Pi as Disk in OS X

1. Download and install OSXFUSE and SSHFS [here](http://osxfuse.github.io/)

2. Navigate to _one directory up_ from the directory you'd like to mount the Pi into

```
cd ~/Desktop
```
3. Create a folder to mount the Pi

```
mkdir Pi
```
4. Mount the Pi using SSHFS

```
sshfs pi@192.168.100.116: Pi
```

You can now drag and drop files to/from your Pi as you would any other mounted drive.
