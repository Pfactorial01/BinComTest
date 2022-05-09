# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        
        db_table = 'agentname'


class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'announced_lga_results'


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.ForeignKey('PollingUnit', on_delete=models.SET_NULL, null=True, blank=True)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'announced_pu_results'
    def __str__(self):
        return self.polling_unit_uniqueid.polling_unit_name

class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'announced_state_results'


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'announced_ward_results'


class Lga(models.Model):
    #uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'lga'
    def __str__(self):
        return self.lga_name

class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.ForeignKey(Lga, on_delete=models.SET_NULL, null=True, blank=True)
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'ward'
    def __str__(self):
        return self.ward_name




class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = ChainedForeignKey(
        'PollingUnit',
        chained_field="uniquewardid",
        chained_model_field="uniquewardid",
        show_all=False,
        auto_choose=True,
        sort=True)
    ward_id = models.IntegerField()
    lga_id = models.ForeignKey('Lga', on_delete=models.SET_NULL, null=True, blank=True)
    uniquewardid = ChainedForeignKey(
        Ward,
        chained_field="lga_id",
        chained_model_field="lga_id",
        show_all=False,
        auto_choose=True,
        sort=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'polling_unit'
    def __str__(self):
        return self.polling_unit_name


class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'states'

class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    class Meta:
        
        db_table = 'party'

class New_Polling_Unit(models.Model):
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    lga_name = models.ForeignKey('Lga', on_delete=models.SET_NULL, null=True, blank=True)
    ward_name = ChainedForeignKey(
        Ward,
        chained_field="lga_name",
        chained_model_field="lga_id",
        show_all=False,
        auto_choose=True,
        sort=True)
    PDP = models.IntegerField()
    DPP = models.IntegerField()
    ACN = models.IntegerField()
    PPA = models.IntegerField()
    CDC = models.IntegerField()
    JP = models.IntegerField()
    ANPP = models.IntegerField()
    LABOUR = models.IntegerField()
    CPP = models.IntegerField()


