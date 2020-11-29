import re
import allure

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def email_validation(email):
    return bool(EMAIL_REGEX.match(email))


def check_email(posts_by_user, func):
    with allure.step(f"Get comments of each post"):
        for post in posts_by_user:
            post_id = post["id"]
            comments = func(post_id).json()

            if len(comments) == 0:
                with allure.step("This post hasn't had any comments yet"):
                    continue

            with allure.step(f"Check email in each comment of this post"):
                for comment in comments:
                    email = comment["email"]
                    with allure.step(f"Email in comment with id={comment['id']} is ok"):
                        with allure.step("Email exists"):
                            assert email is not None, "Comment should include email, but got None"
                        with allure.step("Email is a string"):
                            assert isinstance(email, str), f"Email should be a string, but got {email}"
                        with allure.step("Email is valid"):
                            assert email_validation(email), f"Email {email} is not valid"


def check_user_id(user_id, username):
    with allure.step(f"Check id of {username}"):
        with allure.step("Id exists"):
            assert user_id is not None, "User should include id, but got None"
        with allure.step("Id is integer"):
            assert isinstance(user_id, int), f"Id should be integer, but got {user_id}"


def check_user_name(data_user_name):
    with allure.step("Check username"):
        with allure.step("Username exists"):
            assert data_user_name is not None, "User should include username, but got None"
        with allure.step("Username is a string"):
            assert isinstance(data_user_name, str), f"Username should be a string, but got {data_user_name}"


def check_user_id_in_post(post_id, user_id_in_post, user_id, post):
    with allure.step(f"Check userId in the post with id={post_id}"):
        with allure.step("UserId exists in the post"):
            assert user_id_in_post is not None, "Post should include id, but got None"
        with allure.step("UserId is integer"):
            assert isinstance(user_id_in_post, int), f"UserId should be integer, but got {user_id}"
    with allure.step(f"Post with id={post_id} contains correct userId"):
        assert user_id_in_post == user_id, f"UserId should be {user_id}, but got {post['userId']}"


def check_response(res, data):
    with allure.step("Status code of response is 200"):
        assert res.status_code == 200, f"Status code should be 200, but got {res.status_code}"
    with allure.step("Content of response is not empty"):
        assert res.content is not None, f"Body should contain something, but got {res.content}"
    with allure.step("Type of result is a list"):
        assert isinstance(data, list), "Type of result should be a list"
