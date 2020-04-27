#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A class to estimate create a population of random size, and we will
try to estimate the size of the populations.
"""

import random

class PopulationSampling:
    """
    A class to estimate create a population of random size, and we will
    try to estimate the size of the populations.
    """

    def __init__(self, minPop=200, maxPop=500, seed=None):
        """
        input variables:
          minPop: the minimum population to be created (default 100)
          maxPop: the maximum population to be created (default 500)
          seed [int]: a random seed, if you want repeatable results
        """
        random.seed(seed)
        self.populationSize = random.randint(minPop, maxPop)
        self.numMarked = 0


    def mark(self, numMarked):
        """ Mark numMarked from the population
        """
        self.numMarked = numMarked

    def takeSample(self, numSample):
        """ returns numMarked if taking a sample of size numSample
        """
        sample = random.sample(range(self.populationSize), numSample)
        return sum(i < self.numMarked for i in sample)
