import matplotlib.pyplot as plt
import numpy as np
from . import line_coding_schemes as lcs

def plot_UNRZ(bits):
    fig, axs = plt.subplots(figsize=(7, 4))
    x, y = lcs.uni_NRZ(bits)
    axs.plot(x, y, linewidth=3)
    axs.set(xlabel='Time', ylabel='Amplitude', title='Unipolar: NRZ')
    axs.set_xticks([x for x in range(len(bits)+1)])
    axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs.grid()
    plt.show()

def plot_PNRZ(bits,code):
    fig, axs = plt.subplots(1, figsize=(7, 4), sharex=True)
    x, y = lcs.pol_NRZL(bits)
    if code == "nrzl":
        axs.plot(x, y, linewidth=3)
        axs.set_title('Polar: NRZ-L')
        axs.set(ylabel='Amplitude', title='Polar: NRZ-L')
        axs.set_xticks([x for x in range(len(bits)+1)])
        axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
        axs.grid()
        
    else:
        x, y, ix0, i0, ix1, i1 = lcs.pol_NRZI(bits, 1)
        axs.plot(x, y, linewidth=3)
        p1, = axs.plot(ix0, i0, 'o', markeredgecolor="black", markerfacecolor="white", markersize=7, label="Next bit is 0: No Inversion")
        p2, = axs.plot(ix1, i1, 'ok', markersize=7, label="Next bit is 1: Inversion")
        axs.legend(loc='lower right', prop={'size': 5.5})
        axs.set_title('Polar: NRZ-I')
        axs.set(xlabel='Time', ylabel='Amplitude', title='Polar: NRZ-I')
        axs.set_xticks([x for x in range(len(bits)+1)])
        axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
        axs.grid()
    plt.show()

def plot_PRZ(bits):
    fig, axs = plt.subplots(figsize=(7, 4))
    x, y = lcs.pol_RZ(bits)
    axs.plot(x, y, linewidth=3)
    axs.set_title('Polar RZ')
    axs.set(xlabel='Time', ylabel='Amplitude', title='Polar RZ')
    axs.set_xticks([x for x in range(len(bits)+1)])
    axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
    axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
    axs.grid()
    plt.show()

def plot_Biphase(bits,code):
    fig, axs = plt.subplots(1, figsize=(7, 4), sharex=True)
    x, y = lcs.MANCHESTER(bits)
    if code != "diff":
        axs.plot(x, y, linewidth=3)
        axs.set(ylabel='Amplitude', title='Biphase: Manchester')
        axs.set_xticks([x for x in range(len(bits)+1)])
        axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
        axs.grid()
    else:
        x, y, ix0, i0, ix1, i1 = lcs.diff_MANCHESTER(bits, 1)
        axs.plot(x, y, linewidth=3)
        axs.plot(ix0, i0, 'o', markeredgecolor="black", markerfacecolor="white", markersize=7, label="No Inversion: Next bit is 1")
        axs.plot(ix1, i1, 'ok', markersize=7, label="Inversion: Next bit is 0s")
        axs.legend(loc='lower right', prop={'size': 5.5})
        axs.set(xlabel='Time', ylabel='Amplitude', title='Differential Manchester')
        axs.set_xticks([x for x in range(len(bits)+1)])
        axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
        axs.grid()
    plt.show()

def plot_Bipolar(bits,code):
    fig, axs = plt.subplots(1, figsize=(7, 4), sharex=True)
    x, y = lcs.AMI(bits)
    if code == "ami":
        axs.plot(x, y, linewidth=3)
        axs.set(ylabel='Amplitude', title='Bipolar: AMI(Alternate Mark Inversion)')
        axs.set_xticks([x for x in range(len(bits)+1)])
        axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
        axs.grid()
    else:
        x, y = lcs.Pseudoternary(bits)
        axs.plot(x, y, linewidth=3)
        axs.set(xlabel='Time', ylabel='Amplitude', title='Bipolar: Pseudoternary')
        axs.set_xticks([x for x in range(len(bits)+1)])
        axs.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
        axs.set_yticklabels(['', '-1', '', '0', '', '1', ''])
        axs.grid()
    plt.show()
