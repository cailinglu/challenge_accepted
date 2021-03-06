# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import ChallengeSession
from ..ninjas.models import Ninja
from ..session_bouts.models import SessionBout

class ChallengeSessionModelTest(TestCase):
    def test_that_challenge_session_can_be_created_and_saved(self):
        challenge_session = ChallengeSession.objects.create()
        self.assertTrue(challenge_session)

    def test_that_challenge_session_calculates_correct_number_of_winners_losers_and_participants(self):
        # Create some ninjas
        ninja1 = Ninja.objects.create_user('bob', 'bobby@ross.com', 'password')
        ninja2 = Ninja.objects.create_user('jorge', 'jorge@ross.com', 'password')
        ninja3 = Ninja.objects.create_user('alice', 'alice@ross.com', 'password')
        ninja4 = Ninja.objects.create_user('pam', 'pam@ross.com', 'password')
        # Create some bouts (2)
        bout1 = SessionBout.objects.create()
        bout2 = SessionBout.objects.create()
        # Add ninjas to bouts
        bout1.participants.add(ninja1, ninja2)
        bout1.winner = ninja1
        bout1.loser = ninja2
        bout2.participants.add(ninja3, ninja4)
        bout2.winner = ninja4
        bout2.loser = ninja3
        # Create challenge_session (1)
        challenge_session = ChallengeSession.objects.create(number=1)
        # Attach challenge_session to bouts
        bout1.challenge_session = challenge_session
        bout2.challenge_session = challenge_session
        bout1.save()
        bout2.save()
        # Saving winners, losers, and participants
        winners = challenge_session.winners
        losers = challenge_session.losers
        participants = challenge_session.participants
        # Assertions
        self.assertEqual(len(winners), 2)
        self.assertEqual(len(losers), 2)
        self.assertEqual(len(participants), 4)
        
        
        
