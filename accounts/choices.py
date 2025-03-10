from django.db import models


class BranchChoices(models.TextChoices):
    ASMB_SOFIA = 'АСМБ София', 'АСМБ София'
    ASMB_SU = 'АСМБ СУ', 'АСМБ СУ'
    ASMB_VARNA = 'АСМБ Варна', 'АСМБ Варна'
    ASM_PLOVDIV = 'АСМ Пловдив', 'АСМ Пловдив'
    ASMB_BURGAS = 'АСМБ Бургас', 'АСМБ Бургас'
    ASMB_PLEVEN = 'АСМБ Плевен', 'АСМБ Плевен'
    ASMB_STARA_ZAGORA = 'АСМБ Стара Загора', 'АСМБ Стара Загора'


class RoleChoices(models.TextChoices):
    PRESIDENT = 'National Member Organization President', 'National Member Organization President'
    VISE_PRESIDENT_EXTERNAL_AFFAIRS = 'Vise President External Affairs', 'Vise President External Affairs'
    VISE_PRESIDENT_INTERNAL_AFFAIRS = 'Vise President External Internal', 'Vise President External Internal'
    PR_C = 'PRnC', 'PRnC'
    NEO_IN = 'Neo-In', 'Neo-In'
    NEO_OUT = 'Neo-Out', 'Neo-Out'
    NORE_IN = 'Nore-In', 'Nore-In'
    NORE_OUT = 'Nore-Out', 'Nore-Out'
    NOME = 'Nome', 'Nome'
    NPO = 'NPO', 'NPO'
    NORA = 'Nora', 'Nora'
    NORP = 'NorP', 'NorP'
    MEMBER = 'Member', 'Member'