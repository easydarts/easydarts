#!/usr/bin/env python
"""
Command line interface (CLI) for easydarts
"""


import argparse
import pkg_resources
from easydarts.cli.calibration import cli_command_calibration
from easydarts.cli.scorer import cli_command_scorer


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


    calibration_parser = commands.add_parser(
		'calibrate', 
		help='starts calibration process')


    #
    # -> Commands -> Scorer
    #


    scorer_parser = commands.add_parser(
		'scorer', 
		help='opens window with score program')


    # ------------------------------------


    args = vars(parser.parse_args())
    command = args.get('command')


    if command == 'calibrate': cli_command_calibration(args)
    if command == 'scorer': cli_command_scorer(args)
    else: parser.print_help()
