import django_setup
from task.models import Role, User

john_doe = User.objects.filter(id=3).first()
print(john_doe.role)