from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=160)
    slug = models.SlugField(verbose_name = _("slug"),editable=False,unique=True,null=False)
    cover  = models.ImageField(verbose_name=_("Product Cover Image"), upload_to="cover/",blank=False,null=False,default="cover.png")

    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Product,self).save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Product_detail", kwargs={"slug": self.slug})
