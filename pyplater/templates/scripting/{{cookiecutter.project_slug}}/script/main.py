from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print(os.getenv("YOUR_SECRET"))


if __name__ == "__main__":
    main()
