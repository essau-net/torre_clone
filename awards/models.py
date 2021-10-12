from django.db.models import BigAutoField, CharField, DateField, IntegerField, Model

# Create your models here.
class Awards(Model):
    id = BigAutoField(primary_key=True)
    award_name = CharField(max_length=255)
    is_current = IntegerField()
    started_at = DateField()
    finished_at = DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'awards'