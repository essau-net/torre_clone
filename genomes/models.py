from users.models import User
from django.db.models import Model, BigAutoField, ForeignKey, CharField, DO_NOTHING

# Create your models here.
class Genomes(Model):
    id = BigAutoField(primary_key=True)
    user = ForeignKey(User, DO_NOTHING)
    about = CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genomes'