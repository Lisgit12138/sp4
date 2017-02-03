from django.shortcuts import render,HttpResponse
from sp4_sp.models import Student,Admin,MIS

# Create your views here.
def index(req):
    errors=[]
    if req.method=='POST':
        name = req.POST.get('name')
        id1=req.POST.get('id')
        idcard=req.POST.get('idcard')
        通过学号匹配到的学生 = Student.objects.filter(学号 = id1)
        通过姓名匹配到的学生 = Student.objects.filter(姓名 = name)
        通过身份证匹配到的学生 = Student.objects.filter(身份证号 = idcard)
        if not 通过姓名匹配到的学生:
            errors.append('未从数据库中匹配到您的姓名。')
        if not 通过学号匹配到的学生:
            errors.append('未从数据库中匹配到您的学号。')
        if not 通过身份证匹配到的学生:
            errors.append('未从数据库中匹配到您的身份证号（后六位）。')
        #if 通过学号匹配到的学生[0]==通过身份证匹配到的学生[0]==通过姓名匹配到的学生[0]:
        #    errors.append('您已经提交过信息，请勿重复提交！')
        if not errors:
            if 通过学号匹配到的学生[0] == 通过姓名匹配到的学生[0] == 通过身份证匹配到的学生[0]:
                待补办学生姓名 = 通过姓名匹配到的学生[0].姓名
                待补办学生学号 = 通过学号匹配到的学生[0].学号
                待补办学生身份证号 = 通过身份证匹配到的学生[0].身份证号
                匹配到的待补办学生 = MIS.objects.filter(姓名=待补办学生姓名, 学号=待补办学生学号, 身份证号=待补办学生身份证号)
                if 匹配到的待补办学生:
                    errors.append('您已经提交过补办信息，请勿重复提交。')
                    return render(req,'index.html',{'error':errors})
                else:
                    errors.append('您已经成功提交补办信息！')
                    MIS.objects.create(姓名=待补办学生姓名, 身份证号=待补办学生身份证号, 学号=待补办学生学号)
                    return render(req, 'index.html', {'error': errors})
            else:
                errors.append('您输入的姓名，学号，身份证号不匹配。')
        return render(req,'index.html',{'error':errors})
    else:
        return render(req,'index.html',{})
def lookth(req):
    error2=[]
    if req.method == 'POST':
        account = req.POST.get('account')
        passw = req.POST.get('password')
        通过账号匹配到的管理员 = Admin.objects.filter(name=account)
        通过密码匹配到的管理员 = Admin.objects.filter(password=passw)
        if not 通过账号匹配到的管理员:
            error2.append('未查询到您的管理员账号。')
        if not 通过密码匹配到的管理员:
            error2.append('请检查密码后重试，注意大小写。')
        if not error2:
            匹配到的管理员 = Admin.objects.filter(name=通过账号匹配到的管理员[0].name, password=通过密码匹配到的管理员[0].password)
            if not 匹配到的管理员:
                error2.append('您输入的账号密码不匹配。')
                return render(req, 'adminlogin.html', {'error': error2})
            else:
                all_mis = MIS.objects.all()
                return render(req,'lookup.html',{'mis':all_mis})
        return render(req,'adminlogin.html',{'error':error2})
    else:
        return render(req,'adminlogin.html',{})