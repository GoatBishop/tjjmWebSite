from django.shortcuts import render
from backManage import models
from backManage import forms
from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.

def get_all_school_list():
    allSchoolList = []
    with open("static/data/my_school_name.csv", "rb") as f:
        for eachline in f:
            allSchoolList.append(eachline.strip().decode())
#    print(allSchoolList)
    print(type(allSchoolList))
    return allSchoolList
        


def mylogin(request):
    if request.method == 'GET':
        print("我是mylogin的GET")
        contacts_telephone = request.COOKIES.get('contacts_telephone', '')
        return render(request, 'login-sch.html', locals())
    elif request.method == 'POST':
        # 获取表单的数据
        print("我是mylogin的POST")
        school = request.POST.get('school', '')
        password = request.POST.get('password', '')
        print(school, "--", password)
#        # 验证用户名，密码是否正确
        try:
            print("我进入mylogin的try里来了")
            user = models.College.objects.get(school = school,
                                           password = password)
            print(user)
            print("我存在数据库中")
            print(user.school, "--", user.contacts_telephone)
            print("===我输出了===")
            # 在当前连接的Session中记录当前用户的信息
            request.session['userinfo'] = {
                "school": user.school,
                'contacts_telephone': user.contacts_telephone
            }
        except:
            #登录失败
            print("我登录失败了")
            return render(request, 'login-sch.html', locals())

        # 处理COOKIES
        print("我要跳转到index-sch.html")
        resp = redirect(reverse('school:collegemain'))
        resp.set_cookie('contacts_telephone', user.contacts_telephone, 5*24*60*60)
        print("我已经设置了cookie")
        return resp
        #HttpResponse("<h1>Success</h1>")


def mylogout(request):
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return redirect(reverse('school:slogin')) 


def myregister(request):
    if request.method == 'GET':
        school_list = get_all_school_list()
        return render(request, 'sch-forgetpass.html', locals())
    elif request.method == 'POST':
        collegeForm = forms.CollegeForm(request.POST, request.FILES)
        
        if collegeForm.is_valid():
            contacts_telephone = collegeForm.cleaned_data.get('contacts_telephone')
            school = collegeForm.cleaned_data.get('school')
            print(contacts_telephone, "==", school)
            collegeForm.save()
            return HttpResponse("<h1>注册成功！</h1>")
        else:
            file_error = forms.get_errors(collegeForm)
            contacts_telephone = request.POST.get('contacts_telephone', '')
            school = request.POST.get('school', '')
            contacts = request.POST.get('contacts', '')
#            password = request.POST.get('password', '')
            print(collegeForm.errors.get_json_data())
            print("我是: ", contacts, "学校为: ", school,
                  '电话是：', contacts_telephone)
            school_list = get_all_school_list()
            return render(request, 'sch-forgetpass.html', locals())
            
        
