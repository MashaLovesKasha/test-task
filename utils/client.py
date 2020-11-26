import requests


class ApiClient:
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def get_user_by_name(self, name: str):
        params = {"username": name}
        return self._s.get(self.host + "/users", params=params)

    def get_posts_by_user_id(self, uid: int):
        params = {"userId": uid}
        return self._s.get(self.host + "/posts", params=params)

    def get_comments_by_post_id(self, post_id: int):
        return self._s.get(self.host + f"/posts/{post_id}/comments")

    def get_comments_by_post_id_v2(self, post_id: int):
        params = {"postId": post_id}
        return self._s.get(self.host + "/comments", params=params)
