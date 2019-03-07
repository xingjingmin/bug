from django.db import models

# Create your models here.


class Student(models.Model):
    Name=(
        ('LK','Lu Kai'),
        ('LMD','Liu Meng Die'),
        ('LXH','Li Xiao Hui'),
        ('OY','Ou Yang Gao Fen'),
        ('XJM','Xing Jing Ming'),
    )
    username=models.CharField('测试人',max_length=100,choices=Name,default='LK')
    demandname=models.CharField('项目名称', max_length=256)
    pub_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

    class Meta:
        ordering=['pub_date']
        verbose_name='student'
        verbose_name_plural='student'


class State(models.Model):
    addbug = models.IntegerField('新增',default=0)
    repair = models.IntegerField('修复',default=0)
    activation = models.IntegerField('激活',default=0)
    ignore = models.IntegerField('忽略',default=0)
    surplus = models.IntegerField('剩余',default=0)
    deadly = models.IntegerField('致命',default=0)
    serious = models.IntegerField('严重',default=0)
    ordinary = models.IntegerField('普通',default=0)
    light = models.IntegerField('轻度',default=0)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)





