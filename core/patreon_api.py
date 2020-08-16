import patreon
import os

from core.patreon_response import PatreonResponse

access_token = os.environ.get('ACCESS_TOKEN', None)

api_client = patreon.API(access_token)

campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()


def get_patreons(list_of_user_names=None):
    all_pledges = []
    cursor = None

    while True:
        # TODO: Fetch by specific user emails or usernames
        pledges_response = api_client.fetch_page_of_pledges(
            campaign_id, 50, cursor=cursor,
            fields={
                'pledge': ['total_historical_amount_cents', 'declined_since', 'is_paused', 'currently_entitled_tiers']})
        cursor = api_client.extract_cursor(pledges_response)
        all_pledges += pledges_response.data()
        print('Fetching page')
        if not cursor:
            break

    patreon_list = []
    for pledge in all_pledges:
        declined = pledge.attribute('declined_since') or pledge.attribute('is_paused') == 'true'
        reward_tier = 0

        if pledge.relationships()['reward']['data']:
            reward_tier = pledge.relationship('reward').attribute('amount_cents')

        mail = pledge.relationship('patron').attribute('email')
        username = mail.split('@')[0]

        if username in list_of_user_names or list_of_user_names is None:
            if not declined and reward_tier >= 300:
                patreon_list.append(PatreonResponse(
                    username=username,
                    mail=mail,
                    status='ACTIVE',
                ))
            elif declined and reward_tier >= 300:
                patreon_list.append(PatreonResponse(
                    username=username,
                    mail=mail,
                    status='INACTIVE',
                ))
            elif reward_tier >= 300:
                patreon_list.append(PatreonResponse(
                    username=username,
                    mail=mail,
                    status='EVALUATE',
                ))

    patreon_list_sorted = sorted(patreon_list,
                                 key=lambda patreon: [patreon.status == 'ACTIVE' or patreon.status == 'EVALUATE'],
                                 reverse=True)

    return patreon_list_sorted
