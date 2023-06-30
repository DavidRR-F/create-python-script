from dotenv import load_dotenv
import os

load_env()

def main():
    print(os.getenv("YOUR_SECRET"))

if __name__ == "__main__":
    main()
    