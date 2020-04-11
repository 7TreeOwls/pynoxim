from matplotlib import pyplot as plt

import numpy as np
from datetime import datetime
from typing import List

ANNOTATION_MARKER=['o','+','s','d','^','*','x','<']
ANNOTATION_LINE=['-','--','.-',':']
ANNOTATION_COLOR=['r','b','g','m']

NAME_TO_IX = {
    "mesh": 0,
    "injection_load": 1,
    "ra_ix": 2,
    "vc_ix": 3,
    "filt_size": 4,
    "packet_size": 5,
    "total_received_packets": 6,
    "total_received_filts": 7,
    "received_filt_ratio": 8,
    "average_wireless_utilization": 9,
    "global_average_delay": 10,
    "max_delay": 11,
    "network_throughput": 12,
    "average_IP_throughput": 13,
    "total_energy": 14,
    "dynamic_energy": 15,
    "static_energy": 16
}


def find_rows_of_results(results,parameter_index, parameter_value):
    return results[np.where(results[:,parameter_index]==parameter_value)[0],:]

def get_nowtime():
    return '{:%Y%m%d_%H%M%S_}'.format(datetime.today())

def plot(path: str, x_labels: List, y_labels: List, ms: int):
    #Virtual Channels plotting
    data_noxim = np.genfromtxt(csv_name, delimiter=',')
    for y_label in y_labels:
        for x_label in x_labels:
            f=plt.figure()
            ax=f.add_subplot(111)
            ax.plot(data_noxim[:,NAME_TO_IX[x_label[0]]],
                    data_noxim[:,NAME_TO_IX[y_label[0]]],
                    'o', 
                    markersize=ms, 
                    fillstyle='none')

            ax.set_ylabel(y_label[0] + y_label[1])
            ax.set_xlabel(x_label[0] + x_label[1])
            ax.set_title(y_label[0] + " vs " + x_label[0]  + " plot")
            ax.grid(True)
            f.savefig(x_label[0] + "_" + y_label[0] + '.png')
            plt.clf()


if __name__=="__main__":
    ms=7
    csv_name = "20200406_194649_results.csv"
    
    # Delay vs Injection load
    plot(csv_name, 
        [["injection_load", " (filt/IP/Cycles)"]],
        [["global_average_delay", " (Cycles)"], ["max_delay", " (Cycles)"]], 
        ms)

    # Global Througput vs Injection Load
    plot(csv_name, 
        [["injection_load", " (filt/IP/Cycles)"]],
        [["network_throughput", " "], ["average_IP_throughput", " "]], 
        ms)