from django.test import TestCase

from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title = 'Talk Title',
            # start = '10:00',
            # description = 'Talk description.'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """ Talk has many speakers and vice-versa """
        self.talk.speakers.create(
            name='John Doe',
            slug='john-doe',
            website='http://johndoe.com'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Talk Title', str(self.talk))