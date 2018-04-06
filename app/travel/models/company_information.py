# 회사+가이드 다 입력
from .product_base import ProductBase
from django.db import models


class CompanyInformation(ProductBase):
    name = models.CharField('회사명', max_length=50)
    info = models.TextField('회사설명')

    def __str__(self):
        return self.name
