
class JzrqyhtAPi():
    def __init__(self, s, host="http://114.115.153.29:9000"):
        self.host = host
        self.s = s

    def get_companyusercenter(self):
        '''查询企业中心的用户信息'''
        url = self.host + "/api/CompanyUserCenter/GetCompanyUserCenter"
        r = self.s.get(url)
        print(r.text)
        return r.json()

    def get_enterpriseinfodetail(self, enterpriseId):
        '''查询企业用户详情'''
        url = self.host + "/api/EnterpriseInfo/GetEnterpriseInfoDetail"
        param = {
            "enterpriseId": enterpriseId
        }
        r = self.s.get(url, params=param)
        print(r.text)
        return r.json()

    def get_industryinfosinglealllist(self):
        url = self.host + "/api/IndustryInfo/GetIndustryInfoSingleALLList"
        r = self.s.get(url)
        print(r.text)
        return r.json()