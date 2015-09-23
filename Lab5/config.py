#!/usr/bin/python

config = {
    'prevalence': 23, # The end-goal or stable prevalence value
    'pop-human': 1700000, # Total human population at start
    'pop-mosq': 100000000, # Total mosquito population at start
    'vector-density': '0.12', # Percentage of infected mosquitos, initial.
    'death-rate': '0.007', # Change of dying after infection
    'death-delay': '',
    'human-max-age': '',
    'mosq-max-age': '',
    'prob-human-mosq': '0.9', # Probability that a mosquite gets infected
    'prob-mosq-human': '0.9', # Probability that a human gets infected
    'init-distr-human': '0.05', # Initial infected humans
    'init-distr-mosq': '0.05' # Initial infected mosquitos
}
