import psycopg2


def main():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="homework",
        user="postgres",
        password="password",
    )

    print(conn)
    cur = conn.cursor()

    print(cur)

    res1 = cur.execute("INSERT INTO users (name, email) "
                       "VALUES ('sam', 'sam@email.com');")

    res = cur.execute("SELECT * FROM users;")
    print(res)

    #
    users = cur.fetchall()
    print(users)
    #
    print(conn.commit())

    conn.close()


if __name__ == '__main__':
    main()
