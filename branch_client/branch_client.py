# -*- encoding: utf-8 -*-

import requests


class BranchClient(object):
    """
    Python Branch.io client to communicate with BranchMetrics service
    """

    def __init__(self, app_id):
        """
        Client constructor
        :param app_id: Your branch.io application id
        :return:
        """
        self.app_id = app_id
        self.branch_api_url = 'https://api.branch.io'

    def create_branch_link(self, data={}, alias=None, link_type=None, duration=None, identity=None, campaign=None,
                           feature=None, channel=None, stage=None):
        """
        Creates a branch.io link
        :param data: optional data parameter to embed into the link
        :param alias: optional
        :param link_type: optional
        :param duration: optional
        :param identity: optional
        :param campaign: optional
        :param feature: optional
        :param channel: optional
        :param stage: optional
        :return: requests object
        """
        url_endpoint = '{0}/v1/url'.format(self.branch_api_url)
        payload = {
            'app_id': str(self.app_id),
            'data': data
        }
        if link_type:
            payload.update({'type': link_type})
        if alias:
            payload.update({'alias': alias})
        if duration:
            payload.update({'duration': duration})
        if identity:
            payload.update({'identity': str(identity)})
        if campaign:
            payload.update({'campaign': campaign})
        if feature:
            payload.update({'feature': feature})
        if channel:
            payload.update({'channel': channel})
        if stage:
            payload.update({'stage': stage})
        return requests.post(url_endpoint, json=payload)
