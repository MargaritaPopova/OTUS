import redis


def main():
    r = redis.Redis().client()
    r.set("id", 2)
    print(r.get("id"))


if __name__ == '__main__':
    main()
