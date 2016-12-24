from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class CurrencyManager(models.Manager):
    def add(self, postData):
        self.create(name = postData["name"], project_url = postData["project_url"], summary_url = postData["summary_url"])

    def edit(self, postData):
        pass

    def destroy(self, postData):
        pass

class ACManager(models.Manager):
    def add(self, postData):
        self.create(title = postData["title"], creator = postData["creator"], collaborator = postData["collaborator"], follower = postData["follower"], cred_rating = postData["cred_rating"])

    def edit(self, postData):
        pass

    def destroy(self, postData):
        pass

class DataDumpManager(models.Manager):
    def add(self, content):
        for item in content:
            self.create(data_id=item['id'], 
                name=item['name'],
                symbol=item['symbol'],
                rank=item['rank'],
                price_usd=item['price_usd'],
                price_btc=item['price_btc'],
                volume_usd=item['24h_volume_usd'],
                market_cap_usd=item['market_cap_usd'],
                available_supply=item['available_supply'],
                total_supply=item['total_supply'],
                percent_change_1h=item['percent_change_1h'],
                percent_change_24h=item['percent_change_24h'],
                percent_change_7d=item['percent_change_7d'],
                last_updated=datetime.datetime.fromtimestamp(int(item['last_updated'])).strftime('%Y-%m-%d %H:%M:%S')
                )                       

    def update(self, postData):
        pass

class Currency(models.Model):
    name = models.CharField(max_length = 255)
    project_url = models.TextField()
    summary_url = models.TextField()
    currencyManager = CurrencyManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AppCoin(models.Model):
    #These are our fields
    title = models.CharField(max_length = 255)
    creator = models.CharField(max_length = 255)
    collaborator = models.CharField(max_length = 255)
    follower = models.CharField(max_length = 255)
    cred_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ACManager = ACManager()

class DataDump(models.Model):
    data_id = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    symbol = models.CharField(max_length = 255)
    rank = models.IntegerField()
    price_usd = models.DecimalField(max_digits=19, decimal_places=10)
    price_btc = models.DecimalField(max_digits=19, decimal_places=10)
    volume_usd = models.FloatField()
    market_cap_usd = models.FloatField()
    available_supply = models.FloatField()
    total_supply = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_24h = models.FloatField()
    percent_change_7d = models.FloatField()
    last_updated = models.DateTimeField()
    DDManager = DataDumpManager()
