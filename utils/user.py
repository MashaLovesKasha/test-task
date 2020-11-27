from requests import Response


def get_user_by_name(client, username):
    res: Response = client.get_user_by_name(username)
    assert res.status_code == 200, f"Status should be 200, but got {res.status_code}"
    assert res.content is not None, f"Body should contain something, but got {res.content}"
    user_data = res.json()[0]
    return user_data


def get_posts_by_user_id(client, user_id):
    posts = client.get_posts_by_user_id(user_id)
    assert posts.status_code == 200, f"Status should be 200, but got {posts.status_code}"
    assert posts.content is not None, f"Body should contain something, but got {posts.content}"
    posts_by_user = posts.json()
    return posts_by_user
