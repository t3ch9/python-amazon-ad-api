from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils

class InitialBudgetRecommendation(Client):
    @sp_endpoint('/sp/campaigns/initialbudgetrecommendation', method='POST')
    def initial_campaign_budget_recommendation(self, **kwargs) -> ApiResponse:
        json_version = 'application/vnd.spinitialbudgetrecommendation.v3+json'

        headers = {
            "Content-Type": json_version
        }
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

