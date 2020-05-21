class JzrggAPi():
    def __init__(self, s, host="http://114.115.153.29:9000"):
        self.host = host
        self.s = s

    def get_industryinfosinglealllist(self):
        '''获取所有行业的列表'''
        url = self.host + "/api/IndustryInfo/GetIndustryInfoSingleALLList"
        r = self.s.get(url)
        print(r.text)
        return r.json()

    def newgetbykey(self):
        '''获取key值下的数据'''
        url = self.host + "/api/BaseDataCust/NewGetByKey"
        body = {
            "key": "CompanyWeal,BusinessNature,CompanyScale"
        }
        r = self.s.post(url, json=body)
        print(r.text)
        return r.json()