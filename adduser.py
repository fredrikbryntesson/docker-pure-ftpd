import subprocess
import sys


name = sys.argv[1]
command = ['docker', 'exec', '-it', 'ftpd_server', 'pure-pw', 'useradd', name, '-f', '/etc/pure-ftpd/passwd/pureftpd.passwd', '-m', '-u', 'ftpuser', '-d', '/home/ftpusers/share']
subprocess.call(command)


