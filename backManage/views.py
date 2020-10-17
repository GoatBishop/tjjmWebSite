from django.shortcuts import render
from backManage import models
from backManage import forms
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import random
import time
import csv
# Create your views here.

def judge_username_random(id_length = 3):
    #团队作品编号随机数生成器
    t = str(int(time.time()))
    j_username = "r" + t
    num = ["0", "1", "2", "3", "4"]
    for item in range(id_length):
        j_username += random.choice(num)
    return j_username

def produce_judge(is_one = True):
    if is_one:
        judge_username = judge_username_random()
        judge = models.Judge.objects.create(judge_username = judge_username)
    else:
        judge_username = judge_username_random()
        password = judge_username[-6:]
        judge = models.Judge.objects.create(judge_username = judge_username,
                                            password = password)
    return judge


def mylogin(request):
    if request.method == 'GET':
        print("backManage: 我是mylogin的GET")
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        # 获取表单的数据
        print("backManage: 我是mylogin的POST")
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, "--", password)
#        # 验证用户名，密码是否正确
        print("我进入mylogin的try里来了")
        user = authenticate(username = username, password = password)
        if user is not None:
            print("我存在数据库中")
            if user.is_active:
                login(request, user)
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                else:
                    resp = redirect(reverse('back:bmain'))
                print("我已经设置了cookie")
                return resp
            # 执行验证通过后的代码
            return render(request, 'login.html', locals())
        else:
            print("我登录失败了")
            return render(request, 'login.html', locals())


@login_required(login_url='/back/login/')
def back_main(request):
    return render(request, "index.html", locals())


@login_required(login_url='/back/login/')
def work_list(request):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    teams = models.Team.objects.filter(status_is_pass = "通过")
    works = [t.work for t in teams]
    if request.method == "GET":
#        print(works)
        return render(request, "work.html", locals())
    elif request.method == "POST":
        status_is_submit = request.POST.get("is_submit", "")
        if status_is_submit:
            print(status_is_submit)
            teams = teams.filter(status_is_submit = status_is_submit)
            works = [t.work for t in teams]
            return render(request, "work.html", locals())
        else:
            return render(request, "work.html", locals())

@login_required(login_url='/back/login/')
def judge_list(request):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    if request.method == "GET":
        judges = models.Judge.objects.all()
        return render(request, "a-teacher.html", locals())
    
@login_required(login_url='/back/login/')
def random_one(request):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    if request.method == "GET":
        judge = produce_judge()
        return render(request, "teacher-add.html", locals())
    elif request.method == "POST":
        judgeForm = forms.JudgeForm(request.POST, request.FILES)
        if judgeForm.is_valid():
#            judge_username = request.POST.get("judge_username", "")
            judge_username = judgeForm.cleaned_data.get("judge_username")
            judge_name = request.POST.get("judge_name", "")
            password = request.POST.get("password", "")
            judge_type = request.POST.get("judge_type", "")
            print("judge_username:" + judge_username)
            judge = models.Judge.objects.get(judge_username = judge_username)
            judge.judge_name = judge_name
            judge.password = password
            judge.judge_type = judge_type
            judge.save()
            return render(request, 'back-success.html', locals()) 
        else:
            file_error = forms.get_errors(judgeForm)
            print(judgeForm.errors.get_json_data())
            return render(request, 'teacher-add.html', locals()) 
           
           
@login_required(login_url='/back/login/')
def random_many(request):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    if request.method == "GET":
        return render(request, "teacher-addall.html", locals())
    elif request.method == "POST":
        number = request.POST.get("number", "")
        if number:
            num = int(number)
            with open((r"./judge/judge_" + str(int(time.time())) + ".csv"), "w", newline = '') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'password'])
                usernameList = []
                pswList = []
                
                while(num > 0):
                    num -= 1
                    judge = produce_judge(False)
                    usernameList.append(judge.judge_username)
                    pswList.append(judge.password)
                writer.writerows(zip(usernameList, pswList))
            return render(request, 'back-success.html', locals())
        else:
            render(request, 'teacher-addall.html', locals())

@login_required(login_url='/back/login/')
def wait_round2_list(request):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    teams = models.Team.objects.filter(status_is_pass = "通过",
                                       status_is_review = "否")
    works = [t.work for t in teams]
    if request.method == "GET":
