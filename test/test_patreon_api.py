from unittest import TestCase

from core.patreon_api import PatreonApi
from core.patreon_response import Status, Tier
from test.patreon_api_test_data import *


class Test(TestCase):

    def test_create_patreon_list(self):
        active_patreon = PatreonStructureStub(active_user_pledge, active_user_patron, active_user_reward)
        cancel_patreon = PatreonStructureStub(cancel_user_pledge, cancel_user_patron, cancel_user_reward)
        pause_patreon = PatreonStructureStub(pause_user_pledge, pause_user_patron, pause_user_reward)
        all_pledges = [active_patreon, cancel_patreon, pause_patreon]

        patreon_list = PatreonApi.create_patreon_list(all_pledges, None)

        self.assertEqual(patreon_list[0].status, Status.ACTIVE)
        self.assertEqual(patreon_list[0].username, 'activeUser')
        self.assertEqual(patreon_list[0].mail, 'activeUser@dummy.com')
        self.assertEqual(patreon_list[0].tier, Tier.TIER_2)
        self.assertEqual(patreon_list[1].status, Status.INACTIVE)
        self.assertEqual(patreon_list[1].username, 'cancelUser')
        self.assertEqual(patreon_list[1].mail, 'cancelUser@dummy.com')
        self.assertEqual(patreon_list[2].tier, None)
        self.assertEqual(patreon_list[2].status, Status.INACTIVE)
        self.assertEqual(patreon_list[2].username, 'pauseUser')
        self.assertEqual(patreon_list[2].mail, 'pauseUser@dummy.com')
        self.assertEqual(patreon_list[2].tier, None)