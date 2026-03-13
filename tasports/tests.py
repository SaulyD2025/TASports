from django.test import TestCase
from .models import Teams, CustomUser, Game

class TeamsTest(TestCase):
    def setUp(self):
        Teams.objects.create(FullName='Tune Squad', id=100)
        Teams.objects.create(FullName='Monstars', id=200)

    def testteams(self):
        tunesquad = Teams.objects.get(id=100)
        monstars = Teams.objects.get(id=200)
        self.assertEqual(tunesquad.FullName, 'Tune Squad')
        self.assertEqual(monstars.FullName, 'Monstars')


class GameTest(TestCase):
    def setUp(self):
        Game.objects.create(hometeam_name='Tune Squad', awayteam_name='Monstars', hometeam_id=100, awayteam_id=200)

    def testgames(self):
        game = Game.objects.get(hometeam_id=100)
        self.assertEqual(game.hometeam_name, 'Tune Squad')
        self.assertEqual(game.awayteam_name, 'Monstars')
        self.assertEqual(game.awayteam_id, 200)
        self.assertEqual(game.hometeam_id, 100)


# Create your tests here.
