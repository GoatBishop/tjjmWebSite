#from django.db import models
#from django.utils import timezone
#from django.core import validators
##from schoolManage.models import College,Instructor
## Create your models here.
#
#
#class Member(models.Model):
#    member_name = models.CharField('成员姓名', max_length = 30)
#    student_number = models.CharField('学号', max_length = 30)
#    telephone = models.CharField("手机号", max_length = 11,
#                                          validators=[validators.RegexValidator("1[3456789]\d{9}",message='请输入正确格式的手机号码！')],
#                                          unique=True)
#    school = models.ForeignKey("College", on_delete = models.CASCADE)
#    id_number = models.CharField("身份证号", max_length = 30, default = "")
#    grade = models.CharField('年级', max_length = 30)
#    major = models.CharField('专业', max_length = 30)
#    class_in_school = models.CharField('班级', max_length = 30)
#    is_captain = models.CharField('是否为队长', max_length = 2, default = "否")
#    add_time = models.DateTimeField(default = timezone.now())
#    
#    def __str__(self):
#        return "成员:" + self.member_name
#    
#    
#class Team(models.Model):
#    group = models.CharField('组别', max_length = 30, default = "本科组")
#    work_group = models.CharField('参赛项目类别', max_length = 30, default = "大数据应用类")
##    captain = models.CharField('团队长姓名', max_length = 30)
#    telephone = models.OneToOneField('Member', on_delete = models.CASCADE,
#                                             related_name = "team")
#    
#    password = models.CharField('密码', max_length = 16,
#                                validators=[validators.RegexValidator(r"\w{6,16}", message = '请输入正确格式的密码！')])
#    
#    first_instru = models.ManyToManyField("Instructor", related_name = "team_first", null = True)
#    second_instru = models.ManyToManyField("Instructor", related_name = "team_second", null = True)
#    add_time = models.DateTimeField(default = timezone.now())
#    #修改时间
#    status = models.CharField('状态', max_length = 20, default = "待审核")
#    
#    def __str__(self):
#        return  "团队组别:"  + self.group
#
