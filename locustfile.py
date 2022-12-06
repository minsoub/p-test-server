from locust import HttpUser, task, between

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://k8s-systemsd-cmsappap-eca615f605-1526138129.ap-northeast-2.elb.amazonaws.com"

    @task(1)
    def get_index(self):
        self.client.get("/", headers=default_headers)

