def test_login_normal_account(client):
    response = client.get("/auth/login", data={})
    assert response.status_code == 405
