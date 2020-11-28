import requests
import allure


class ApiClient:
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def get(self, path="/", params=None, headers=None):
        url = f"{self.host}{path}"
        url_params = ""
        if params:
            url_params = '?' + '&'.join([f"{k}={v}" for k, v in params.items()])

        with allure.step(f'GET request to: {url}{url_params}'):
            return self._s.get(url=url, params=params, headers=headers)

    @allure.step('Get a user by the specific name')
    def get_user_by_name(self, name: str):
        params = {"username": name}
        return self.get("/users", params=params)

    @allure.step('Get posts by the userId')
    def get_posts_by_user_id(self, uid: int):
        params = {"userId": uid}
        return self.get("/posts", params=params)

    @allure.step('Get comments of the post')
    def get_comments_by_post_id(self, post_id: int):
        return self.get(f"/posts/{post_id}/comments")

    @allure.step('Get comments of the post')
    def get_comments_by_post_id_v2(self, post_id: int):
        params = {"postId": post_id}
        return self.get("/comments", params=params)
