# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError

from openerp.test.common import TransactionCase
from openerp.tools import mute_logger

# import pdb;pdb.set_trace()

class GlobalTestOpenAcademyCourse(TransactionCase):
    '''
    Global test to openacademy course model.
    Test create course and trigger contraints.
    '''

    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        # self.variable = 'hello world'
        self.course = self.env['openacademy.course']

    # Method of class that don't is test
    def create_course(self, course_name, course_description,
                      course_responsable_id):
        # create  a course with parameters received
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsable_id': course_responsable_id,

        })
        return course_id

    # Method of test startswith 'def test_*(self):'

    # Mute the error openerp.sql_db to avoid it in log.
    @mute_logger('openacademy.sql_db')
    def test_01_same_name_description(self):
        '''
        Test create a course whit same name and description.
        To test contraint of name different to description.
        '''
        # Error raised expected with message expected
            with self.assertRaisesRegexp(
                IntegrityError,
            'new row for relation "openacademy_course" violates'
            'check constraint "openacademy_course_name_description_check"'
            ):
        # Create a course with same name and description to raise error.
        self.create_course('test', 'test', None)

    @mute_logger('openacademy.sql_db')
    def test_02_two_courses_same_name(self):
        '''
        Test to create two courses with same name.
        To raise constraint of unique name
        '''
        new_id = self.create_course('test', 'test_description', None)
        print "new_id", new_id
        with self.assertRaisesRegexp(
                IntegrityError,
                'duplicate key value violates unique constraint "openacademy_course_name_inique"'
                'constraint "openacademy_course_name_unique"'
        ):
        new_id2 = self.create_course('test', 'test_description', None)
        print "new_id2", new_id2
    def test_15_duplicate_course(self):
        '''
        Test to duplicate a course and check that work fine
        '''
        course = self.env.ref('open')