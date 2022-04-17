from .models import User


def resolve_users(self, info, page=1):
    page = max(page, 1)
    page_size = 5
    skip = page_size * (page - 1)
    taking = page_size * page
    user_list = User.objects.all()[skip:taking]
    print(user_list)

    return user_list


def resolve_user(self, info, id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        return None
