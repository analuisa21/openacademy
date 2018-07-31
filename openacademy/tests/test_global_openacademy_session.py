# -*- coding: utf-8 -*-

from openerp.test.common import TransactionCase

class GlobalTestOpenAcademySession(TransactionCase):
    '''
    This create global test to sessions
    '''
    # Seudo-constructor method
    def setUp(self):
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.partner_vauxoo = self.env.ref('base.res_partner_23')
        self.course = self.env.ref('openacademy.course0')

    # Generic methods
    #def create_session(selfself, name,):

    # Test methods
    def test_10_instructor_is_attende(self):
        '''
        Check that raise of 'A session's instructor can't be an attendee'
        '''
        self.session.create({
            'name': 'Session test 1',
            'seats': 1,
            'instructor_id': self.partner_vauxoo.id,
            'attendee_ids': [(6,0, [self.partner_vauxoo.id])],


        })