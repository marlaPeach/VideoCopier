How to Use Video Copier Script:
======

Please be aware that this script is written in Python3 and should run as such. The hashbang should notify the system of this, however for future debugging or enhancement, please make note of this.
This program also has a script to run on Mac as a cron job, or can be used on Windows as a scheduled task. It does not specify for security, and will need to be enhanced to do so if this becomes a necessity.

This program is run from the command line if not run as a cron job or scheduled task. The only input necessary is to call it as your normally would a Python script from the respective OS. (Python for Windows or Python3 for Mac, then the file name while inside the correct directory.)

Additional documentation on creating cron jobs and scheduled tasks will be specified in other documentation files.

Please note that the Mac version only has the copy2 version of this script, as the robocopy command is specific to the Windows environment.

__Within the windows version:__
Provided are two scripts. One running with Python's copy2 command which saves *most* metadata. Specific data on which metadata can be lost was not available at the time of this scripts writing. Therefore the second script which runs Window's robocopy command from the script was also built in order to be sure that all metadata was copied.

As it is writen currently, within the copy2 script, the paths for source, destination, and log will need to be input into the code as variables before the cron job or scheduled task is put in place.
In the robocopy script, the log and source will need to be input into the code as variables, however the destination will need to be hard coded into the robocopy command within the script.

This script also utilizes the send2trash library. In order to install this library, the command: <pip install send2trash> will need to be performed
when the script is setup to run. This will be sure that all deleted files are sent to the Trash or Recycle Bin depending on the OS it is used on. __The library will determine the OS, there is no need to apply any further settings beyond the initial install command.__


Scheduled Task Documentation:
------
__Setting up a scheduled task in Windows:__

Windows offers two options for setting up a scheduled task. This can be done either from the GUI provided by pushing the "Windows Key"+R then typing taskschd.msc. This will allow you to open the Task Scheduler and click Create Task.

Creating a scheduled task can also be done from the command line. Below is a link to a reference for creating a scheduled task in both ways: https://www.technipages.com/scheduled-task-windows


Cron Job Documentation:
------
__Cron Job Format:__

Cron jobs are the scheduled task for the Mac environment. They are setup as follows:

Using your terminal and the command: crontab -e
You can also set the editor to use by inputting EDITOR=nano crontab -e
* *Note: nano can be substituted for vim or an editor of your choice.*

Editing the crontab will allow you to create a new cron job. The format for a cron job is below with each asterisk representing a unit of time. The first is for minutes, the second hours, the third day of the month, fourth month, and fifth is the day of the week.
* __For a further breakdown of this information, please visit the following link:__
* https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html

Example setup of cron job:
    * * * * * /usr/local/bin/python3 /Users/tiffanyschmidt/Documents/Video_Copier/VideoCopier.py

*Please note that asterisks can be left in all five places, however this will setup the utility to run every minute of every day of every month etc..*
