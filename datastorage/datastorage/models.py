
from django.db import models


class MultiValuedData(models.Model):
    user_id = models.IntegerField(null=False)
    data_source = models.CharField(max_length=30, null=False)
    data_type = models.CharField(max_length=30, null=False)
    data = models.CharField(max_length=100, null=False)

    class Meta:
        unique_together = ('user_id', 'data_source', 'data_type',)

    def __str__(self) -> str:
        return str(self.user_id) + " " + self.data_source + " " + self.data_type
