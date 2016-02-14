#!/usr/bin/python

from datetime import date, datetime, timedelta
import commands

SEARCH_TITLE = "your search title"
LOG_LOCATION = "./exe.log" # edit your appropriate log location

today = date.today()
oneWeekAgo = today - timedelta(7)
yesterday = today - timedelta(1)

rename = oneWeekAgo.strftime("%Y.%m.%d")
rename +=  " - "
rename += yesterday.strftime("%Y.%m.%d")

# rename task log title
command = 'geeknote edit --note "%s" --title "%s"' % (SEARCH_TITLE, rename)
output = commands.getoutput(command)

# append to log file
log = today.strftime("%Y.%m.%d")
log += " -- "
log += output
commands.getoutput('echo "%s" >> %s' % (log, LOG_LOCATION))
