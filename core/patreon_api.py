import patreon
import os

from core.patreon_response import PatreonResponse, Status, Tier


class PatreonApi:

    def __init__(self):
        access_token = os.environ.get('ACCESS_TOKEN', None)
        self.api_client = patreon.API(access_token)
        campaign_response = self.api_client.fetch_campaign()
        self.campaign_id = campaign_response.data()[0].id()

    def get_patreons(self, list_of_user_names=None):
        all_pledges = []
        cursor = None

        while True:
            # TODO: Fetch by specific user emails or usernames
            pledges_response = self.api_client.fetch_page_of_pledges(
                self.campaign_id, 50, cursor=cursor,
                fields={
                    'pledge': ['total_historical_amount_cents', 'declined_since', 'is_paused',
                               'currently_entitled_tiers']})
            cursor = self.api_client.extract_cursor(pledges_response)
            all_pledges += pledges_response.data()
            print('Fetching page')
            if not cursor:
                break

        patreon_list = self.create_patreon_list(all_pledges, list_of_user_names)
        patreon_list_sorted = sorted(patreon_list,
                                     key=lambda patreon: [patreon.status == 'ACTIVE' or patreon.status == 'EVALUATE'],
                                     reverse=True)

        return patreon_list_sorted

    @staticmethod
    def get_patreon_list(all_pledges, list_of_user_names):
        raise NotImplementedError

    @staticmethod
    def get_default_patreon_list(all_pledges, list_of_user_names):
        patreon_list = []
        for pledge in all_pledges:
            # declined_since indicates the date of the most recent payment if it failed,
            # or `null` if the most recent payment succeeded.
            # A pledge with a non-null declined_since should be treated as invalid.
            # is_paused is when the patreon stop the payment for any reason
            is_declined_or_paused = pledge.attribute('declined_since') \
                                    or (pledge.attribute('is_paused') or pledge.attribute('is_paused') == 'true')
            reward_tier = 0

            relationship_reward_info = pledge.relationship_info('reward')
            if relationship_reward_info.json_data and relationship_reward_info.json_data['data']:
                relationship_reward = pledge.relationship('reward')
                if relationship_reward:
                    reward_tier = relationship_reward.attribute('amount_cents')

            relationship_patron = pledge.relationship('patron')
            mail = relationship_patron.attribute('email')
            username = mail.split('@')[0]

            if list_of_user_names is None or username in list_of_user_names:

                patreon_response = PatreonResponse(
                    patron_id=relationship_patron.id(),
                    username=username,
                    mail=mail)
                patreon_response.total_amount = pledge.attribute('total_historical_amount_cents') / 100

                if not is_declined_or_paused:
                    # TIER 1 is consider inactive
                    if reward_tier == 100:
                        patreon_response.status = Status.INACTIVE.value
                        patreon_response.tier = Tier.TIER_1
                        patreon_list.append(patreon_response)
                    if reward_tier == 300:
                        patreon_response.status = Status.ACTIVE.value
                        patreon_response.tier = Tier.TIER_2
                        patreon_list.append(patreon_response)
                    if reward_tier == 500:
                        patreon_response.status = Status.ACTIVE.value
                        patreon_response.tier = Tier.TIER_3
                        patreon_list.append(patreon_response)

                elif is_declined_or_paused and reward_tier >= 300:
                    patreon_list.append(patreon_response)
                else:
                    patreon_list.append(patreon_response)

        return patreon_list

    @staticmethod
    def create_patreon_list(all_pledges, list_of_user_names):
        try:
            PatreonApi.get_patreon_list(all_pledges, list_of_user_names)
        except NotImplementedError:
            return PatreonApi.get_default_patreon_list(all_pledges, list_of_user_names)
