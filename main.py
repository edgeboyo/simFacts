import twitter

from config import CredentialsManager

if __name__ == "__main__":
    api = CredentialsManager().createValidAPI()
    api.PostUpdate(status="API Connected")
