import sys, getopt
import matplotlib
import math
import json

matplotlib.use('Agg')  # do not change this matplotlib import order
from matplotlib import pyplot as plt  # do not change this matplotlib import order


def chart_rps_response(files_, output="", legend=[''], title='', markers=['o'], lim=500):
    """
        Charts successful RPS as a function of attempted RPS
    """

    scenario_duration = 10.0  # seconds

    for i, file_ in enumerate(files_):
        atts_all = []
        succs_all = []
        with open(file_) as f:
            json_obj = json.loads(f.read())

            atts = []
            succs = []
            text_coords = []
            for j, intermediate in enumerate(json_obj['intermediate']):
                attempted = float(intermediate['scenariosCreated']) / scenario_duration

                if len(atts) > 0 and attempted < atts[-1]: continue

                try:
                    successful = float(intermediate['codes']['200']) / scenario_duration
                except:
                    successful = float(intermediate['scenariosCompleted']) / scenario_duration
                atts.append(attempted)
                succs.append(successful)

                if successful == max(succs):
                    text_coords = [attempted, successful]

            if len(files_) > 1:
                color = plt.cm.Blues(50 + int(200.0 / (len(files_) - 1)) * i)
            else:
                color = plt.cm.Blues(250)

            plt.plot(
                atts,
                succs,
                color=color,
                #                         s=100,
                linewidth=5,
                marker=markers[i % len(markers)]
            )
            plt.text(
                text_coords[0] + 10,
                text_coords[1] + 10,
                "%s (%0d)" % (legend[i], text_coords[1])  # "Api Keys (358)"
            )
            atts_all += atts
            succs_all += succs

    plt.ylim(0, max(atts_all + succs_all) + 25)
    plt.xlim(0, max(atts_all + succs_all) + 25)
    plt.title(title)
    plt.legend(legend, loc='upper left')
    plt.ylabel('Successful requests per second')
    plt.xlabel('Attempted requests per second')
    plt.grid()
    plt.savefig("/data/%s.png" % output)


if __name__ == "__main__":
    argv = sys.argv[1:]

    inputfiles = []
    outputfile = 'out'  # .png

    try:
        opts, args = getopt.getopt(argv, "i:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfiles.append(arg)
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfiles == []:
        inputfiles = ['out.json']

    print 'Input file is ', inputfiles
    print 'Output file is ', outputfile

    chart_rps_response(["/data/%s" % i for i in inputfiles], legend=inputfiles, output=outputfile)
