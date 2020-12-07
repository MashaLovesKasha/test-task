from requests import Response
import allure
from utils.validators import check_response
from utils.client import ApiClient


class UserClient(ApiClient):
    def __init__(self, host):
        super(UserClient, self).__init__(host)

    @allure.step('Get user by specific name')
    def get_user_by_name(self, name: str):
        params = {"username": name}
        res = self.get("/users", params=params)
        user_data = res.json()
        allure.attach(res.content, "User's information", attachment_type=allure.attachment_type.JSON)
        with allure.step("Check response"):
            check_response(res, user_data)
            with allure.step("User is found and it is unique"):
                assert len(user_data) == 1, f"User should exist and be uniq, but got {len(user_data)} user(s)"
        return user_data[0]

    @allure.step('Get posts by userId')
    def get_posts_by_user_id(self, uid: int):
        params = {"userId": uid}
        posts = self.get("/posts", params=params)
        posts_by_user = posts.json()
        with allure.step("Check response"):
            check_response(posts, posts_by_user)
            with allure.step("At least one post was found"):
                assert len(posts_by_user) >= 1, "This user hasn't had any posts yet"
        return posts_by_user

    @allure.step('Get comments of post')
    def get_comments_by_post_id(self, post_id: int):
        return self.get(f"/posts/{post_id}/comments")

    @allure.step('Get comments of post')
    def get_comments_by_post_id_query_param(self, post_id: int):
        params = {"postId": post_id}
        return self.get("/comments", params=params)


#
# def get_user_by_name(client, username):
#     res: Response = client.get_user_by_name(username)
#     user_data = res.json()
#     allure.attach(res.content, "User's information", attachment_type=allure.attachment_type.JSON)
#     with allure.step("Check response"):
#         check_response(res, user_data)
#         with allure.step("User is found and it is unique"):
#             assert len(user_data) == 1, f"User should exist and be uniq, but got {len(user_data)} user(s)"
#     return user_data[0]


# def get_posts_by_user_id(client, user_id):
#     posts: Response = client.get_posts_by_user_id(user_id)
#     posts_by_user = posts.json()
#     with allure.step("Check response"):
#         check_response(posts, posts_by_user)
#         with allure.step("At least one post was found"):
#             assert len(posts_by_user) >= 1, "This user hasn't had any posts yet"
#     return posts_by_user
