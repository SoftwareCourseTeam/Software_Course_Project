import json

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01.models import  UserInfo,Device,Borrow,Scrap
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


@csrf_exempt
def login_me(request):
    if request.method == "GET":
        return render(request,'login.html')

@csrf_exempt
def login_me_deal(request):
    user = request.POST.get("username")
    pwd = request.POST.get("password")
    print(user,pwd)
    list=UserInfo.objects.filter(name=user,password=pwd).first()
    print(list)
    if(list == None):
        print("asdfca")
        return render(request,'login.html',{"error_msg": "用户名或密码错误"})
    else:
        print("sad")
        request.session["info"]={"id":list.id,"name":user}
        res_dic={"status":'success'}
        return JsonResponse(res_dic)

def logout(request):
    request.session.clear()
    return redirect('/login/')

@csrf_exempt
def regist_user(request):
    if request.method == "GET":
        return render(request,'regist.html')
    user = request.POST.get("username")
    pwd = request.POST.get("password")
    admin_pwd = request.POST.get("admin")
    if UserInfo.objects.filter(name=user).first() ==None:
        if admin_pwd != "123":
            UserInfo.objects.create(name=user, password=pwd)
        else:
            UserInfo.objects.create(name=user, password=pwd,admin=1)
    print("chenggong")
    return redirect('/login/')

@csrf_exempt
def regist_user_new(request):
    user = request.POST.get("username")
    pwd = request.POST.get("password")
    admin_pwd = request.POST.get("admin")
    print(admin_pwd)
    if UserInfo.objects.filter(name=user).first() == None:
        if admin_pwd != "123":
            UserInfo.objects.create(name=user, password=pwd)
        else:
            UserInfo.objects.create(name=user, password=pwd, admin=1)
    return HttpResponse("成功了")

