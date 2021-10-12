#Local apps
from awards.models import Awards
from genomes.models import Genomes
from skills.models import Skills
#Django
from django.db.models import  BigAutoField, CharField, DO_NOTHING, ForeignKey, Model

# Create your models here.
class SkillsAwards(Model):
    id = BigAutoField(primary_key=True)
    skill = ForeignKey(Skills, DO_NOTHING)
    award = ForeignKey(Awards, DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'skills_awards'


class SkillsGenoms(Model):
    id = BigAutoField(primary_key=True)
    skill = ForeignKey(Skills, DO_NOTHING)
    genome = ForeignKey(Genomes, DO_NOTHING)
    skill_level = CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'skills_genoms'