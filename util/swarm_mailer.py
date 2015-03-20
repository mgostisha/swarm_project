import sys
import smtplib

# Only an email address and a job id should be passes to this script
# More or less and the script will write to the log and exit without
# doing anything.
if len(sys.argv) != 3:
	print 'Incorrect number of arguments.'
	# TODO: Write to logger
	# TODO: Exit script

# Inputs to script
TO_EMAIL = sys.argv[1]
JOB_ID = sys.argv[2]

# Server Constants
FILE_SERVER = 'astro.wisc.edu'
FILE_USER = 'gostisha'
FILE_DIR = '/d/www/{0}/resource/download/swarm'.format(FILE_USER)

WEB_PAGE = 'http://www.astro.wisc.edu/~gostisha/swarm.html'
WEB_DIR = 'http://www.astro.wisc.edu/`Gostisha/resource/download/swarm' 

FILENAME = 'swarm_{0}.zip'.format(str(JOB_ID))

# Email Fields
FROM_EMAIL = 'gostisha@astro.wisc.edu'
SUBJECT = 'Swarm Job #{0} has completed'.format(str(JOB_ID))
BODY = ''' Your swarm job (ID {0}) has completed. The data is available for download at:\n
{1}/{2}\n\nYou can reply to this email with any problems you encounter.'''.format(
	str(JOB_ID), WEB_DIR, FILENAME)

try:
	s = smtplib.SMTP(FILE_SERVER, 25)
	s.sendmail(FROM_EMAIL, [TO_EMAIL], BODY)
	print 'Sent Email!'
except smtplib.SMTPException:
	print 'Couldn\'t send email'
