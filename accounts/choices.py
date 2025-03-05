from django.db import models


class BranchChoices(models.TextChoices):
    ASMB_SOFIA = 'АСМБ София', 'АСМБ София'
    ASMB_SU = 'АСМБ СУ', 'АСМБ СУ'
    ASMB_VARNA = 'АСМБ Варна', 'АСМБ Варна'
    ASM_PLOVDIV = 'АСМ Пловдив', 'АСМ Пловдив'
    ASMB_BURGAS = 'АСМБ Бургас', 'АСМБ Бургас'
    ASMB_PLEVEN = 'АСМБ Плевен', 'АСМБ Плевен'
    ASMB_STARA_ZAGORA = 'АСМБ Стара Загора', 'АСМБ Стара Загора'