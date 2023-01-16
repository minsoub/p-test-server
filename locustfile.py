from locust import HttpUser, task, between

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://k8s-systemsd-cmsappap-eca615f605-1526138129.ap-northeast-2.elb.amazonaws.com"

    @task(1)
    def get_index(self):
        self.client.get("/api/v1/cms/notices/bf?pageNo=1&pageSize=15", headers=default_headers)

    @task(2)
    def get_category_notices(self):
        self.client.get("/api/v1/cms/notices/bf?categoryId=3&pageNo=1&pageSize=15", headers=default_headers)

    @task(3)
    def get_search_notices(self):
        self.client.get("/api/v1/cms/notices/bf?searchText=모네로&pageNo=1&pageSize=15", headers=default_headers)

    @task(4)
    def get_notice(self):
        self.client.get("/api/v1/cms/notices/1643453", headers=default_headers)

