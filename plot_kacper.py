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
    "static_energy": 16,
    "buffer_size": 17
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

def plot_energy(path: str, ms: int):
    #Virtual Channels plotting
    data_noxim = np.genfromtxt(csv_name, delimiter=',')
    f=plt.figure()
    ax=f.add_subplot(111)
    ax.plot(data_noxim[:,NAME_TO_IX["injection_load"]],
            data_noxim[:,NAME_TO_IX["total_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color='green',
            label='total energy')
    ax.plot(data_noxim[:,NAME_TO_IX["injection_load"]],
            data_noxim[:,NAME_TO_IX["static_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color='blue',
            label='static energy')    
    ax.plot(data_noxim[:,NAME_TO_IX["injection_load"]],
            data_noxim[:,NAME_TO_IX["dynamic_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color='red',
            label='dynamic energy')  
    ax.legend()
    ax.set_ylabel("Energy (J)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Energy plot")
    ax.grid(True)
    f.savefig("injection_load_energy.png")
    plt.clf()

def plot_hotspots(path: List, ms: int):
    #Virtual Channels plotting
    data_noxim_05 = np.genfromtxt(path[0], delimiter=',')
    data_noxim_15 = np.genfromtxt(path[1], delimiter=',')
    data_noxim_25 = np.genfromtxt(path[2], delimiter=',')

    f=plt.figure()
    ax=f.add_subplot(111)
    ax.plot(data_noxim_05[:,NAME_TO_IX["injection_load"]],
            data_noxim_05[:,NAME_TO_IX["total_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color='green',
            label="Hotspot 5% traffic")
    ax.plot(data_noxim_15[:,NAME_TO_IX["injection_load"]],
            data_noxim_15[:,NAME_TO_IX["total_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color="blue",
            label="Hotspot 7.5% traffic")
    ax.plot(data_noxim_25[:,NAME_TO_IX["injection_load"]],
            data_noxim_25[:,NAME_TO_IX["total_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color="red",
            label="Hotspot 10% traffic")
    ax.legend()
    ax.set_ylabel("Total Energy (J)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Total Energy (J)")
    ax.grid(True)
    f.savefig("injection_load_tot_energt_hotspots.png")
    plt.clf()

    f=plt.figure()
    ax=f.add_subplot(111)
    ax.plot(data_noxim_05[:,NAME_TO_IX["injection_load"]],
            data_noxim_05[:,NAME_TO_IX["network_throughput"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color='green',
            label="Hotspot 5% traffic")
    ax.plot(data_noxim_15[:,NAME_TO_IX["injection_load"]],
            data_noxim_15[:,NAME_TO_IX["network_throughput"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color="blue",
            label="Hotspot 7.5% traffic")
    ax.plot(data_noxim_25[:,NAME_TO_IX["injection_load"]],
            data_noxim_25[:,NAME_TO_IX["network_throughput"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color="red",
            label="Hotspot 10% traffic")
    ax.legend()
    ax.set_ylabel("Network throughput (flits/Cycle)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Network throughput")
    ax.grid(True)
    f.savefig("injection_load_throughput_hotspots.png")
    plt.clf()


    f=plt.figure()
    ax=f.add_subplot(111)
    ax.plot(data_noxim_05[:,NAME_TO_IX["injection_load"]],
            data_noxim_05[:,NAME_TO_IX["global_average_delay"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color='green',
            label="Hotspot 5% traffic")
    ax.plot(data_noxim_15[:,NAME_TO_IX["injection_load"]],
            data_noxim_15[:,NAME_TO_IX["global_average_delay"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color="blue",
            label="Hotspot 7.5% traffic")
    ax.plot(data_noxim_25[:,NAME_TO_IX["injection_load"]],
            data_noxim_25[:,NAME_TO_IX["global_average_delay"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color="red",
            label="Hotspot 10% traffic")
    ax.legend()
    ax.set_ylabel("Average Delay (Cycles)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Average Delay")
    ax.grid(True)
    f.savefig("injection_load_delay_hotspots.png")
    plt.clf()

def plot_routing_algs(csv_name, ms):
    RA_list = [
        "XY",
        "WEST_FIRST",
        "NORTH_LAST",
        "NEGATIVE_FIRST",
        "ODD_EVEN",
        "DYAD",
    ]
    color_list = [
        "blue",
        "green",
        "red",
        "yellow",
        "brown",
        "purple"
    ]
    data = np.genfromtxt(csv_name, delimiter=',')
    f=plt.figure()
    ax=f.add_subplot(111)
    for i, RA in enumerate(RA_list):
        # i is equivalent to the RA index
        b = find_rows_of_results(data, NAME_TO_IX["ra_ix"], i)
        ax.plot(
            b[:,NAME_TO_IX["injection_load"]],
            b[:,NAME_TO_IX["global_average_delay"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color=color_list[i],
            label=RA
            )
    ax.legend()
    ax.set_ylabel("Average Delay (Cycles)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Average Delay for different routing algorithms")
    ax.grid(True)
    f.savefig("injection_load_delay_hotspots_ras.png")
    plt.clf()

    f=plt.figure()
    ax=f.add_subplot(111)
    for i, RA in enumerate(RA_list):
        # i is equivalent to the RA index
        b = find_rows_of_results(data, NAME_TO_IX["ra_ix"], i)
        ax.plot(
            b[:,NAME_TO_IX["injection_load"]],
            b[:,NAME_TO_IX["network_throughput"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color=color_list[i],
            label=RA
            )
    ax.legend()
    ax.set_ylabel("Network throughput (flits/Cycle)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Network throughput with different routing algorithms")  
    ax.grid(True)
    f.savefig("injection_load_throughput_hotspots_ras.png")
    plt.clf()

    f=plt.figure()
    ax=f.add_subplot(111)
    for i, RA in enumerate(RA_list):
        # i is equivalent to the RA index
        b = find_rows_of_results(data, NAME_TO_IX["ra_ix"], i)
        ax.plot(
            b[:,NAME_TO_IX["injection_load"]],
            b[:,NAME_TO_IX["total_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color=color_list[i],
            label=RA
            )
    ax.legend()
    ax.set_ylabel("Total Energy (J)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Total Energy with different routing algorithms")  
    ax.grid(True)
    f.savefig("injection_load_totenergy_hotspots_ras.png")
    plt.clf()

def plot_buffer_sizes(csv_name, ms):
    buffer_sizes=[2, 4, 8, 16, 32, 64]
    color_list = [
        "blue",
        "green",
        "red",
        "yellow",
        "brown",
        "purple"
    ]
    data = np.genfromtxt(csv_name, delimiter=',')
    f=plt.figure()
    ax=f.add_subplot(111)
    for i, RA in enumerate(RA_list):
        # i is equivalent to the RA index
        b = find_rows_of_results(data, , i)
        ax.plot(
            b[:,NAME_TO_IX["injection_load"]],
            b[:,NAME_TO_IX["global_average_delay"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color=color_list[i],
            label=RA
            )
    ax.legend()
    ax.set_ylabel("Average Delay (Cycles)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Average Delay for different routing algorithms")
    ax.grid(True)
    f.savefig("injection_load_delay_hotspots_ras.png")
    plt.clf()

    f=plt.figure()
    ax=f.add_subplot(111)
    for i, RA in enumerate(RA_list):
        # i is equivalent to the RA index
        b = find_rows_of_results(data, NAME_TO_IX["ra_ix"], i)
        ax.plot(
            b[:,NAME_TO_IX["injection_load"]],
            b[:,NAME_TO_IX["network_throughput"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color=color_list[i],
            label=RA
            )
    ax.legend()
    ax.set_ylabel("Network throughput (flits/Cycle)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Network throughput with different routing algorithms")  
    ax.grid(True)
    f.savefig("injection_load_throughput_hotspots_ras.png")
    plt.clf()

    f=plt.figure()
    ax=f.add_subplot(111)
    for i, RA in enumerate(RA_list):
        # i is equivalent to the RA index
        b = find_rows_of_results(data, NAME_TO_IX["ra_ix"], i)
        ax.plot(
            b[:,NAME_TO_IX["injection_load"]],
            b[:,NAME_TO_IX["total_energy"]],
            'o', 
            markersize=ms, 
            fillstyle='none',
            color=color_list[i],
            label=RA
            )
    ax.legend()
    ax.set_ylabel("Total Energy (J)")
    ax.set_xlabel("Injection Load (filt/IP/Cycles)")
    ax.set_title("Injection load vs Total Energy with different routing algorithms")  
    ax.grid(True)
    f.savefig("injection_load_totenergy_hotspots_ras.png")
    plt.clf()

if __name__=="__main__":
    ms=2
    csv_name = "ra_sweep.csv"
    plot_routing_algs(csv_name, ms)
    plot_buffer_sizes(csv_name_buff, ms)
    buffer_sizes=[2, 4, 8, 16, 32, 64]
    # For Part B

    """ 
    # For Part A
    csv_name = "injection_load_sweep.csv"
    csv_name_hotspots = ["hotspot_0.05.csv",  "hotspot_0.075.csv",  "hotspot_0.1.csv"]
    # Delay vs Injection load
    plot(csv_name, 
        [["injection_load", " (filt/IP/Cycles)"]],
        [["global_average_delay", " (Cycles)"], ["max_delay", " (Cycles)"]], 
        ms)

    # Global Througput vs Injection Load
    plot(csv_name, 
        [["injection_load", " (filt/IP/Cycles)"]],
        [["network_throughput", " (flits/cycle)"], ["average_IP_throughput", " (flits/cycle/IP)"]], 
        ms)

    plot_energy(csv_name, ms)

    plot_hotspots(csv_name_hotspots, ms)
    """