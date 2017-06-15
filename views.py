from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

import numpy as np

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass

class Welcome_wait(WaitPage):
    def after_all_groups_arrive(self):
        self.group.set_role()

class Waiting(WaitPage):
    pass

class Waiting3(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_output3()
        order3 = np.random.choice(5,5,replace=False, p=[p.share3 for p in self.group.get_players()])
        self.session.vars['order3'] = order3
        self.group.set_switch3()
        self.group.set_pc3()
        for p in self.group.get_players():
            if p.id_in_group == order3[0]:
                p.rank3 = 1
            if p.id_in_group == order3[1]:
                p.rank3 = 2
            if p.id_in_group == order3[2]:
                p.rank3 = 3
            if p.id_in_group == order3[3]:
                p.rank3 = 4
            if p.id_in_group == order3[4]:
                p.rank3 = 5

class Waiting4(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_output4()
        order4 = np.random.choice(5,5,replace=False, p=[p.share4 for p in self.group.get_players()])
        self.session.vars['order4'] = order4
        self.group.set_switch4()
        self.group.set_pc4()
        for p in self.group.get_players():
            if p.id_in_group == order4[0]:
                p.rank4 = 1
            if p.id_in_group == order4[1]:
                p.rank4 = 2
            if p.id_in_group == order4[2]:
                p.rank4 = 3
            if p.id_in_group == order4[3]:
                p.rank4 = 4
            if p.id_in_group == order4[4]:
                p.rank4 = 5

class Waiting5(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_output5()
        order5 = np.random.choice(5,5,replace=False, p=[p.share5 for p in self.group.get_players()])
        self.session.vars['order5'] = order5
        self.group.set_switch5()
        self.group.set_pc5()
        for p in self.group.get_players():
            if p.id_in_group == order5[0]:
                p.rank5 = 1
            if p.id_in_group == order5[1]:
                p.rank5 = 2
            if p.id_in_group == order5[2]:
                p.rank5 = 3
            if p.id_in_group == order5[3]:
                p.rank5 = 4
            if p.id_in_group == order5[4]:
                p.rank5 = 5

class Waiting6(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_output6()
        order6 = np.random.choice(5,5,replace=False, p=[p.share6 for p in self.group.get_players()])
        self.session.vars['order6'] = order6
        self.group.set_switch6()
        self.group.set_pc6()
        for p in self.group.get_players():
            if p.id_in_group == order6[0]:
                p.rank6 = 1
            if p.id_in_group == order6[1]:
                p.rank6 = 2
            if p.id_in_group == order6[2]:
                p.rank6 = 3
            if p.id_in_group == order6[3]:
                p.rank6 = 4
            if p.id_in_group == order6[4]:
                p.rank6 = 5

class Waiting7(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_output7()
        order7 = np.random.choice(5,5,replace=False, p=[p.share7 for p in self.group.get_players()])
        self.session.vars['order7'] = order7
        self.group.set_switch7()
        self.group.set_pc7()
        for p in self.group.get_players():
            if p.id_in_group == order7[0]:
                p.rank7 = 1
            if p.id_in_group == order7[1]:
                p.rank7 = 2
            if p.id_in_group == order7[2]:
                p.rank7 = 3
            if p.id_in_group == order7[3]:
                p.rank7 = 4
            if p.id_in_group == order7[4]:
                p.rank7 = 5

class Waiting8(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_output8()
        order8 = np.random.choice(5,5,replace=False, p=[p.share8 for p in self.group.get_players()])
        self.session.vars['order8'] = order8
        self.group.set_switch8()
        self.group.set_pc8()
        for p in self.group.get_players():
            if p.id_in_group == order8[0]:
                p.rank8 = 1
            if p.id_in_group == order8[1]:
                p.rank8 = 2
            if p.id_in_group == order8[2]:
                p.rank8 = 3
            if p.id_in_group == order8[3]:
                p.rank8 = 4
            if p.id_in_group == order8[4]:
                p.rank8 = 5

class Introduction(Page):
    pass

class Task_Instructions(Page):
    pass

class Switch_Instructions(Page):
    pass

class Technology_Instructions(Page):
    pass

class Competition_Instructions_1(Page):
    pass

class Competition_Instructions_2_Example(Page):
    pass

class Competition_Instructions_3(Page):
    pass

class Questionnaire(Page):
    form_model = models.Player
    form_fields = ['luck', 'skill']

class Thank_you(Page):
    pass

class Round0(Page):
    form_model = models.Player
    form_fields = ['t001',
                   't002',
                   't003',
                   't004',
                   't005',
                   'output0'
                   ]

class Round1(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t101',
                   't102',
                   't103',
                   't104',
                   't105',
                   't106',
                   't107',
                   't108',
                   't109',
                   't110',
                   't111',
                   't112',
                   't113',
                   't114',
                   't115',
                   't116',
                   't117',
                   't118',
                   't119',
                   't120',
                   't121',
                   't122',
                   't123',
                   't124',
                   't125',
                   't126',
                   't127',
                   't128',
                   't129',
                   't130',
                   'output1',
                   'switch1',
                   'additionaltime1'
                   ]

    def before_next_page(self):
        self.player.set_switch1()

class Round2(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t201',
                   't202',
                   't203',
                   't204',
                   't205',
                   't206',
                   't207',
                   't208',
                   't209',
                   't210',
                   't211',
                   't212',
                   't213',
                   't214',
                   't215',
                   't216',
                   't217',
                   't218',
                   't219',
                   't220',
                   't221',
                   't222',
                   't223',
                   't224',
                   't225',
                   't226',
                   't227',
                   't228',
                   't229',
                   't230',
                   'output2',
                   'switch2',
                   'additionaltime2'
                   ]

    def before_next_page(self):
        self.player.set_switch2()

class Round3(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t301',
                   't302',
                   't303',
                   't304',
                   't305',
                   't306',
                   't307',
                   't308',
                   't309',
                   't310',
                   't311',
                   't312',
                   't313',
                   't314',
                   't315',
                   't316',
                   't317',
                   't318',
                   't319',
                   't320',
                   't321',
                   't322',
                   't323',
                   't324',
                   't325',
                   't326',
                   't327',
                   't328',
                   't329',
                   't330',
                   'output3',
                   'switch3',
                   'additionaltime3'
                   ]

    def before_next_page(self):
        if self.player.output3 == 0:
            self.player.output3 = 0.0000001

class Round4a(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t401',
                   't402',
                   't403',
                   't404',
                   't405',
                   't406',
                   't407',
                   't408',
                   't409',
                   't410',
                   't411',
                   't412',
                   't413',
                   't414',
                   't415',
                   't416',
                   't417',
                   't418',
                   't419',
                   't420',
                   't421',
                   't422',
                   't423',
                   't424',
                   't425',
                   't426',
                   't427',
                   't428',
                   't429',
                   't430',
                   'output4',
                   'switch4',
                   'additionaltime4'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order3'][0] + 1 or self.player.id_in_group == self.session.vars['order3'][1] + 1

    def before_next_page(self):
        if self.player.output4 == 0:
            self.player.output4 = 0.0000001

class Round4b(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t401',
                   't402',
                   't403',
                   't404',
                   't405',
                   't406',
                   't407',
                   't408',
                   't409',
                   't410',
                   't411',
                   't412',
                   't413',
                   't414',
                   't415',
                   't416',
                   't417',
                   't418',
                   't419',
                   't420',
                   't421',
                   't422',
                   't423',
                   't424',
                   't425',
                   't426',
                   't427',
                   't428',
                   't429',
                   't430',
                   'output4',
                   'switch4',
                   'additionaltime4'
                   ]
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order3'][2] + 1 or self.player.id_in_group == self.session.vars['order3'][3] + 1 or self.player.id_in_group == self.session.vars['order3'][4] + 1

    def before_next_page(self):
        if self.player.output4 == 0:
            self.player.output4 = 0.0000001

class Round5a(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t501',
                   't502',
                   't503',
                   't504',
                   't505',
                   't506',
                   't507',
                   't508',
                   't509',
                   't510',
                   't511',
                   't512',
                   't513',
                   't514',
                   't515',
                   't516',
                   't517',
                   't518',
                   't519',
                   't520',
                   't521',
                   't522',
                   't523',
                   't524',
                   't525',
                   't526',
                   't527',
                   't528',
                   't529',
                   't530',
                   'output5',
                   'switch5',
                   'additionaltime5'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order4'][0] + 1 or self.player.id_in_group == self.session.vars['order4'][1] + 1

    def before_next_page(self):
        if self.player.output5 == 0:
            self.player.output5 = 0.0000001

class Round5b(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t501',
                   't502',
                   't503',
                   't504',
                   't505',
                   't506',
                   't507',
                   't508',
                   't509',
                   't510',
                   't511',
                   't512',
                   't513',
                   't514',
                   't515',
                   't516',
                   't517',
                   't518',
                   't519',
                   't520',
                   't521',
                   't522',
                   't523',
                   't524',
                   't525',
                   't526',
                   't527',
                   't528',
                   't529',
                   't530',
                   'output5',
                   'switch5',
                   'additionaltime5'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order4'][2] + 1 or self.player.id_in_group == self.session.vars['order4'][3] + 1 or self.player.id_in_group == self.session.vars['order4'][4] + 1

    def before_next_page(self):
        if self.player.output5 == 0:
            self.player.output5 = 0.0000001

class Round6a(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t601',
                   't602',
                   't603',
                   't604',
                   't605',
                   't606',
                   't607',
                   't608',
                   't609',
                   't610',
                   't611',
                   't612',
                   't613',
                   't614',
                   't615',
                   't616',
                   't617',
                   't618',
                   't619',
                   't620',
                   't621',
                   't622',
                   't623',
                   't624',
                   't625',
                   't626',
                   't627',
                   't628',
                   't629',
                   't630',
                   'output6',
                   'switch6',
                   'additionaltime6'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order5'][0] + 1 or self.player.id_in_group == self.session.vars['order5'][1] + 1

    def before_next_page(self):
        if self.player.output6 == 0:
            self.player.output6 = 0.0000001

class Round6b(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t601',
                   't602',
                   't603',
                   't604',
                   't605',
                   't606',
                   't607',
                   't608',
                   't609',
                   't610',
                   't611',
                   't612',
                   't613',
                   't614',
                   't615',
                   't616',
                   't617',
                   't618',
                   't619',
                   't620',
                   't621',
                   't622',
                   't623',
                   't624',
                   't625',
                   't626',
                   't627',
                   't628',
                   't629',
                   't630',
                   'output6',
                   'switch6',
                   'additionaltime6'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order5'][2] + 1 or self.player.id_in_group == self.session.vars['order5'][3] + 1 or self.player.id_in_group == self.session.vars['order5'][4] + 1

    def before_next_page(self):
        if self.player.output6 == 0:
            self.player.output6 = 0.0000001

class Round7a(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t701',
                   't702',
                   't703',
                   't704',
                   't705',
                   't706',
                   't707',
                   't708',
                   't709',
                   't710',
                   't711',
                   't712',
                   't713',
                   't714',
                   't715',
                   't716',
                   't717',
                   't718',
                   't719',
                   't720',
                   't721',
                   't722',
                   't723',
                   't724',
                   't725',
                   't726',
                   't727',
                   't728',
                   't729',
                   't730',
                   'output7',
                   'switch7',
                   'additionaltime7'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order6'][0] + 1 or self.player.id_in_group == self.session.vars['order6'][1] + 1

    def before_next_page(self):
        if self.player.output7 == 0:
            self.player.output7 = 0.0000001

class Round7b(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t701',
                   't702',
                   't703',
                   't704',
                   't705',
                   't706',
                   't707',
                   't708',
                   't709',
                   't710',
                   't711',
                   't712',
                   't713',
                   't714',
                   't715',
                   't716',
                   't717',
                   't718',
                   't719',
                   't720',
                   't721',
                   't722',
                   't723',
                   't724',
                   't725',
                   't726',
                   't727',
                   't728',
                   't729',
                   't730',
                   'output7',
                   'switch7',
                   'additionaltime7'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order6'][2] + 1 or self.player.id_in_group == self.session.vars['order6'][3] + 1 or self.player.id_in_group == self.session.vars['order6'][4] + 1

    def before_next_page(self):
        if self.player.output7 == 0:
            self.player.output7 = 0.0000001

class Round8a(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t801',
                   't802',
                   't803',
                   't804',
                   't805',
                   't806',
                   't807',
                   't808',
                   't809',
                   't810',
                   't811',
                   't812',
                   't813',
                   't814',
                   't815',
                   't816',
                   't817',
                   't818',
                   't819',
                   't820',
                   't821',
                   't822',
                   't823',
                   't824',
                   't825',
                   't826',
                   't827',
                   't828',
                   't829',
                   't830',
                   'output8',
                   'switch8',
                   'additionaltime8'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order7'][0] + 1 or self.player.id_in_group == self.session.vars['order7'][1] + 1
    
    def before_next_page(self):
        if self.player.output8 == 0:
            self.player.output8 = 0.0000001
        self.player.set_output()
        
class Round8b(Page):
    timeout_seconds = Constants.t
    form_model = models.Player
    form_fields = ['t801',
                   't802',
                   't803',
                   't804',
                   't805',
                   't806',
                   't807',
                   't808',
                   't809',
                   't810',
                   't811',
                   't812',
                   't813',
                   't814',
                   't815',
                   't816',
                   't817',
                   't818',
                   't819',
                   't820',
                   't821',
                   't822',
                   't823',
                   't824',
                   't825',
                   't826',
                   't827',
                   't828',
                   't829',
                   't830',
                   'output8',
                   'switch8',
                   'additionaltime8'
                   ]

    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order7'][2] + 1 or self.player.id_in_group == self.session.vars['order7'][3] + 1 or self.player.id_in_group == self.session.vars['order7'][4] + 1
    
    def before_next_page(self):
        if self.player.output8 == 0:
            self.player.output8 = 0.0000001
        self.player.set_output()

class Feedback_Round1(Page):
    pass

class Feedback_Round2(Page):
    pass

class Feedback_Round3a(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order3'][0] + 1 or self.player.id_in_group == self.session.vars['order3'][1] + 1

class Feedback_Round4a(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order4'][0] + 1 or self.player.id_in_group == self.session.vars['order4'][1] + 1

class Feedback_Round5a(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order5'][0] + 1 or self.player.id_in_group == self.session.vars['order5'][1] + 1

class Feedback_Round6a(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order6'][0] + 1 or self.player.id_in_group == self.session.vars['order6'][1] + 1

class Feedback_Round7a(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order7'][0] + 1 or self.player.id_in_group == self.session.vars['order7'][1] + 1

class Feedback_Round3b(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order3'][2] + 1 or self.player.id_in_group == self.session.vars['order3'][3] + 1 or self.player.id_in_group == self.session.vars['order3'][4] + 1

class Feedback_Round4b(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order4'][2] + 1 or self.player.id_in_group == self.session.vars['order4'][3] + 1 or self.player.id_in_group == self.session.vars['order4'][4] + 1

class Feedback_Round5b(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order5'][2] + 1 or self.player.id_in_group == self.session.vars['order5'][3] + 1 or self.player.id_in_group == self.session.vars['order5'][4] + 1

class Feedback_Round6b(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order6'][2] + 1 or self.player.id_in_group == self.session.vars['order6'][3] + 1 or self.player.id_in_group == self.session.vars['order6'][4] + 1

class Feedback_Round7b(Page):
    timeout_seconds = Constants.tf
    def is_displayed(self):
        return self.player.id_in_group == self.session.vars['order7'][2] + 1 or self.player.id_in_group == self.session.vars['order7'][3] + 1 or self.player.id_in_group == self.session.vars['order7'][4] + 1

class Feedback_Round8(Page):
    pass

class Beliefs3(Page):
    form_model = models.Player
    form_fields = ['avgbelief3',
                   'mostprodATbelief3',
                   'mostprodBTbelief3'
                   ]
class Beliefs4(Page):
    form_model = models.Player
    form_fields = ['avgbelief4',
                   'mostprodATbelief4',
                   'mostprodBTbelief4'
                   ]

class Beliefs5(Page):
    form_model = models.Player
    form_fields = ['avgbelief5',
                   'mostprodATbelief5',
                   'mostprodBTbelief5'
                   ]

class Beliefs6(Page):
    form_model = models.Player
    form_fields = ['avgbelief6',
                   'mostprodATbelief6',
                   'mostprodBTbelief6'
                   ]

class Beliefs7(Page):
    form_model = models.Player
    form_fields = ['avgbelief7',
                   'mostprodATbelief7',
                   'mostprodBTbelief7'
                   ]

class Beliefs8(Page):
    form_model = models.Player
    form_fields = ['avgbelief8',
                   'mostprodATbelief8',
                   'mostprodBTbelief8'
                   ]

page_sequence = [
    Welcome,
    Welcome_wait,
#    Introduction,
 #   Task_Instructions,
 #   Round0,
 #   Waiting,
 #   Switch_Instructions,
#    Round1,
#    Waiting,
 #   Feedback_Round1,
 #   Technology_Instructions,
 #   Round2,
#    Waiting,
 #   Feedback_Round2,
 #   Competition_Instructions_1,
 #   Competition_Instructions_2_Example,
 #   Competition_Instructions_3,
 #   Beliefs3,
 #   Waiting,
    Round3,
    Waiting3,
    Feedback_Round3a,
    Feedback_Round3b,
    Beliefs4,
    Waiting,
    Round4a,
    Round4b,
    Waiting4,
    Feedback_Round4a,
    Feedback_Round4b,
    Beliefs5,
    Waiting,
    Round5a,
    Round5b,
    Waiting5,
    Feedback_Round5a,
    Feedback_Round5b,
    Beliefs6,
    Waiting,
    Round6a,
    Round6b,
    Waiting6,
    Feedback_Round6a,
    Feedback_Round6b,
    Beliefs7,
    Waiting,
    Round7a,
    Round7b,
    Waiting7,
    Feedback_Round7a,
    Feedback_Round7b,
    Beliefs8,
    Waiting,
    Round8a,
    Round8b,
    Waiting8,
    Feedback_Round8,
    Questionnaire,
    Thank_you,
]