def repsw(request):
    if request.method == 'GET':
        return render(request, 'sch-password.html', locals())
    elif request.method == 'POST':
        # 获取表单的数据
        contacts_telephone = request.POST.get('contacts_telephone', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
#        # 验证用户名，密码是否正确
        if password == '':
            password_error = "不能为空"
            return render(request, 'sch-password.html', locals())
        if password != password2:
            password2_error = "两次密码不一致"
            return render(request, 'sch-password.html', locals())
        try:
            user = models.College.objects.get(contacts_telephone = contacts_telephone)
            user.password = password
            user.save()
            return HttpResponse("<h1>修改密码成功！</h1>")
            # 在当前连接的Session中记录当前用户的信息
        except:
            #手机验证失败
            user_error = "没有当前手机号"
            return render(request, 'sch-password.html', locals())

def college_index(request):
    session_college = request.session.get('userinfo', '')
    if session_college:
        print(session_college)
        #contacts_telephone
        contacts_telephone = session_college['contacts_telephone']
        user = models.College.objects.get(contacts_telephone = contacts_telephone)
        school = user.school
        return render(request, "index-sch.html", locals())
    else:
        print("我没有session")
        return redirect(reverse('school:slogin'))

def chpsw(request):
    #change-password.html
    if request.method == 'GET':
        print("我进入了修改密码的GET")
        return render(request, 'change-password.html', locals())
    elif request.method == 'POST':
        # 获取表单的数据
        print("我进入了修改密码的POST")
        contacts_telephone = request.COOKIES.get('contacts_telephone', '')
        oldpassword = request.POST.get('oldpassword', '')
        newpassword = request.POST.get('newpassword', '')
        newpassword2 = request.POST.get('newpassword2', '')
        print( oldpassword, "--", newpassword,
              '--', newpassword2)
#        # 验证密码，密码是否正确
        if newpassword == '':
            password_error = "密码不能为空"
            return render(request, 'change-password.html', locals())
        if newpassword != newpassword2:
            password2_error = "两次密码不一致"
            return  render(request, 'change-password.html', locals())
        try:
            user = models.College.objects.get(contacts_telephone = contacts_telephone, 
                                              password = oldpassword)
            user.password = newpassword
            user.save()
            return HttpResponse("<h1>修改成功！</h1>")
            # 在当前连接的Session中记录当前用户的信息
        except:
            #手机验证失败
            user_error = "密码不正确"
            return render(request, 'change-password.html', locals())

def part_school_teacher(request):
    session_school = request.session.get('userinfo', '')
    school = session_school['school']
    zhidao = models.Instructor.objects.filter(school = models.College.objects.get(school = school))
    
    if request.method == "GET":
        return render(request, 'school-tea.html', locals())
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        if name:
            zhidao = zhidao.filter(name = name)
            return render(request, 'school-tea.html', locals())
        else:
            return render(request, 'school-tea.html', locals())


def part_game_team(request):
    session_school = request.session.get('userinfo', '')
    school = session_school['school']
    school = models.College.objects.get(school = school)
    teams = models.Team.objects.filter(school = school, status = "待审核")
    print(teams)
#    captains = models.Member.objects.filter()
    all_num = school.number_team
    team_num = len(teams)
    surplus_num = all_num - team_num
    
    if request.method == "GET":
        return render(request, "sch-waitteam.html", locals())
    elif request.method == "POST":
        teamFindForm = forms.TeamFindForm(request.POST, request.FILES)
        if teamFindForm.is_valid():
            group = request.POST.get('group', '')
            work_group = request.POST.get('work_group', '')
            if group:
                if work_group:
                    teams = teams.filter(group = group, work_group = work_group)
                else:
                    teams = teams.filter(group = group)
                return render(request, "sch-waitteam.html", locals())
            else:
                if work_group:
                    teams = teams.filter(work_group = work_group)
                else:
                    pass
                return render(request, "sch-waitteam.html", locals())
        else:
            file_error = forms.get_errors(teamFindForm)
            print(teamFindForm.errors.get_json_data())
            return render(request, 'sch-waitteam.html', locals())

def part_game_team_all(request):
    session_school = request.session.get('userinfo', '')
    school = session_school['school']
    school = models.College.objects.get(school = school)
    teams = models.Team.objects.filter(school = school)
#    captains = models.Member.objects.filter()
    all_num = school.number_team
    team_num = len(teams)
    surplus_num = all_num - team_num
    
    if request.method == "GET":
        return render(request, "sch-waitteam-all.html", locals())
    elif request.method == "POST":
        teamFindForm = forms.TeamFindForm(request.POST, request.FILES)
        if teamFindForm.is_valid():
            group = request.POST.get('group', '')
            work_group = request.POST.get('work_group', '')
            if group:
                if work_group:
                    teams = teams.filter(group = group, work_group = work_group)
                else:
                    teams = teams.filter(group = group)
                return render(request, "sch-waitteam-all.html", locals())
            else:
                if work_group:
                    teams = teams.filter(work_group = work_group)
                else:
                    pass
                return render(request, "sch-waitteam-all.html", locals())
        else:
            file_error = forms.get_errors(teamFindForm)
            print(teamFindForm.errors.get_json_data())
            return render(request, 'sch-waitteam-all.html', locals())



def part_game_paper(request):
    session_school = request.session.get('userinfo', '')
    school = session_school['school']
    school = models.College.objects.get(school = school)
    teams = models.Team.objects.filter(school = school, status_is_pass = "未通过")
#    works = [t.work for t in teams]
    
    all_num = school.number_team
    team_num = len(teams)
    surplus_num = all_num - team_num
    
    if request.method == "GET":
        print("我是part_game_paper的GET")
        return render(request, "sch-game.html", locals())
    elif request.method == "POST":
        teamFindForm = forms.TeamFindForm(request.POST, request.FILES)
        if teamFindForm.is_valid():
            group = request.POST.get('group', '')
            work_group = request.POST.get('work_group', '')
            if group:
                if work_group:
                    teams = teams.filter(group = group, work_group = work_group)
                else:
                    teams = teams.filter(group = group)
                return render(request, "sch-game.html", locals())
            else:
                if work_group:
                    teams = teams.filter(work_group = work_group)
                else:
                    pass
                return render(request, "sch-game.html", locals())
        else:
            file_error = forms.get_errors(teamFindForm)
            print(teamFindForm.errors.get_json_data())
            return render(request, 'sch-game.html', locals())

def part_game_paper_all(request):
    session_school = request.session.get('userinfo', '')
    school = session_school['school']
    school = models.College.objects.get(school = school)
    teams = models.Team.objects.filter(school = school)
#    works = [t.work for t in teams]
    
    all_num = school.number_team
    team_num = len(teams)
    surplus_num = all_num - team_num
    
    if request.method == "GET":
        print("我是part_game_paper的GET")
        return render(request, "sch-game.html", locals())
    elif request.method == "POST":
        teamFindForm = forms.TeamFindForm(request.POST, request.FILES)
        if teamFindForm.is_valid():
            group = request.POST.get('group', '')
            work_group = request.POST.get('work_group', '')
            if group:
                if work_group:
                    teams = teams.filter(group = group, work_group = work_group)
                else:
                    teams = teams.filter(group = group)
                return render(request, "sch-game.html", locals())
            else:
                if work_group:
                    teams = teams.filter(work_group = work_group)
                else:
                    pass
                return render(request, "sch-game.html", locals())
        else:
            file_error = forms.get_errors(teamFindForm)
            print(teamFindForm.errors.get_json_data())
            return render(request, 'sch-game.html', locals())

def team_pass(request, work_id):
    team = models.Team.objects.get(work_id = work_id)
    team.status_is_pass = "通过"
    team.status = "通过"
    team.status_is_submit = "报送"
    team.save()
    return redirect(reverse("school:game_team"))
    

def team_no_pass(request, work_id):
    team = models.Team.objects.get(work_id = work_id)
    team.status_is_pass = "未通过"
    team.status = "未通过"
    team.save()
    return redirect(reverse("school:game_team"))


def instruc_del(request, telephone):
#    session_back = request.session.get('userinfo', '')
#    back_username = session_back['username']

    try:
        instruc = models.Instructor.objects.get(telephone = telephone)
        instruc.delete()
        return redirect(reverse("school:schoolteacher"))
    except:
        return HttpResponse("没有找到该导师信息,删除失败")

#=========测试===========

def testupload(request):
    if request.method == "GET":
        return render(request, "test_upload_paper.html")
    elif request.method == "POST":
#        work_name = request.POST.get("work_name", "")
#        paper = request.FILES.get("paper", "")
#        models.Work.objects.create(work_name = work_name,
#                                   paper = paper)
#        return HttpResponse("Success!")
        workForm = forms.WorkForm(request.POST, request.FILES)
        #request.FILES用于验证paper
        #request.POST用于验证work_name
        if workForm.is_valid():
            workForm.save()
            return HttpResponse("Success!")
        else:
            file_error = forms.get_errors(workForm)
            return render(request, "test_upload_paper.html", locals())

def test_school_list(request):
    school_list = get_all_school_list()
    return HttpResponse(school_list)


def testPage(request):
    user = models.College.objects.create(
                school = "安徽财经大学",
                password = "19970928",
                contacts = "桂扬",
                telephone = "13013103320"
            )
    return HttpResponse("Yes! 添加成功！")


