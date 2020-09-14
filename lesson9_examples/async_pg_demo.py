import asyncio
import asyncpg


async def main():
    conn = await asyncpg.connect(
        "postgresql://postgres:password@localhost/homework"
        # user='user',
        # password='password',
        # database='database',
        # host='127.0.0.1'
    )
    # await conn.execute(
    #     "INSERT INTO users.users(id, name, email) VALUES($1, $2, $3)",
    #     5,
    #     "Magna",
    #     "magna@email.com",
    # )

    rows = await conn.fetch("SELECT name, email FROM users;")
    print(rows)
    for r in rows:
        print(r["name"], r["email"])
        # print(r[0])

    sam = await conn.fetchrow("SELECT * FROM users WHERE name = $1", "sam")
    print(sam)

    # values = await conn.fetch()
    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
