JenkinsJobs
===========

Python scripts and config.xml files for various jobs on the Bradner Lab Jenkins server.

Jenkins (http://jenkins-ci.org/) is a continous integration server.  Jenkins is flexible and can also serve as a cron 
replacement and can run arbitrary jobs.  Jenkins can provide a simple GUI wrapper around command line programs, and 
also provides easy ways to string multiple jobs together, email results or failure messages, archive results, and 
do logging.

Most of these Jenkins jobs will be centered around automating (as much as possible) the process from genome sequence 
data to useful plots to help Cancer researchers.

These jobs require at least the following plugins:
* http://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin
* http://wiki.jenkins-ci.org/display/JENKINS/Email-ext+plugin
* http://wiki.jenkins-ci.org/display/JENKINS/Extended+Choice+Parameter+plugin
