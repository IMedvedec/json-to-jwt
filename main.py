def main():
    import sys
    import json
    import jwt

    if len(sys.argv) != 3:
        print(f"Invalid argument number: provide input json and secret key filenames!")
        sys.exit()

    try:
        with open(sys.argv[1], "r") as input, open(sys.argv[2], "r") as key:
            claims = json.loads(input.read())
            secret = key.read()
            token = jwt.encode(claims, secret, algorithm="HS256")
            print(token)
    except Exception as err:
        print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()
