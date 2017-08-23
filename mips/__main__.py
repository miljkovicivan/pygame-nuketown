import sys

from mips.game import run


def main():
    try:
        sys.exit(run())
    except KeyboardInterrupt:
        # Ctrl-C exit status
        # http://www.tldp.org/LDP/abs/html/exitcodes.html
        sys.exit(130)
