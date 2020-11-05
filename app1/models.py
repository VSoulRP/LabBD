# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CountryWiseLatest(models.Model):
    country_region = models.CharField(primary_key=True, max_length=100)
    confirmed = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    new_cases = models.IntegerField(blank=True, null=True)
    new_deaths = models.IntegerField(blank=True, null=True)
    new_recovered = models.IntegerField(blank=True, null=True)
    deaths_per_100_cases = models.FloatField(db_column='deaths_per_100_Cases', blank=True, null=True)  # Field name made lowercase.
    recovered_per_100_cases = models.FloatField(db_column='recovered_per_100_Cases', blank=True, null=True)  # Field name made lowercase.
    deaths_per_100_recovered = models.FloatField(db_column='deaths_per_100_Recovered', blank=True, null=True)  # Field name made lowercase.
    confirmed_last_week = models.IntegerField(blank=True, null=True)
    one_week_change = models.IntegerField(blank=True, null=True)
    one_week_perc_increase = models.FloatField(blank=True, null=True)
    who_region = models.CharField(db_column='WHO_Region', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country_wise_latest'


class Covid19CleanComplete(models.Model):
    province_state = models.CharField(db_column='Province_State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country_region = models.CharField(db_column='Country_Region', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(db_column='Long', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    confirmed = models.IntegerField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    deaths = models.BigIntegerField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.
    recovered = models.IntegerField(db_column='Recovered', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    who_region = models.CharField(db_column='WHO Region', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'covid_19_clean_complete'


class DayWise(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    confirmed = models.IntegerField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    deaths = models.IntegerField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.
    recovered = models.IntegerField(db_column='Recovered', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    new_cases = models.IntegerField(db_column='New cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_deaths = models.IntegerField(db_column='New deaths', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_recovered = models.IntegerField(db_column='New recovered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deaths_per_100_cases = models.FloatField(db_column='Deaths per 100 Cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recovered_per_100_cases = models.FloatField(db_column='Recovered per 100 Cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deaths_per_100_recovered = models.FloatField(db_column='Deaths per 100 Recovered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    num_of_countries = models.IntegerField(db_column='Num of countries', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'day_wise'



class FullGrouped(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    country_region = models.CharField(db_column='Country_Region', max_length=100)  # Field name made lowercase.
    confirmed = models.IntegerField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    deaths = models.IntegerField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.
    recovered = models.IntegerField(db_column='Recovered', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    new_cases = models.IntegerField(db_column='New cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_deaths = models.IntegerField(db_column='New deaths', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_recovered = models.IntegerField(db_column='New recovered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    who_region = models.TextField(db_column='WHO Region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'full_grouped'
        unique_together = (('date', 'country_region'),)


class WorldometerData(models.Model):
    country_region = models.CharField(db_column='Country_Region', max_length=100, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    totalcases = models.IntegerField(db_column='TotalCases', blank=True, null=True)  # Field name made lowercase.
    newcases = models.IntegerField(db_column='NewCases', blank=True, null=True)  # Field name made lowercase.
    totaldeaths = models.IntegerField(db_column='TotalDeaths', blank=True, null=True)  # Field name made lowercase.
    newdeaths = models.IntegerField(db_column='NewDeaths', blank=True, null=True)  # Field name made lowercase.
    totalrecovered = models.IntegerField(db_column='TotalRecovered', blank=True, null=True)  # Field name made lowercase.
    newrecovered = models.IntegerField(db_column='NewRecovered', blank=True, null=True)  # Field name made lowercase.
    activecases = models.IntegerField(db_column='ActiveCases', blank=True, null=True)  # Field name made lowercase.
    serious_critical = models.IntegerField(db_column='Serious,Critical', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tot_cases_per1m_pop = models.IntegerField(db_column='Tot Cases per1M pop', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deaths_per_1m_pop = models.IntegerField(db_column='Deaths per 1M pop', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    totaltests = models.IntegerField(db_column='TotalTests', blank=True, null=True)  # Field name made lowercase.
    tests_per_1m_pop = models.IntegerField(db_column='Tests per 1M pop', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    who_region = models.CharField(db_column='WHO Region', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'worldometer_data'
