from django.contrib.auth.models import AbstractUser
from django.db import models

from composteira.models import models
from classificacao.models import models
from notificacaoMeta.models import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
