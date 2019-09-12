"""
CLI calibration
"""


from easydarts.calibration.calibration import main as calibration


def main(args):
    """
    Runs calibation process and saves output to file
    """

    print("Running command: %s" % args.get('command'))
    print("Number of cameras: %s" % args.get('cameras'))

    calibration()
