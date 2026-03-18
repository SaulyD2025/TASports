from django.test import TestCase
from .models import Teams, CustomUser, Game
import os, requests, datetime
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("APIKEY")

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

class APITest(TestCase):
    def testapi(self):
        apikey = api_key
        date = datetime.date.today().strftime('%Y-%m-%d')
        base_url = f"https://api.balldontlie.io/v1/games?start_date={date}&per_page=10"
        headers = {"Authorization": apikey}
        response = requests.get(base_url, headers=headers)
        self.assertEqual(response.status_code,200)


# Create your tests here.
