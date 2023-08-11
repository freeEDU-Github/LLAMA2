# This file is imported from __init__.py and exec'd from setup.py

MAJOR = 2
MINOR = 2
MICRO = 1
RELEASE = True

__version__ = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

if not RELEASE:
    # if it's a rcx release, it's not proceeded by a period. If it is a
    # devx release, it must start with a period
    __version__ += ''


_kivy_git_hash = '344768bfefd2e8f5302cc9dfb8ca41991ce6f7e7'
_kivy_build_date = '20230617'
