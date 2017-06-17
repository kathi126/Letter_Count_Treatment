from __future__ import division

import random

import numpy as np

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer


author = 'AS,GS,HV,KS'

doc = """
Meritocracy Experiment - Treatment Group
"""


class Constants(BaseConstants):
    name_in_url = 'project_2_treat'
    players_per_group = 5
    num_rounds = 1

    t = 20
    tokensper_string = c(1)
    eurosper_token = 0.10
    secondsper_token = 10

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    groupoutput3 = models.FloatField(default=1)
    groupoutput4 = models.FloatField(default=1)
    groupoutput5 = models.FloatField(default=1)
    groupoutput6 = models.FloatField(default=1)
    groupoutput7 = models.FloatField(default=1)
    groupoutput8 = models.FloatField(default=1)

    def set_output3(self):
        self.groupoutput3 = sum([p.output3 for p in self.get_players()])
        if self.groupoutput3 == 0:
            for p in self.get_players():
                p.share3 = 0.2
        else:
            for p in self.get_players():
                p.share3 = p.output3 / self.groupoutput3

    def set_output4(self):
        self.groupoutput4 = sum([p.output4 for p in self.get_players()])
        if self.groupoutput4 == 0:
            for p in self.get_players():
                p.share4 = 0.2
        else:
            for p in self.get_players():
                p.share4 = p.output4 / self.groupoutput4

    def set_output5(self):
        self.groupoutput5 = sum([p.output5 for p in self.get_players()])
        if self.groupoutput5 == 0:
            for p in self.get_players():
                p.share5 = 0.2
        else:
            for p in self.get_players():
                p.share5 = p.output5 / self.groupoutput5

    def set_output6(self):
        self.groupoutput6 = sum([p.output for p in self.get_players()])
        if self.groupoutput6 == 0:
            for p in self.get_players():
                p.share6 = 0.2
        else:
            for p in self.get_players():
                p.share6 = p.output6 / self.groupoutput6

    def set_output7(self):
        self.groupoutput7 = sum([p.output7 for p in self.get_players()])
        if self.groupoutput7 == 0:
            for p in self.get_players():
                p.share7 = 0.2
        else:
            for p in self.get_players():
                p.share7 = p.output7 / self.groupoutput7

    def set_output8(self):
        self.groupoutput8 = sum([p.output8 for p in self.get_players()])
        if self.groupoutput8 == 0:
            for p in self.get_players():
                p.share8 = 0.2
        else:
            for p in self.get_players():
                p.share8 = p.output8 / self.groupoutput8

    def set_switch3(self):
        for p in self.get_players():
            p.switchtime3 = p.switch3 * (p.additionaltime3 + p.t301 + p.t302 + p.t303 + p.t304 + p.t305 + p.t306 + p.t307 + p.t308 + p.t309 + p.t310 + p.t311 + p.t312 + p.t313 + p.t314 + p.t315 + p.t316 + p.t317 + p.t318 + p.t319 + p.t320 + p.t321 + p.t322 + p.t323 + p.t324 + p.t325 + p.t326 + p.t327 + p.t328 + p.t329 + p.t330)
            p.timeinswitch3 = p.switch3 * (Constants.t - p.switchtime3)
            p.outputinswitch3 = p.timeinswitch3 / 10
            p.totaloutput3 = p.output3 + p.outputinswitch3

    def set_switch4(self):
        for p in self.get_players():
            p.switchtime4 = p.switch4 * (p.additionaltime4 + p.t401 + p.t402 + p.t403 + p.t404 + p.t405 + p.t406 + p.t407 + p.t408 + p.t409 + p.t410 + p.t411 + p.t412 + p.t413 + p.t414 + p.t415 + p.t416 + p.t417 + p.t418 + p.t419 + p.t420 + p.t421 + p.t422 + p.t423 + p.t424 + p.t425 + p.t426 + p.t427 + p.t428 + p.t429 + p.t430)
            p.timeinswitch4 = p.switch4 * (Constants.t - p.switchtime4)
            p.outputinswitch4 = p.timeinswitch4 / 10
            p.totaloutput4 = p.output4 + p.outputinswitch4

    def set_switch5(self):
        for p in self.get_players():
            p.switchtime5 = p.switch5 * (p.additionaltime5 + p.t501 + p.t502 + p.t503 + p.t504 + p.t505 + p.t506 + p.t507 + p.t508 + p.t509 + p.t510 + p.t511 + p.t512 + p.t513 + p.t514 + p.t515 + p.t516 + p.t517 + p.t518 + p.t519 + p.t520 + p.t521 + p.t522 + p.t523 + p.t524 + p.t525 + p.t526 + p.t527 + p.t528 + p.t529 + p.t530)
            p.timeinswitch5 = p.switch5 * (Constants.t - p.switchtime5)
            p.outputinswitch5 = p.timeinswitch5 / 10
            p.totaloutput5 = p.output5 + p.outputinswitch5

    def set_switch6(self):
        for p in self.get_players():
            p.switchtime6 = p.switch6 * (p.additionaltime6 + p.t601 + p.t602 + p.t603 + p.t604 + p.t605 + p.t606 + p.t607 + p.t608 + p.t609 + p.t610 + p.t611 + p.t612 + p.t613 + p.t614 + p.t615 + p.t616 + p.t617 + p.t618 + p.t619 + p.t620 + p.t621 + p.t622 + p.t623 + p.t624 + p.t625 + p.t626 + p.t627 + p.t628 + p.t629 + p.t630)
            p.timeinswitch6 = p.switch6 * (Constants.t - p.switchtime6)
            p.outputinswitch6 = p.timeinswitch6 / 10
            p.totaloutput6 = p.output6 + p.outputinswitch6

    def set_switch7(self):
        for p in self.get_players():
            p.switchtime7 = p.switch7 * (p.additionaltime7 + p.t701 + p.t702 + p.t703 + p.t704 + p.t705 + p.t706 + p.t707 + p.t708 + p.t709 + p.t710 + p.t711 + p.t712 + p.t713 + p.t714 + p.t715 + p.t716 + p.t717 + p.t718 + p.t719 + p.t720 + p.t721 + p.t722 + p.t723 + p.t724 + p.t725 + p.t726 + p.t727 + p.t728 + p.t729 + p.t730)
            p.timeinswitch7 = p.switch7 *(Constants.t - p.switchtime7)
            p.outputinswitch7 = p.timeinswitch7 / 10
            p.totaloutput7 = p.output7 + p.outputinswitch7

    def set_switch8(self):
        for p in self.get_players():
            p.switchtime8 = p.switch8 * (p.additionaltime8 + p.t801 + p.t802 + p.t803 + p.t804 + p.t805 + p.t806 + p.t807 + p.t808 + p.t809 + p.t810 + p.t811 + p.t812 + p.t813 + p.t814 + p.t815 + p.t816 + p.t817 + p.t818 + p.t819 + p.t820 + p.t821 + p.t822 + p.t823 + p.t824 + p.t825 + p.t826 + p.t827 + p.t828 + p.t829 + p.t830)
            p.timeinswitch8 = p.switch8 * (Constants.t - p.switchtime8)
            p.outputinswitch8 = p.timeinswitch8 / 10
            p.totaloutput8 = p.output8 + p.outputinswitch8

    def set_pc3(self):
        for p in self.get_players():
            p.sharepc3 = p.share3 * 100

    def set_pc4(self):
        for p in self.get_players():
            p.sharepc4 = p.share4 * 100

    def set_pc5(self):
        for p in self.get_players():
            p.sharepc5 = p.share5 * 100

    def set_pc6(self):
        for p in self.get_players():
            p.sharepc6 = p.share6 * 100

    def set_pc7(self):
        for p in self.get_players():
            p.sharepc7 = p.share7 * 100

    def set_pc8(self):
        for p in self.get_players():
            p.sharepc8 = p.share8 * 100

    def set_letter(self):
        for p in self.get_players():
            if p.id_in_group == 1:
                p.letter = 'A'
            if p.id_in_group == 2:
                p.letter = 'B'
            if p.id_in_group == 3:
                p.letter = 'C'
            if p.id_in_group == 4:
                p.letter = 'D'
            if p.id_in_group == 5:
                p.letter = 'E'

