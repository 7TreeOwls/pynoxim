from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

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

def injection_throughput_plot(path: str, ms: int):
    #Virtual Channels plotting
    data_noxim = np.genfromtxt(csv_name, delimiter=',')
    for y_label in ["global_average_delay", "max_delay"]:
        f=plt.figure()
        ax=f.add_subplot(111)
        ax.plot(data_noxim[:,NAME_TO_IX["injection_load"]],
                data_noxim[:,NAME_TO_IX[y_label]],
                'o', 
                markersize=ms, 
                fillstyle='none')


        x_label = 'Injection Load (flits/cycle/IP)'
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        ax.grid(True)
        f.savefig("injection_load_" + y_label + '.png')
        plt.clf()

if __name__=="__main__":
    ms=10
    csv_name = "20200406_194649_results.csv"
    
    injection_throughput_plot(csv_name, ms)