def device_main(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    return render(request,'device_list.html')

@csrf_exempt
def device_load(request):
    info = request.session.get("info")
    user = UserInfo.objects.get(id=info["id"])
    type_load=request.GET.get('type')
    print(type_load)
    if user.admin == 0 and type_load != "borrow":
        dev_list = Device.objects.filter(user=user)
    else:
        dev_list = Device.objects.all()
    data_list = []
    for item in dev_list:
        item_dir = {}
        item_dir['id'] = item.id
        item_dir['name'] = item.name
        item_dir['number'] = item.num
        item_dir['model_spec'] = item.model_spec
        item_dir['purchase_date'] = item.purchase_date
        if item.image != None:
            item_dir['image'] = item.image.url
        data_list.append(item_dir)
    res_dic={"devices":data_list}
    return JsonResponse(res_dic)

@csrf_exempt
def device_add(request):
    info = request.session.get("info")
    user = UserInfo.objects.get(id=info["id"])
    form_data = request.POST.dict()
    print(form_data)
    name = form_data["addDeviceName"]
    num = form_data["addDeviceNumber"]
    spe = form_data["addDeviceModelSpec"]
    date = form_data["addDevicePurchaseDate"]
    image=request.FILES["addDeviceImage"]
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    Device.objects.create(name=name, num=num,
                          model_spec=spe,purchase_date=date,image=filename,user=user)
    return HttpResponse("成功了")

@csrf_exempt
def device_edit(request):
    form_data = request.POST.dict()
    print(form_data)
    name = form_data["editDeviceName"]
    num = form_data["editDeviceNumber"]
    spe = form_data["editDeviceModelSpec"]
    date = form_data["editDevicePurchaseDate"]
    id = form_data['id']
    image = request.FILES["editDeviceImage"]
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    print(name, num, spe, date,id)
    Device.objects.filter(id=id).update(name=name, num=num,
                          model_spec=spe,purchase_date=date,image=filename)
    return HttpResponse("成功了")

@csrf_exempt
def device_edit_show(request):
    id=request.GET.get('id')
    data=Device.objects.filter(id=id).first()
    print(data,id)
    res_dic = {'id':data.id,'name':data.name,'number':data.num,
               'model_spec':data.model_spec,'purchase_date':data.purchase_date}
    return JsonResponse({'device':res_dic})

@csrf_exempt
def device_delete(request):
    form_data = request.POST.dict()
    id = eval(form_data['id'])
    tmp=1
    if type(id)==type(tmp):
        Device.objects.filter(id=id).delete()
        return HttpResponse("成功了")
    for i in id:
        Device.objects.filter(id=i).delete()

    return HttpResponse("成功了")


def device_search(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    if request.method == "GET":
        return render(request, 'device_search.html')

@csrf_exempt
def device_search_act(request):
    info = request.session.get("info")
    user = UserInfo.objects.get(id=info["id"])
    qtype = request.GET.get('query_type')
    qdata=request.GET.get('query_input')
    if user.admin==0:
        if qtype=="name":
            data_list=Device.objects.filter(name=qdata,user=user)
        elif qtype=='model' :
            data_list=Device.objects.filter(model_spec=qdata,user=user)
    else:
        if qtype=="name":
            data_list=Device.objects.filter(name=qdata)
        elif qtype=='model' :
            data_list=Device.objects.filter(model_spec=qdata)
    res_list = []
    for data in data_list:
        dic={}
        print(data)
        dic['id']=data.id
        dic['name']=data.name
        dic['num'] = data.num
        dic['model'] = data.model_spec
        dic['purchase_date'] = data.purchase_date
        if data.image != None:
            dic['image'] = data.image.url
        res_list.append(dic)
    res_dic={'devices':res_list}
    return JsonResponse(res_dic)

def device_scrap(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    user = UserInfo.objects.get(id=info["id"])
    if user.admin==0:
        return redirect("/device_list/")
    if request.method == "GET":
        return render(request, 'device_scrap.html')

@csrf_exempt
def device_scrap_my(request):
    info = request.session.get("info")
    data_list = Scrap.objects.filter(user=info["id"])
    res_list = []
    for data in data_list:
        dic = {}
        dic['id'] = data.id
        dic['name'] = data.device.name
        dic['scrapQuantity'] = data.number
        dic['scrapDate'] = data.scrap_date
        res_list.append(dic)
    res_dic = {'scrappedDevices': res_list}
    return JsonResponse(res_dic)

@csrf_exempt
def device_scrap_submit(request):
    form_data = request.POST.dict()
    device=Device.objects.filter(id=form_data["deviceId"]).first()
    if device.num < int(form_data["scrapQuantity"]):
        return JsonResponse({'error': '设备数量不足'}, status=400)
    info = request.session.get("info")
    user=UserInfo.objects.get(id=info["id"])
    Scrap.objects.create(user=user, device=device,number=form_data["scrapQuantity"])
    Device.objects.filter(id=form_data["deviceId"]).update(num=device.num-int(form_data["scrapQuantity"]))
    return HttpResponse("成功了")

def device_borrow(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    if request.method == "GET":
        return render(request, 'device_borrow.html')

@csrf_exempt
def device_borrow_my(request):
    info = request.session.get("info")
    data_list = Borrow.objects.filter(user=info["id"])
    res_list = []
    for data in data_list:
        dic = {}
        dic['id'] = data.id
        dic['name'] = data.device.name
        dic['borrowNumber'] = data.number
        dic['borrowDate'] = data.borrow_date
        dic['returnDate'] = data.return_date
        dic['status'] = data.status
        print(data.device.name,data.status)
        res_list.append(dic)
    res_dic = {'borrowedDevices': res_list}
    return JsonResponse(res_dic)

@csrf_exempt
def device_borrow_submit(request):
    form_data = request.POST.dict()
    device=Device.objects.filter(id=form_data["deviceId"]).first()
    if device.num < int(form_data["borrowNumber"]):
        return JsonResponse({'error': '设备数量不足'}, status=400)
    info = request.session.get("info")
    user=UserInfo.objects.get(id=info["id"])
    Borrow.objects.create(user=user, device=device,number=form_data["borrowNumber"])
    return HttpResponse("成功了")

@csrf_exempt
def device_borrow_return(request):
    form_data = request.POST.dict()
    print(form_data)
    device=Borrow.objects.filter(id=form_data["deviceId"]).first()
    device.return_device()
    return HttpResponse("成功了")

@csrf_exempt
def device_borrow_delete(request):
    form_data = request.POST.dict()
    device=Borrow.objects.filter(id=form_data["deviceId"]).delete()
    return HttpResponse("成功了")

def message_center(request):
    info = request.session.get("info")
    user = UserInfo.objects.get(id=info["id"])
    if not info:
        return redirect("/login/")
    if request.method == "GET":
        return render(request, 'message_center.html',{'admin': user.admin})

@csrf_exempt
def message_center_borrow(request):
    info = request.session.get("info")
    data_list = Borrow.objects.filter(status=0)
    res_list = []
    for data in data_list:
        dic = {}
        dic['id'] = data.id
        dic['deviceName'] = data.device.name
        dic['borrowNumber'] = data.number
        dic['requestDate'] = data.borrow_date
        dic['requester'] = data.user.name
        res_list.append(dic)
    res_dic = {'requests': res_list}
    return JsonResponse(res_dic)

@csrf_exempt
def message_center_processed(request):
    info = request.session.get("info")
    user = UserInfo.objects.get(id=info["id"])
    if user.admin == 0:
        data_list = Borrow.objects.filter(user=info["id"])
    else:
        data_list = Borrow.objects.all()
    res_list = []
    for data in data_list:
        dic = {}
        dic['id'] = data.id
        dic['deviceName'] = data.device.name
        dic['borrowNumber'] = data.number
        dic['requestDate'] = data.borrow_date
        dic['requester'] = data.user.name
        if data.status == 0:
            dic["approved"]="未处理"
        elif data.status == 1:
            dic["approved"]="同意"
        elif data.status == 2:
            dic["approved"] = "拒绝"
        else:
            dic["approved"] = "已归还"
        res_list.append(dic)
    res_dic = {'requests': res_list}
    return JsonResponse(res_dic)

@csrf_exempt
def message_center_request(request):
    info = request.session.get("info")
    form_data = request.POST.dict()
    print(form_data)
    borrow = Borrow.objects.filter(id=form_data["id"]).first()
    if form_data["approve"] == 'true':
        borrow.borrow_device()
    else:
        Borrow.objects.filter(id=form_data["id"]).update(status=2)
    return HttpResponse("成功了")

def user_info(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    if request.method == "GET":
        return render(request, 'user_info.html')

@csrf_exempt
def profile_load(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    user = UserInfo.objects.get(id=info["id"])
    dic = {}
    dic["username"]=user.real_name
    dic["gender"] = user.sex
    dic["age"] = user.age
    dic["phone"] = user.phone
    dic["email"] = user.email
    res_dic = {'user': dic}
    return JsonResponse(res_dic)

@csrf_exempt
def profile_edit(request):
    info = request.session.get("info")
    form_data = request.POST.dict()
    UserInfo.objects.filter(id=info["id"]).update(real_name=form_data["editUsername"],sex=form_data["editGender"],
                                                  age=form_data["editAge"],phone=form_data["editPhone"],email=form_data["editEmail"])
    return HttpResponse("成功")

@csrf_exempt
def profile_password(request):
    info = request.session.get("info")
    form_data = request.POST.dict()
    user=UserInfo.objects.get(id=info["id"])
    if user.password == form_data["currentPassword"]:
        UserInfo.objects.filter(id=info["id"]).update(password=form_data["newPassword"])
        return HttpResponse("成功")

def user_edit(request):
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    if request.method == "GET":
        return render(request, 'edit_info.html')

def admin(request):
    Borrow.objects.all().delete()
    UserInfo.objects.all().delete()
    Device.objects.all().delete()
    Scrap.objects.all().delete()
    return HttpResponse("成功了")