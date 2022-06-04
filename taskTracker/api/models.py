from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

USER_ROLE = [
    ('TL','Team leader'),
    ('TM','Team member'),
    ('US','User')
]

class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(_('email address'), unique = True)
  user_role = models.CharField(_('role of user'), max_length = 2, choices = USER_ROLE, default = 'US')

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name','user_role']
  def __str__(self):
      return "{}".format(self.email)

class Team(models.Model):
    name = models.CharField(_("name of team"), max_length = 50)
    team_leader = models.ForeignKey(User, related_name="tl", on_delete = models.PROTECT)
    team_member = models.ManyToManyField(User, related_name="tm")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}".format(self.name)

TASK_STATUS = (
    ("Asgn.","Assigned"),
    ("Prgs.","In progress"),
    ("Unrv.","Under review"),
    ("Done","Done")
    )


class Task(models.Model):
    name = models.CharField(_('task name'), max_length=50)
    team = models.ForeignKey(Team, on_delete = models.PROTECT)
    status = models.CharField(_("task status"), max_length = 50, choices=TASK_STATUS)
    started_at = models.DateTimeField(_("when this project started"), null=True, blank=True)
    completed_at = models.DateTimeField(_("when it was completed"), null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}".format(self.name)