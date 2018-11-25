'''
    This project is aimed at trying to use python to run
    other applications via the systems CLI/Terminal

    This is of-course dependant on the other applications containing
    a usable CLI interface.

    The secondary aim is to test it with MakeMKV + Handbrake
    - As well as searching the web for info on inserted optical media!
'''

import subprocess

def someFunction(echo) :
    print(echo)
    subprocess.run(['ls', '-l'])


def testMKV_cli () :
    '''
    makemkvcon --minlength=3600 -r --decrypt --directio=true
    mkv
    disc:0
    all
    /DVDs/MovieName/;
    eject - r
    '''
    subprocess.run(['makemkvcon', '-r', 'info', 'disc:0'])
    #subprocess.run(['makemkvcon', '-r', 'info', 'disc:0', '|','grep cell | awk '{ print $7 }' | tr - d ')","Title' | sort - nr | head - n1 | awk - F: '{print ($1 * 3600) + ($2 * 60) + $3}')

    #long_title =$(makemkvcon - r info disc: 0 | grep cell | awk '{ print $7 }' | tr - d ')","Title' | sort - nr | head - n1 | awk - F: '{print ($1 * 3600) + ($2 * 60) + $3}')

testMKV_cli()