class Player(BasePlayer):
    pay = models.FloatField()
    letter = models.CharField()
    luck = models.PositiveIntegerField(
        choices=[
            [1, 'Not at all'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, ''],
            [8, ''],
            [9, ''],
            [10, ''],
        ],
        widget=widgets.RadioSelectHorizontal()
    )
    skill = models.PositiveIntegerField(
        choices=[
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10'],
        ],
        widget=widgets.RadioSelectHorizontal()
    )
    # The next variables record the beliefs about the production of other's and the group
    avgbelief3 = models.PositiveIntegerField()
    #there is no advanced technology in round 3
    mostprodBTbelief3 = models.PositiveIntegerField()
    avgbelief4 = models.PositiveIntegerField()
    mostprodATbelief4 = models.PositiveIntegerField()
    mostprodBTbelief4 = models.PositiveIntegerField()
    avgbelief5 = models.PositiveIntegerField()
    mostprodATbelief5 = models.PositiveIntegerField()
    mostprodBTbelief5 = models.PositiveIntegerField()
    avgbelief6 = models.PositiveIntegerField()
    mostprodATbelief6 = models.PositiveIntegerField()
    mostprodBTbelief6 = models.PositiveIntegerField()
    avgbelief7 = models.PositiveIntegerField()
    mostprodATbelief7 = models.PositiveIntegerField()
    mostprodBTbelief7 = models.PositiveIntegerField()
    avgbelief8 = models.PositiveIntegerField()
    mostprodATbelief8 = models.PositiveIntegerField()
    mostprodBTbelief8 = models.PositiveIntegerField()

    # the next variables record the number of sequences solved
    output = models.FloatField(default=0)
    output0 = models.FloatField(default=0)
    output1 = models.FloatField(default=0)
    output2 = models.FloatField(default=0)
    output3 = models.FloatField(default=0)
    output4 = models.FloatField(default=0)
    output5 = models.FloatField(default=0)
    output6 = models.FloatField(default=0)
    output7 = models.FloatField(default=0)
    output8 = models.FloatField(default=0)
    rank3 = models.PositiveIntegerField()
    rank4 = models.PositiveIntegerField()
    rank5 = models.PositiveIntegerField()
    rank6 = models.PositiveIntegerField()
    rank7 = models.PositiveIntegerField()
    rank8 = models.PositiveIntegerField()
    share3 = models.FloatField(default=0)
    share4 = models.FloatField(default=0)
    share5 = models.FloatField(default=0)
    share6 = models.FloatField(default=0)
    share7 = models.FloatField(default=0)
    share8 = models.FloatField(default=0)
    sharepc3 = models.FloatField(default=0)
    sharepc4 = models.FloatField(default=0)
    sharepc5 = models.FloatField(default=0)
    sharepc6 = models.FloatField(default=0)
    sharepc7 = models.FloatField(default=0)
    sharepc8 = models.FloatField(default=0)
    switch1 = models.PositiveIntegerField(default=0)
    switch2 = models.PositiveIntegerField(default=0)
    switch3 = models.PositiveIntegerField(default=0)
    switch4 = models.PositiveIntegerField(default=0)
    switch5 = models.PositiveIntegerField(default=0)
    switch6 = models.PositiveIntegerField(default=0)
    switch7 = models.PositiveIntegerField(default=0)
    switch8 = models.PositiveIntegerField(default=0)
    switchtime1 = models.PositiveIntegerField(default=0)
    switchtime2 = models.PositiveIntegerField(default=0)
    switchtime3 = models.PositiveIntegerField(default=0)
    switchtime4 = models.PositiveIntegerField(default=0)
    switchtime5 = models.PositiveIntegerField(default=0)
    switchtime6 = models.PositiveIntegerField(default=0)
    switchtime7 = models.PositiveIntegerField(default=0)
    switchtime8 = models.PositiveIntegerField(default=0)
    timeinswitch1 = models.PositiveIntegerField(default=0)
    timeinswitch2 = models.PositiveIntegerField(default=0)
    timeinswitch3 = models.PositiveIntegerField(default=0)
    timeinswitch4 = models.PositiveIntegerField(default=0)
    timeinswitch5 = models.PositiveIntegerField(default=0)
    timeinswitch6 = models.PositiveIntegerField(default=0)
    timeinswitch7 = models.PositiveIntegerField(default=0)
    timeinswitch8 = models.PositiveIntegerField(default=0)
    additionaltime1 = models.PositiveIntegerField(default=0)
    additionaltime2 = models.PositiveIntegerField(default=0)
    additionaltime3 = models.PositiveIntegerField(default=0)
    additionaltime4 = models.PositiveIntegerField(default=0)
    additionaltime5 = models.PositiveIntegerField(default=0)
    additionaltime6 = models.PositiveIntegerField(default=0)
    additionaltime7 = models.PositiveIntegerField(default=0)
    additionaltime8 = models.PositiveIntegerField(default=0)
    outputinswitch = models.FloatField(default=0)
    outputinswitch1 = models.FloatField(default=0)
    outputinswitch2 = models.FloatField(default=0)
    outputinswitch3 = models.FloatField(default=0)
    outputinswitch4 = models.FloatField(default=0)
    outputinswitch5 = models.FloatField(default=0)
    outputinswitch6 = models.FloatField(default=0)
    outputinswitch7 = models.FloatField(default=0)
    outputinswitch8 = models.FloatField(default=0)
    totaloutput = models.FloatField(default=0)
    totaloutput1 = models.FloatField(default=0)
    totaloutput2 = models.FloatField(default=0)
    totaloutput3 = models.FloatField(default=0)
    totaloutput4 = models.FloatField(default=0)
    totaloutput5 = models.FloatField(default=0)
    totaloutput6 = models.FloatField(default=0)
    totaloutput7 = models.FloatField(default=0)
    totaloutput8 = models.FloatField(default=0)
    t001 = models.PositiveIntegerField(default=0)
    t002 = models.PositiveIntegerField(default=0)
    t003 = models.PositiveIntegerField(default=0)
    t004 = models.PositiveIntegerField(default=0)
    t005 = models.PositiveIntegerField(default=0)
    t101 = models.PositiveIntegerField(default=0)
    t102 = models.PositiveIntegerField(default=0)
    t103 = models.PositiveIntegerField(default=0)
    t104 = models.PositiveIntegerField(default=0)
    t105 = models.PositiveIntegerField(default=0)
    t106 = models.PositiveIntegerField(default=0)
    t107 = models.PositiveIntegerField(default=0)
    t108 = models.PositiveIntegerField(default=0)
    t109 = models.PositiveIntegerField(default=0)
    t110 = models.PositiveIntegerField(default=0)
    t111 = models.PositiveIntegerField(default=0)
    t112 = models.PositiveIntegerField(default=0)
    t113 = models.PositiveIntegerField(default=0)
    t114 = models.PositiveIntegerField(default=0)
    t115 = models.PositiveIntegerField(default=0)
    t116 = models.PositiveIntegerField(default=0)
    t117 = models.PositiveIntegerField(default=0)
    t118 = models.PositiveIntegerField(default=0)
    t119 = models.PositiveIntegerField(default=0)
    t120 = models.PositiveIntegerField(default=0)
    t121 = models.PositiveIntegerField(default=0)
    t122 = models.PositiveIntegerField(default=0)
    t123 = models.PositiveIntegerField(default=0)
    t124 = models.PositiveIntegerField(default=0)
    t125 = models.PositiveIntegerField(default=0)
    t126 = models.PositiveIntegerField(default=0)
    t127 = models.PositiveIntegerField(default=0)
    t128 = models.PositiveIntegerField(default=0)
    t129 = models.PositiveIntegerField(default=0)
    t130 = models.PositiveIntegerField(default=0)
    t201 = models.PositiveIntegerField(default=0)
    t202 = models.PositiveIntegerField(default=0)
    t203 = models.PositiveIntegerField(default=0)
    t204 = models.PositiveIntegerField(default=0)
    t205 = models.PositiveIntegerField(default=0)
    t206 = models.PositiveIntegerField(default=0)
    t207 = models.PositiveIntegerField(default=0)
    t208 = models.PositiveIntegerField(default=0)
    t209 = models.PositiveIntegerField(default=0)
    t210 = models.PositiveIntegerField(default=0)
    t211 = models.PositiveIntegerField(default=0)
    t212 = models.PositiveIntegerField(default=0)
    t213 = models.PositiveIntegerField(default=0)
    t214 = models.PositiveIntegerField(default=0)
    t215 = models.PositiveIntegerField(default=0)
    t216 = models.PositiveIntegerField(default=0)
    t217 = models.PositiveIntegerField(default=0)
    t218 = models.PositiveIntegerField(default=0)
    t219 = models.PositiveIntegerField(default=0)
    t220 = models.PositiveIntegerField(default=0)
    t221 = models.PositiveIntegerField(default=0)
    t222 = models.PositiveIntegerField(default=0)
    t223 = models.PositiveIntegerField(default=0)
    t224 = models.PositiveIntegerField(default=0)
    t225 = models.PositiveIntegerField(default=0)
    t226 = models.PositiveIntegerField(default=0)
    t227 = models.PositiveIntegerField(default=0)
    t228 = models.PositiveIntegerField(default=0)
    t229 = models.PositiveIntegerField(default=0)
    t230 = models.PositiveIntegerField(default=0)
    t301 = models.PositiveIntegerField(default=0)
    t302 = models.PositiveIntegerField(default=0)
    t303 = models.PositiveIntegerField(default=0)
    t304 = models.PositiveIntegerField(default=0)
    t305 = models.PositiveIntegerField(default=0)
    t306 = models.PositiveIntegerField(default=0)
    t307 = models.PositiveIntegerField(default=0)
    t308 = models.PositiveIntegerField(default=0)
    t309 = models.PositiveIntegerField(default=0)
    t310 = models.PositiveIntegerField(default=0)
    t311 = models.PositiveIntegerField(default=0)
    t312 = models.PositiveIntegerField(default=0)
    t313 = models.PositiveIntegerField(default=0)
    t314 = models.PositiveIntegerField(default=0)
    t315 = models.PositiveIntegerField(default=0)
    t316 = models.PositiveIntegerField(default=0)
    t317 = models.PositiveIntegerField(default=0)
    t318 = models.PositiveIntegerField(default=0)
    t319 = models.PositiveIntegerField(default=0)
    t320 = models.PositiveIntegerField(default=0)
    t321 = models.PositiveIntegerField(default=0)
    t322 = models.PositiveIntegerField(default=0)
    t323 = models.PositiveIntegerField(default=0)
    t324 = models.PositiveIntegerField(default=0)
    t325 = models.PositiveIntegerField(default=0)
    t326 = models.PositiveIntegerField(default=0)
    t327 = models.PositiveIntegerField(default=0)
    t328 = models.PositiveIntegerField(default=0)
    t329 = models.PositiveIntegerField(default=0)
    t330 = models.PositiveIntegerField(default=0)
    t401 = models.PositiveIntegerField(default=0)
    t402 = models.PositiveIntegerField(default=0)
    t403 = models.PositiveIntegerField(default=0)
    t404 = models.PositiveIntegerField(default=0)
    t405 = models.PositiveIntegerField(default=0)
    t406 = models.PositiveIntegerField(default=0)
    t407 = models.PositiveIntegerField(default=0)
    t408 = models.PositiveIntegerField(default=0)
    t409 = models.PositiveIntegerField(default=0)
    t410 = models.PositiveIntegerField(default=0)
    t411 = models.PositiveIntegerField(default=0)
    t412 = models.PositiveIntegerField(default=0)
    t413 = models.PositiveIntegerField(default=0)
    t414 = models.PositiveIntegerField(default=0)
    t415 = models.PositiveIntegerField(default=0)
    t416 = models.PositiveIntegerField(default=0)
    t417 = models.PositiveIntegerField(default=0)
    t418 = models.PositiveIntegerField(default=0)
    t419 = models.PositiveIntegerField(default=0)
    t420 = models.PositiveIntegerField(default=0)
    t421 = models.PositiveIntegerField(default=0)
    t422 = models.PositiveIntegerField(default=0)
    t423 = models.PositiveIntegerField(default=0)
    t424 = models.PositiveIntegerField(default=0)
    t425 = models.PositiveIntegerField(default=0)
    t426 = models.PositiveIntegerField(default=0)
    t427 = models.PositiveIntegerField(default=0)
    t428 = models.PositiveIntegerField(default=0)
    t429 = models.PositiveIntegerField(default=0)
    t430 = models.PositiveIntegerField(default=0)
    t501 = models.PositiveIntegerField(default=0)
    t502 = models.PositiveIntegerField(default=0)
    t503 = models.PositiveIntegerField(default=0)
    t504 = models.PositiveIntegerField(default=0)
    t505 = models.PositiveIntegerField(default=0)
    t506 = models.PositiveIntegerField(default=0)
    t507 = models.PositiveIntegerField(default=0)
    t508 = models.PositiveIntegerField(default=0)
    t509 = models.PositiveIntegerField(default=0)
    t510 = models.PositiveIntegerField(default=0)
    t511 = models.PositiveIntegerField(default=0)
    t512 = models.PositiveIntegerField(default=0)
    t513 = models.PositiveIntegerField(default=0)
    t514 = models.PositiveIntegerField(default=0)
    t515 = models.PositiveIntegerField(default=0)
    t516 = models.PositiveIntegerField(default=0)
    t517 = models.PositiveIntegerField(default=0)
    t518 = models.PositiveIntegerField(default=0)
    t519 = models.PositiveIntegerField(default=0)
    t520 = models.PositiveIntegerField(default=0)
    t521 = models.PositiveIntegerField(default=0)
    t522 = models.PositiveIntegerField(default=0)
    t523 = models.PositiveIntegerField(default=0)
    t524 = models.PositiveIntegerField(default=0)
    t525 = models.PositiveIntegerField(default=0)
    t526 = models.PositiveIntegerField(default=0)
    t527 = models.PositiveIntegerField(default=0)
    t528 = models.PositiveIntegerField(default=0)
    t529 = models.PositiveIntegerField(default=0)
    t530 = models.PositiveIntegerField(default=0)
    t601 = models.PositiveIntegerField(default=0)
    t602 = models.PositiveIntegerField(default=0)
    t603 = models.PositiveIntegerField(default=0)
    t604 = models.PositiveIntegerField(default=0)
    t605 = models.PositiveIntegerField(default=0)
    t606 = models.PositiveIntegerField(default=0)
    t607 = models.PositiveIntegerField(default=0)
    t608 = models.PositiveIntegerField(default=0)
    t609 = models.PositiveIntegerField(default=0)
    t610 = models.PositiveIntegerField(default=0)
    t611 = models.PositiveIntegerField(default=0)
    t612 = models.PositiveIntegerField(default=0)
    t613 = models.PositiveIntegerField(default=0)
    t614 = models.PositiveIntegerField(default=0)
    t615 = models.PositiveIntegerField(default=0)
    t616 = models.PositiveIntegerField(default=0)
    t617 = models.PositiveIntegerField(default=0)
    t618 = models.PositiveIntegerField(default=0)
    t619 = models.PositiveIntegerField(default=0)
    t620 = models.PositiveIntegerField(default=0)
    t621 = models.PositiveIntegerField(default=0)
    t622 = models.PositiveIntegerField(default=0)
    t623 = models.PositiveIntegerField(default=0)
    t624 = models.PositiveIntegerField(default=0)
    t625 = models.PositiveIntegerField(default=0)
    t626 = models.PositiveIntegerField(default=0)
    t627 = models.PositiveIntegerField(default=0)
    t628 = models.PositiveIntegerField(default=0)
    t629 = models.PositiveIntegerField(default=0)
    t630 = models.PositiveIntegerField(default=0)
    t701 = models.PositiveIntegerField(default=0)
    t702 = models.PositiveIntegerField(default=0)
    t703 = models.PositiveIntegerField(default=0)
    t704 = models.PositiveIntegerField(default=0)
    t705 = models.PositiveIntegerField(default=0)
    t706 = models.PositiveIntegerField(default=0)
    t707 = models.PositiveIntegerField(default=0)
    t708 = models.PositiveIntegerField(default=0)
    t709 = models.PositiveIntegerField(default=0)
    t710 = models.PositiveIntegerField(default=0)
    t711 = models.PositiveIntegerField(default=0)
    t712 = models.PositiveIntegerField(default=0)
    t713 = models.PositiveIntegerField(default=0)
    t714 = models.PositiveIntegerField(default=0)
    t715 = models.PositiveIntegerField(default=0)
    t716 = models.PositiveIntegerField(default=0)
    t717 = models.PositiveIntegerField(default=0)
    t718 = models.PositiveIntegerField(default=0)
    t719 = models.PositiveIntegerField(default=0)
    t720 = models.PositiveIntegerField(default=0)
    t721 = models.PositiveIntegerField(default=0)
    t722 = models.PositiveIntegerField(default=0)
    t723 = models.PositiveIntegerField(default=0)
    t724 = models.PositiveIntegerField(default=0)
    t725 = models.PositiveIntegerField(default=0)
    t726 = models.PositiveIntegerField(default=0)
    t727 = models.PositiveIntegerField(default=0)
    t728 = models.PositiveIntegerField(default=0)
    t729 = models.PositiveIntegerField(default=0)
    t730 = models.PositiveIntegerField(default=0)
    t801 = models.PositiveIntegerField(default=0)
    t802 = models.PositiveIntegerField(default=0)
    t803 = models.PositiveIntegerField(default=0)
    t804 = models.PositiveIntegerField(default=0)
    t805 = models.PositiveIntegerField(default=0)
    t806 = models.PositiveIntegerField(default=0)
    t807 = models.PositiveIntegerField(default=0)
    t808 = models.PositiveIntegerField(default=0)
    t809 = models.PositiveIntegerField(default=0)
    t810 = models.PositiveIntegerField(default=0)
    t811 = models.PositiveIntegerField(default=0)
    t812 = models.PositiveIntegerField(default=0)
    t813 = models.PositiveIntegerField(default=0)
    t814 = models.PositiveIntegerField(default=0)
    t815 = models.PositiveIntegerField(default=0)
    t816 = models.PositiveIntegerField(default=0)
    t817 = models.PositiveIntegerField(default=0)
    t818 = models.PositiveIntegerField(default=0)
    t819 = models.PositiveIntegerField(default=0)
    t820 = models.PositiveIntegerField(default=0)
    t821 = models.PositiveIntegerField(default=0)
    t822 = models.PositiveIntegerField(default=0)
    t823 = models.PositiveIntegerField(default=0)
    t824 = models.PositiveIntegerField(default=0)
    t825 = models.PositiveIntegerField(default=0)
    t826 = models.PositiveIntegerField(default=0)
    t827 = models.PositiveIntegerField(default=0)
    t828 = models.PositiveIntegerField(default=0)
    t829 = models.PositiveIntegerField(default=0)
    t830 = models.PositiveIntegerField(default=0)

    def set_switch1(self):
        self.switchtime1 = self.switch1 * (self.additionaltime1 + self.t101 + self.t102 + self.t103 + self.t104 + self.t105 + self.t106 + self.t107 + self.t108 + self.t109 + self.t110 + self.t111 + self.t112 + self.t113 + self.t114 + self.t115 + self.t116 + self.t117 + self.t118 + self.t119 + self.t120 + self.t121 + self.t122 + self.t123 + self.t124 + self.t125 + self.t126 + self.t127 + self.t128 + self.t129 + self.t130)
        self.timeinswitch1 = self.switch1 * (Constants.t - self.switchtime1)
        self.outputinswitch1 =  self.timeinswitch1 / 10
        self.totaloutput1 = self.output1 + self.outputinswitch1

    def set_switch2(self):
        self.switchtime2 = self.switch2 * (self.additionaltime2 + self.t201 + self.t202 + self.t203 + self.t204 + self.t205 + self.t206 + self.t207 + self.t208 + self.t209 + self.t210 + self.t211 + self.t212 + self.t213 + self.t214 + self.t215 + self.t216 + self.t217 + self.t218 + self.t219 + self.t220 + self.t221 + self.t222 + self.t223 + self.t224 + self.t225 + self.t226 + self.t227 + self.t228 + self.t229 + self.t230)
        self.timeinswitch2 = self.switch2 * (Constants.t - self.switchtime2)
        self.outputinswitch2 =  self.timeinswitch2 / 10
        self.totaloutput2 = self.output2 + self.outputinswitch2

    def set_output(self):
        self.output = self.output1 + self.output2 + self.output3 + self.output4 + self.output5 + self.output6 + self.output7 + self.output8
        self.outputinswitch = self.outputinswitch1 + self.outputinswitch2 + self.outputinswitch3 + self.outputinswitch4 + self.outputinswitch5 + self.outputinswitch6 + self.outputinswitch7 + self.outputinswitch8
        self.totaloutput = self.totaloutput1 + self.totaloutput2 + self.totaloutput3 + self.totaloutput4 + self.totaloutput5 + self.totaloutput6 + self.totaloutput7 + self.totaloutput8
        self.pay = self.totaloutput * Constants.eurosper_token