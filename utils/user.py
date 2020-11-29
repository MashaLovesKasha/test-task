from requests import Response
import allure
from utils.validators import check_response


def get_user_by_name(client, username):
    res: Response = client.get_user_by_name(username)
    user_data = res.json()
    allure.attach(res.content, "User's information", attachment_type=allure.attachment_type.JSON)
    with allure.step("Check response"):
        check_response(res, user_data)
        with allure.step("User is found and it is unique"):
            assert len(user_data) == 1, f"User should exist and be uniq, but got {len(user_data)} user(s)"
    return user_data[0]


def get_posts_by_user_id(client, user_id):
    posts: Response = client.get_posts_by_user_id(user_id)
    posts_by_user = posts.json()
    with allure.step("Check response"):
        check_response(posts, posts_by_user)
        with allure.step("At least one post was found"):
            assert len(posts_by_user) >= 1, "This user hasn't had any posts yet"
    return posts_by_user
