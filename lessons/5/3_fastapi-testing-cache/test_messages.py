from sqlalchemy import insert, select
from messages import models
from conftest import client, async_session_maker


async def test_get_messages():
    response = client.get("/messages", params={"page": 2})
    print("\n\n\n")
    print(response.status_code)
    print(response.json())
    print("\n\n\n")
    assert response.status_code == 200


async def test_get_message():
    response = client.get("/messages/35")
    print("\n\n\n")
    print(response.status_code)
    print(response.json())
    print("\n\n\n")
    assert response.status_code == 200


async def test_create_message():
    chk = "Проверка текста"

    async with async_session_maker() as session:
        print("\n\n\n")
        # before
        old_result = client.get("/messages").json()
        # query = select(models.Message)
        # res = await session.execute(query)
        print(old_result)

        # insert
        query = insert(models.Message).values(text=chk)
        await session.execute(query)
        await session.commit()

        # after
        new_result = client.get("/messages").json()
        print(new_result)
        print("\n\n\n")
        assert len(old_result) + 1 == len(new_result), "Сообщение не добавилось"


def test_register():
    print("\n\n\n")
    # before
    old_result = client.get("/messages").json()
    _id = old_result[-1]["id"]
    print(_id)
    # update
    response = client.put(
        f"/messages/{_id}",
        # json={
        #     "email": "string",
        #     "password": "string",
        #     "is_active": True,
        #     "is_superuser": False,
        #     "is_verified": False,
        #     "username": "string",
        #     "role_id": 1,
        # },
    )
    print(response.json())
    print("\n\n\n")
    assert response.status_code == 200, "Не обновилось"
