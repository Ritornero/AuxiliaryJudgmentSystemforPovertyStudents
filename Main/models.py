from django.db import models

# Create your models here.


class CS_Consumption(models.Model):
    sno = models.CharField(max_length=255)
    balance = models.IntegerField(blank=True, null=True)
    effectdate = models.DateField(blank=True, null=True)
    poscode = models.IntegerField(blank=True, null=True)
    toaccount = models.CharField(max_length=255, blank=True, null=True)
    tranamt = models.IntegerField(blank=True, null=True)
    exact_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_consumption'


class CS_All_Info(models.Model):
    user_sno = models.CharField(primary_key=True, max_length=30)
    bksinfo_edm_xb = models.CharField(db_column='BKSInfo_EDM_XB', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bksinfo_sfzh = models.CharField(db_column='BKSInfo_SFZH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bksinfo_edm_mz = models.CharField(db_column='BKSInfo_EDM_MZ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bksinfo_zymc = models.CharField(db_column='BKSInfo_ZYMC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bksinfo_xm = models.CharField(db_column='BKSInfo_XM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bksinfo_csrq = models.CharField(db_column='BKSInfo_CSRQ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bksinfo_edm_xy = models.CharField(db_column='BKSInfo_EDM_XY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bksinfo_jg = models.CharField(db_column='BKSInfo_JG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bksinfo_edm_zzmm = models.CharField(db_column='BKSInfo_EDM_ZZMM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    personinfo_expdate = models.CharField(db_column='PersonInfo_EXPDATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_all_info'

class AllMealsCopy2(models.Model):
    sno = models.IntegerField()
    year = models.CharField(max_length=255, blank=True, null=True)
    term = models.CharField(max_length=255, blank=True, null=True)
    breakfast_sum = models.FloatField(blank=True, null=True)
    breakfast_aver = models.FloatField(blank=True, null=True)
    breakfast_num = models.FloatField(blank=True, null=True)
    lunch_sum = models.FloatField(blank=True, null=True)
    lunch_aver = models.FloatField(blank=True, null=True)
    lunch_num = models.FloatField(blank=True, null=True)
    dinner_sum = models.FloatField(blank=True, null=True)
    dinner_aver = models.FloatField(blank=True, null=True)
    dinner_num = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All_Meals_copy2'



class Canteen(models.Model):
    canteen_name = models.TextField(blank=True, null=True)
    breakfast_amount = models.FloatField(blank=True, null=True)
    breakfast_count = models.BigIntegerField(blank=True, null=True)
    lunch_amount = models.FloatField(blank=True, null=True)
    lunch_count = models.BigIntegerField(blank=True, null=True)
    dinner_amount = models.FloatField(blank=True, null=True)
    dinner_count = models.BigIntegerField(blank=True, null=True)
    all_amount = models.FloatField(blank=True, null=True)
    all_count = models.BigIntegerField(blank=True, null=True)
    breakfast_rank = models.FloatField(blank=True, null=True)
    lunch_rank = models.FloatField(blank=True, null=True)
    dinner_rank = models.FloatField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Canteen'
