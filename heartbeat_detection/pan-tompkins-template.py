import numpy as np
from scipy.signal import find_peaks
from ekg_testbench import EKGTestBench


def main(filepath):
    if filepath == '':
        return list()

    # import the CSV file using  numpy
    path = filepath

    # load data in matrix from CSV file; skip first two rows

    data = np.loadtxt(path,skiprows=2,delimiter=',')


    # save each vector as own variable

    time = data[:,0]
    V5 = data[:,1]
    V2 = data[:,2]

    # find the sample frequency of the signal
    sample_frequency = 1/(time[1])


    # choose one column to process
    signal = V5

    # pass data through differentiator
    signal = np.diff(signal)

    # pass data through square function
    signal = np.square(signal)

    # pass through moving average window
    signal = np.convolve(signal,[1,1,1])


    # use find_peaks to identify peaks within averaged/filtered data
    # save the peaks result and return as part of testbench result
    peaks,_ = find_peaks(signal,height=.031,distance=110)




    return signal,peaks


# when running this file directly, this will execute first
#written by Jason Forsyth to graph results and find an F1 score which measures accuracy in determining heartbeats
if __name__ == "__main__":

    # place here so doesn't cause import error
    import matplotlib.pyplot as plt

    # database name
    database_name = 'mitdb_103'

    # set to true if you wish to generate a debug file
    file_debug = True

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # set to true if you wish to show a plot of each detection process
    show_plot = True

    # path to ekg folder
    path_to_folder = "./ekg/"

    # select a signal file to run
    signal_filepath = path_to_folder + database_name + ".csv"

    # call main() and run against the file. Should return the filtered
    # signal and identified peaks
    (signal, peaks) = main(signal_filepath)

    # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
    # not matched to any annotation; and remaining is annotations that were not matched.
    annotation_path = path_to_folder + database_name + "_annotations.txt"
    tb = EKGTestBench(annotation_path)
    peaks_list = peaks.tolist()
    (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

    # if was matched, then is true positive
    true_positive = len(matched)

    # if response was unmatched, then is false positive
    false_positive = len(unmatched)

    # whatever remains in annotations is a missed detection
    false_negative = len(remaining)

    # calculate f1 score
    f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

    # if we wish to show the resulting plot
    if show_plot:
        # make a nice plot of results
        plt.title('Signal for ' + database_name + " with detections")

        plt.plot(signal, label="Filtered Signal")
        plt.plot(peaks, signal[peaks], 'p', label='Detected Peaks')

        true_annotations = np.asarray(tb.annotation_indices)
        plt.plot(true_annotations, signal[true_annotations], 'o', label='True Annotations')

        plt.legend()

        # uncomment line to show the plot
        plt.show()

    # if we wish to save all the stats to a file
    if file_debug:
        # print out more complex stats to the debug file
        debug_file_path = database_name + "_debug_stats.txt"
        debug_file = open(debug_file_path, 'w')

        # print out indices of all false positives
        debug_file.writelines("-----False Positives Indices-----\n")
        for fp in unmatched:
            debug_file.writelines(str(fp) + "\n")

        # print out indices of all false negatives
        debug_file.writelines("-----False Negatives Indices-----\n")
        for fn in remaining:
            debug_file.writelines(str(fn.sample) + "\n")

        # close file that we are writing
        debug_file.close()

    if print_debug:
        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        print(database_name, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
        print("-------------------------------------------------")

    print("Done!")
