# sleeping-beauty

Note: documentation incomplete. work in progress.

## What is Sleeping Beauty project?

The goal of Sleeping Beauty Project is to help parents sleeping longer period of time by calming their dear babies with familiar sounds and musics.
The Sleeping Beauty will start playing familiar sounds when the baby gets agitated.
It is IoT project that includes a piece of sotftware and hardware. 

## Requirements

### Software
Raspbian with Python3 and Flask

### Hardware
- Rasberry Pi
- SD Card 8Gb
- Sound sensor (GPIO 17)
- Edimax wifi (USB)

## Installation & Configuration

- Install git
- Install python3
- Install flask: `pip install flask`
- Create logs folder: `mkdir /home/pi/logs`
- Add executing right to launcher: `chmod 755 /home/pi/sleeping-beauty/launcher.sh`
- Add to crontab: `crontab -l; echo "@reboot sh /home/pi/sleeping-beauty/launcher.sh >/home/pi/logs/cronlog 2>&1" | crontab -`

## TODO
- Start app after booting Pi
- Switch off Pi from flask
- Start/stop monitoring
- Turn volume up / down from flask
- Box device & dress it for babies / toddlers
- Develop an installer that will ease deployment of software on virgin Raspbian OS (python3, flask, ...)
- Ease connection between Sleeping Beauty Box and mobile phones (IoT)
- Show logs on UI

### Installer

- Pyhton3
- Flask
- create folder for log 
- make launched executable
- add run launcher to crontab @reboot
