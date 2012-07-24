import sys

from klein import run

from wedis import root


port = int(sys.argv[1]) if sys.argv[1:] else 8080


run("localhost", port)
