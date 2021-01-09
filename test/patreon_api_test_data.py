cancel_user_pledge = {
    'attributes': {
        'declined_since': '2020-07-01T03:54:22.000+00:00',
        'is_paused': False,
        'total_historical_amount_cents': 0
    },
    'id': '44598513',
    'relationships': {
        'address': {
            'data': None
        },
        'patron': {
            'data': {
                'type': 'user'
            },
            'links': {
                'related': 'https://www.patreon.com/api/user/38054769'
            }
        },
        'reward': {
            'data': {
                'id': '5129597',
                'type': 'reward'
            },
            'links': {
                'related': 'https://www.patreon.com/api/rewards/5129597'
            }
        }
    },
    'type': 'pledge',

}
cancel_user_reward = {
    'attributes': {
        'amount': 300,
        'amount_cents': 300,
        'created_at': '2020-05-10T16:02:12.532+00:00',
        'currency': 'USD',
        'description': 'Tier 2',
        'edited_at': '2020-06-24T13:11:32.487+00:00',
        'patron_amount_cents': 300,
        'patron_count': 94,
        'patron_currency': 'USD',
        'post_count': 38,
        'published': True,
        'published_at': '2020-06-24T13:11:32.475+00:00',
        'title': 'Adelanto de Capítulo',
    },
    'relationships': {
        'campaign': {
            'data': {
                'id': '1874794',
                'type': 'campaign'
            },
            'links': {
                'related': 'https://www.patreon.com/api/campaigns/1874794'
            }
        }
    },
    'type': 'reward'
}
cancel_user_patron = {
    'attributes': {
        'email': 'cancelUser@dummy.com',
        'first_name': 'Cancel',
        'full_name': 'Cancel Dummy',
        'gender': 0,
        'patron_currency': None,
    },
    'id': '38054769',
    'relationships': {
        'campaign': {
            'data': None
        }
    },
    'type': 'user'
}

active_user_pledge = {
    'attributes': {
        'declined_since': None,
        'is_paused': False,
        'total_historical_amount_cents': 0
    },
    'id': '44598514',
    'relationships': {
        'address': {
            'data': None
        },
        'patron': {
            'data': {
                'type': 'user'
            },
            'links': {
                'related': 'https://www.patreon.com/api/user/38054769'
            }
        },
        'reward': {
            'data': {
                'id': '5129597',
                'type': 'reward'
            },
            'links': {
                'related': 'https://www.patreon.com/api/rewards/5129597'
            }
        }
    },
    'type': 'pledge',

}
active_user_reward = {
    'attributes': {
        'amount': 300,
        'amount_cents': 300,
        'created_at': '2020-05-10T16:02:12.532+00:00',
        'currency': 'USD',
        'description': 'Tier 2',
        'edited_at': '2020-06-24T13:11:32.487+00:00',
        'patron_amount_cents': 300,
        'patron_count': 94,
        'patron_currency': 'USD',
        'post_count': 38,
        'published': True,
        'published_at': '2020-06-24T13:11:32.475+00:00',
        'title': 'Adelanto de Capítulo',
    },
    'relationships': {
        'campaign': {
            'data': {
                'id': '1874794',
                'type': 'campaign'
            },
            'links': {
                'related': 'https://www.patreon.com/api/campaigns/1874794'
            }
        }
    },
    'type': 'reward'
}
active_user_patron = {
    'attributes': {
        'email': 'activeUser@dummy.com',
        'first_name': 'Active',
        'full_name': 'Active Dummy',
        'gender': 0,
        'patron_currency': None,
    },
    'id': '38054769',
    'relationships': {
        'campaign': {
            'data': None
        }
    },
    'type': 'user'
}

pause_user_pledge = {
    'attributes': {
        'declined_since': None,
        'is_paused': True,
        'total_historical_amount_cents': 0
    },
    'id': '44598513',
    'relationships': {
        'address': {
            'data': None
        },
        'patron': {
            'data': {
                'type': 'user'
            },
            'links': {
                'related': 'https://www.patreon.com/api/user/38054769'
            }
        },
        'reward': {
            'data': {
                'id': '5129597',
                'type': 'reward'
            },
            'links': {
                'related': 'https://www.patreon.com/api/rewards/5129597'
            }
        }
    },
    'type': 'pledge',

}
pause_user_reward = {
    'attributes': {
        'amount': 300,
        'amount_cents': 300,
        'created_at': '2020-05-10T16:02:12.532+00:00',
        'currency': 'USD',
        'description': 'Tier 2',
        'edited_at': '2020-06-24T13:11:32.487+00:00',
        'patron_amount_cents': 300,
        'patron_count': 94,
        'patron_currency': 'USD',
        'post_count': 38,
        'published': True,
        'published_at': '2020-06-24T13:11:32.475+00:00',
        'title': 'Adelanto de Capítulo',
    },
    'relationships': {
        'campaign': {
            'data': {
                'id': '1874794',
                'type': 'campaign'
            },
            'links': {
                'related': 'https://www.patreon.com/api/campaigns/1874794'
            }
        }
    },
    'type': 'reward'
}
pause_user_patron = {
    'attributes': {
        'email': 'pauseUser@dummy.com',
        'first_name': 'Pause',
        'full_name': 'Pancel Dummy',
        'gender': 0,
        'patron_currency': None,
    },
    'id': '38054769',
    'relationships': {
        'campaign': {
            'data': None
        }
    },
    'type': 'user'
}

class PatreonAttributeGet:

    def __init__(self, structure):
        self.structure = structure

    def attribute(self, attribute):
        return self.structure['attributes'][attribute]


class PatreonStructureStub(PatreonAttributeGet):

    def __init__(self, pledge, patreon, reward):
        super().__init__(pledge)
        self.patreon = patreon
        self.reward = reward

    def relationship(self, relation):
        if relation == 'patron':
            return PatreonAttributeGet(self.patreon)
        elif relation == 'reward':
            return PatreonAttributeGet(self.reward)

        return None
