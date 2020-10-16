#from django.db import models
#from django.utils import timezone
#from django.core import validators
#from treamManage.models import Team
#
## Create your models here.
#
#class College(models.Model):
#    school = models.CharField('院校名称', max_length = 30,
#                            unique=True)
#    school_first_name = models.CharField('院校首字母', max_length = 30, null = True,
#                                         default = "")
#    contacts = models.CharField('院校联系人', max_length = 30)
#    school_class = models.CharField('院校类型', max_length = 30,  null = True,
#                                    default = "大学")
#    contacts_telephone = models.CharField("手机号", max_length = 11,
#                                          validators=[validators.RegexValidator("1[3456789]\d{9}",message='请输入正确格式的手机号码！')],
#                                          unique=True)
#    password = models.CharField('密码', max_length = 16,
#                                validators=[validators.RegexValidator(r"\w{6,16}", message = '请输入正确格式的密码！')])
#    audit_status = models.CharField('审核状态', max_length = 20,  null = True,
#                                    default = "待审核")
#    add_time = models.DateTimeField(default = timezone.now())
#    
#    def __str__(self):
#        return "院校:" + self.school
#
#class Instructor(models.Model):
#    instructor_name = models.CharField('指导教师姓名', max_length = 30)
#    instructor_telephone = models.CharField("手机号", max_length = 11,
#                                          validators=[validators.RegexValidator("1[3456789]\d{9}",message='请输入正确格式的手机号码！')],
#                                          unique=True)
#    password = models.CharField('密码', max_length = 16,
#                                validators=[validators.RegexValidator(r"\w{6,16}", message = '请输入正确格式的密码！')])
#    id_number = models.CharField("身份证号", max_length = 30, default = "")
#    add_time = models.DateTimeField(default = timezone.now())
#    school = models.ForeignKey("College", on_delete = models.CASCADE,
#                               related_name = "instructor")
#    
#    def __str__(self):
#        return "指导教师:" + self.instructor_name
#
#
#
##========表关联分界线======
#
#class Work(models.Model):
#    telephone = models.OneToOneField('Team', on_delete = models.CASCADE,
#                                             related_name = "work")
#    add_time = models.DateTimeField(default = timezone.now())
#    paper = models.FileField("作品", upload_to = "paper", 
#                             validators = [validators.FileExtensionValidator(['doc', 'docx','pdf'],
#                                                                           message = "文件格式必须为doc,docx,pdf格式")])
#    status = models.CharField('状态', max_length = 20, default="待审核")
#    
#    def __str__(self):
#        return  "作品名称:"  + self.work_name
#
#class Judge(models.Model):
#    judge_username = models.CharField('用户名', max_length = 30)
#    judge_name = models.CharField('评委姓名', max_length = 30)
#    password = models.CharField('密码', max_length = 16)
#    judge_type = models.CharField('评委类型', max_length = 30)
#    def __str__(self):
#        return  "评委姓名:"  + self.judge_username
#
