from app.services.userService import UserService
from app.config import get_db

def main():
    db = get_db()
    user_service = UserService(db)




if __name__ == '__main__':
    main()