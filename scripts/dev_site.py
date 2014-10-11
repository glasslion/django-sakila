# -*- coding: utf-8 -*-
import argparse
import os
from os.path import abspath, dirname, exists, join
from shutil import rmtree
from subprocess import call
from tempfile import mkdtemp


REPO_ROOT = dirname(dirname(abspath(__file__)))
TEMPLATE_PATH = join(REPO_ROOT, 'project_template')
DEV_SITE_NAME = 'dev_site'
DEV_SITE_PATH = join(REPO_ROOT, DEV_SITE_NAME)

def create_test_site(path):
    call([
        'django-admin.py',
        'startproject',
        DEV_SITE_NAME,
        path,
        '--template=%s' % TEMPLATE_PATH,
        '--extension=py,rst,html'
    ])

def create():
    if not(exists(DEV_SITE_PATH)):
        os.makedirs(DEV_SITE_PATH)
    elif os.listdir(DEV_SITE_PATH) != []:
        print 'Directory< %s > is not empty' % DEV_SITE_PATH
        return

    create_test_site(DEV_SITE_PATH)


def diff():
    tmp_dir = mkdtemp()
    create_test_site(tmp_dir)

    call([
         'colordiff',
         '-ENBwbur',
         '-x',
         "*.pyc",
         '-x',
         "*.json",
         '-x',
         "*.db",
         DEV_SITE_PATH,
         tmp_dir,
    ])
    rmtree(tmp_dir)


def patch():
    tmp_dir = mkdtemp()

    create_test_site(tmp_dir)
    with open(join(REPO_ROOT,'dev_site.patch'), "w") as patchfile:
        call(
            [
                'diff',
                '-ENBwbur',
                '-x'
                "*.pyc",
                '-x'
                "*.json",
                '-x',
                "settings.py",
                '-x',
                "*.db",
                '.',
                tmp_dir,
            ],
            cwd=DEV_SITE_PATH,
            stdout=patchfile
        )

    rmtree(tmp_dir)
    
    print "Applying the path ..."

    call([
        'patch',
        '-d',
        DEV_SITE_PATH,
        '-i',
        join(REPO_ROOT,'dev_site.patch'),
        '-p0'
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, choices=['create', 'diff', 'patch'], help="Execute an command")
    args = parser.parse_args()
    if args.command=="create":
        create()
    elif args.command=="diff":
        diff()
    elif args.command=="patch":
        patch()


if __name__ == '__main__':
    main()
