'''
Created on Feb 9, 2015
@author: Helong, Feng
@description: scripts for internal use. Manually import user excel or anything else. 
'''

import sys, os, commands, re

def restart_uwsgi_process_help_func():
    print '''
    help:
        restart_uwsgi_process(filename)
        filename is the uwsgi configure file, such as uwgi.ini
    '''
def restart_uwsgi_process(filename):
    try:
        kill_str = 'killall -9 uwsgi'
        status_1, output_1 = commands.getstatusoutput(kill_str)
        command_str = 'uwsgi --ini' + ' ' + filename
        status, output = commands.getstatusoutput(command_str)
    except Exception as e:
        print e


if __name__ == '__main__':
    if len(sys.argv) < 2:
        restart_uwsgi_process_help_func()
    elif len(sys.argv) == 2:
        restart_uwsgi_process(sys.argv[1])