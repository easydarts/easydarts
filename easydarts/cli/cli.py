#!/usr/bin/env python
"""
Command line interface (CLI) for easydarts
"""


import argparse
import pkg_resources
from easydarts.cli.calibration import main as cli_calibration
from easydarts.cli.scorer import main as cli_scorer


try:
	version = pkg_resources.require("easydarts")[0].version
except Exception:
	version = '[error]'


def main():
	#
	# Arguments parser
	#


	parser = argparse.ArgumentParser(
		prog='easydarts',
		description='command line interface for easydarts')


	#
	# Options
	#


	parser.add_argument(
		'-v', '--version', 
		action='version', version='easydarts %s' % version)


	#
	# -> Commands
	#


	commands = parser.add_subparsers(
		help='',
		dest='command', metavar='<commands>')


	#
	# -> Commands -> Calibrate
	#


	commands.add_parser(
		'calibrate', 
		help='starts calibration process')


	#
	# -> Commands -> Scorer
	#


	commands.add_parser(
		'scorer', 
		help='opens window with score program')


	# ------------------------------------
	# Execute
	# ------------------------------------


	commands = {
		"calibrate": cli_calibration,
		"scorer": cli_scorer,
	}

	args = vars(parser.parse_args())
	command = commands.get(args.get('command'), parser.print_help)
	command(args)
