from project.library import Library
from project.user import User


class Registration:

    @staticmethod
    def add_user(user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
            library.rented_books[user.username] = {}
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            library.rented_books.pop(user.username)
        else:
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        user_to_change = None
        username_error = False

        for user in library.user_records:
            if user_id == user.user_id and new_username != user.username:
                user_to_change = user
                break
            if user_id == user.user_id and new_username == user.username:
                username_error = True
                break

        if user_to_change:
            library.rented_books[new_username] = library.rented_books.pop(user_to_change.username)
            user_to_change.username = new_username
            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        if username_error:
            return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