#        print(works)
        return render(request, "wait-game.html", locals())
    elif request.method == "POST":
        school = request.POST.get("school", "")
        if school:
            print(school)
            team_school = models.School.objects.filter(school = school)
            teams = teams.filter(school = team_school)
            works = [t.work for t in teams]
            return render(request, "wait-game.html", locals())
        else:
            return render(request, "wait-game.html", locals())

@login_required(login_url='/back/login/')
def rounding2_list(request):
    teams_temp = models.Team.objects.filter(status_is_pass = "通过",
                                       status_is_review = "是")
    #更新队伍
    for t in teams_temp:
        scores = models.Score.objects.filter(work = t.work)
        len_all_scores = len(scores)
        temp_s = [s for s in scores if s.judge_is_review == "是"]
        len_ok = len(temp_s)
        if len_ok < len_all_scores:
            pass
        elif len_ok == len_all_scores:
            t.status_review_end = "是"
            t.save()
    teams = models.Team.objects.filter(status_is_pass = "通过",
                                       status_is_review = "是",
                                       status_review_end = "否")
    works = [t.work for t in teams]
    if request.method == "GET":
#        print(works)
        return render(request, "in-game.html", locals())
    elif request.method == "POST":
        school = request.POST.get("school", "")
        if school:
            print(school)
            team_school = models.School.objects.filter(school = school)
            teams = teams.filter(school = team_school)
            works = [t.work for t in teams]
            return render(request, "in-game.html", locals())
        else:
            return render(request, "in-game.html", locals())

@login_required(login_url='/back/login/')
def rounded2_list(request):
    teams_temp = models.Team.objects.filter(status_is_pass = "通过",
                                       status_is_review = "是")
    #更新队伍
    for t in teams_temp:
        scores = models.Score.objects.filter(work = t.work)
        len_all_scores = len(scores)
        temp_s = [s for s in scores if s.judge_is_review == "是"]
        len_ok = len(temp_s)
        if len_ok < len_all_scores:
            pass
        elif len_ok == len_all_scores:
            t.status_review_end = "是"
            t.save()
    teams = models.Team.objects.filter(status_is_pass = "通过",
                                       status_is_review = "是",
                                       status_review_end = "是")
        
    works = [t.work for t in teams]
    score_all = [models.Score.objects.filter(work = w) for w in works]
    score_sum = []
    s_temp = 0
    for s in score_all:
        s_temp = sum([i.judge_score for i in s])/len(s)
        score_sum.append(s_temp)
    scores = score_sum
    if request.method == "GET":
#        print(works)
        return render(request, "game-finsh.html", locals())
    elif request.method == "POST":
        school = request.POST.get("school", "")
        if school:
            print(school)
            team_school = models.School.objects.filter(school = school)
            teams = teams.filter(school = team_school)
            works = [t.work for t in teams]
            return render(request, "game-finsh.html", locals())
        else:
            return render(request, "game-finsh.html", locals())

@login_required(login_url='/back/login/')
def team_situation(request):
    schools = models.College.objects.all()
    team_num = [len(models.Team.objects.filter(school = s)) for s in schools]
#    print(team_num)
    school_team = zip(schools, team_num)
    print(school_team)
    print(type(school_team))
    if request.method == "GET":
#        print(works)
        return render(request, "team.html", locals())

@login_required(login_url='/back/login/')
def tuihui(request, work_id):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    team = models.Team.objects.get(work_id = work_id)
    team.status_is_submit = "退回"
    team.status = "退回"
    team.save()
    return redirect(reverse('back:worklist'))


def mylogout(request):
    logout(request)
    return redirect(reverse('back:blogin'))
    

@login_required(login_url='/back/login/')
def assign_judges(request):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']
    teams = models.Team.objects.filter(status_is_pass = "通过",
                                       status_is_submit = "报送",
                                       status_is_review = "否")
    works = [t.work for t in teams]
    judges = models.Judge.objects.all()
    judge_list = list(judges)
    print(judge_list)
    if request.method == "GET":
        return render(request, "distribution-teacher.html", locals())
    elif request.method == "POST":
        number = request.POST.get("number", "")
        if number:
            num = int(number)
            print(num)
            for w in works:
                random.shuffle(judge_list)
                wj_list = judge_list[:num]
                for item in wj_list:
                    s = models.Score.objects.create(work = w,
                                                    judge = item)
            for t in teams:
                t.status_is_review = "是"
                t.save()
            return render(request, 'back-success.html', locals())
        else:
            return render(request, "distribution-teacher.html", locals())

