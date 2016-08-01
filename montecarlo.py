# coding=utf-8
#####################################################
# Tyler Hedegard
# 8/1/16
# Thinkful Data Science
# Monte Carlo
#####################################################
"""
Command line>> python montecarlo.py
"""

import numpy as np
import matplotlib.pyplot as plt


class Trial(object):
    last_result = None

    def make_trial(self):
        self.last_result = result = np.random.normal()
        return result


def create_trial(number):
    return [Trial() for _ in xrange(number)]


def main():
    results = []
    max = []
    min = []
    for i in xrange(100):
        trial = create_trial(1000)
        trial_results = []
        for j in trial:
            j.make_trial()
            trial_results.append(j.last_result)
            results.append(j.last_result)
        max.append(np.array(trial_results).max())
        min.append(np.array(trial_results).min())
    results = np.array(results)
    ax1 = plt.subplot(311)
    plt.subplots_adjust(hspace=0.5)
    plt.hist(results)
    plt.title('Results')
    plt.subplot(312, sharex=ax1)
    plt.hist(min)
    plt.title('Trial Minimums')
    plt.subplot(313, sharex=ax1)
    plt.hist(max)
    plt.title('Trial Maximums')
    plt.show()

if __name__ == '__main__':
    main()

