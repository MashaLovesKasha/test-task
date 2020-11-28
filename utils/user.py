from requests import Response
import allure


def get_user_by_name(client, username):
    res: Response = client.get_user_by_name(username)
    with allure.step("Check the response"):
        with allure.step("Check the status code of the response"):
            assert res.status_code == 200, f"Status code should be 200, but got {res.status_code}"
        with allure.step("Check the body of the response"):
            assert res.content is not None, f"Body should contain something, but got {res.content}"
        user_data = res.json()[0]
        return user_data


def get_posts_by_user_id(client, user_id):
    posts: Response = client.get_posts_by_user_id(user_id)
    with allure.step("Check the response"):
        with allure.step("Check the status code of the response"):
            assert posts.status_code == 200, f"Status code should be 200, but got {posts.status_code}"
        with allure.step("Check the body of the response"):
            assert posts.content is not None, f"Body should contain something, but got {posts.content}"
        posts_by_user = posts.json()
        return posts_by_user
