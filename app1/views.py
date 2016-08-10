from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context_processors import request
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import json

from django.template import RequestContext, loader
from .forms import people_form, Activity_form,people_detail_form,Activity_detail_form,settings_form
from .models import People_model, Activity_model,detail_model,settings_model
from django.db.models import Q
def xyz(request):
    ##print("i m in settings")
    f = settings_form
    if request.method == "POST":
        ##print("i m at post")
        f = settings_form(request.POST)
        if f.is_valid():
            Project_Allocated = request.POST.get('Project_Allocated', '')
            ##print('p=', Project_Allocated)
            model=settings_model( Id=1,Project_Allocated=Project_Allocated)
            model.save()

            return render(request, "project.html", {"check":Project_Allocated})
    else:
        f = settings_form(request.GET)
        setting_info=settings_model.objects.filter(Id=1)
        ##print("setting_info",setting_info)
        if setting_info:
            ##print('p=',setting_info.values())
            setting_data={"setting_detalis":setting_info}
            Project_Allocated= [i.Project_Allocated for i in setting_data["setting_detalis"]]
            ##print("ddddddd===",Project_Allocated)
        else:
            Project_Allocated='3'


        return render(request, "project.html", {"check": Project_Allocated})



def add_people(request):
    f=people_form
    ##print("i m in before if block");
    ##print("request",request.method);
    if request.method=="POST":
        ##print("i m n method")
        f=people_form(request.POST)
        if f.is_valid():
            ##print ("i m in form valid");
            name=request.POST.get('name','')
            t=request.POST.get('type','')
            v=request.POST.get('vacation_plan','')
            visa = request.POST.get('visa_status', '')
           ## print ("visa=",visa);
            ##print ('vacation=',v);
            model=People_model(name=name,vacation_plan=v,visa_status=visa)
            if t !="Add Activity":
                model1 = detail_model(Act_name=t, emp_name=name)
                model1.save()
            model.save()

            ##print ("out of box");
            #return render(request,'project.html',{'form': f})
            return redirect('/home')
    else:
        f = people_form(request.GET)
        return render(request,'Add_People.html',{'form': f})
    #return render(request,'Add_people.html',{'form':f})
    return redirect('/home')

@csrf_exempt
def check_availability(request,name):
    n=name.strip()
    model=People_model.objects.filter(name=n)
    if model:
        ##print("if i m there")
        return HttpResponse(json.dumps({"available":"1"}),
                     content_type="application/json")
    else:
       ## print("else")
        return HttpResponse(json.dumps({"available": "0"}),
                     content_type="application/json")

@csrf_exempt
def activity_check_availability(request,name,type):
    n=name.strip()
    model=Activity_model.objects.filter(Activity_Name=n,Activity_type=type)
    if model:
        ##print("if i m there")
        return HttpResponse(json.dumps({"available":"1"}),
                     content_type="application/json")
    else:
       ## print("else")
        return HttpResponse(json.dumps({"available": "0"}),
                     content_type="application/json")

def add_activity(request):
    f=Activity_form

    if request.method=="POST":
        #print ("request act=",request.method())
        f=Activity_form(request.POST)
        #print("valid=",f.is_valid());
        if f.is_valid():
            #i=request.POST.get('Activity_Id','')
            n=request.POST.get('Activity_Name',)
            name=request.POST.getlist('Add_people','')
            customer_name=request.POST.get('customer','')
            description=request.POST.get('Description','')
           # print ('name=',name);
            #p=People_model.objects.get(name=name)
            type=request.POST.get('type','')
            #print ("kkkkkk=",type);
            model=Activity_model(Activity_Name=n,Activity_type=type,Customer_name=customer_name,Description=description)
            for i in name:
                if i!="Add-people":
                    detail_model1=detail_model(Act_name=n,emp_name=i)
                    #print ("i=",i);
                    detail_model1.save()
            model.save()
        #return render(request,'project.html',{'form': f} )
        return redirect('/home')
    else:
        f = people_form(request.GET)
        return render(request,'Add_Activity.html',{'form': f})

@csrf_exempt
def getdata(request):
     People_info=People_model.objects.all()
     print ("people=",People_info);
     People_data={"People_details":People_info}
     print("people_data",People_data)

     return HttpResponse(json.dumps({i.Id:str(i.name) for i in People_data["People_details"]}),
            content_type="application/json")


@csrf_exempt
def Get_activity(request):
    Activity_info = Activity_model.objects.all()
    #print("activity=",Activity_info )
    Activity_data = {"Activity_details": Activity_info}

    return HttpResponse(json.dumps({i. Activity_Id: str(i. Activity_Name) for i in Activity_data["Activity_details"]}),
                        content_type="application/json")

@csrf_exempt
def Get_activity_type(request):
    Activity_type_info = Activity_model.objects.filter(Activity_type='NFV')
    Activity_type_data = {"Activity_type_details": Activity_type_info}

    return HttpResponse(json.dumps({i. Activity_Id: str(i. Activity_Name) for i in Activity_type_data["Activity_type_details"]}),
                        content_type="application/json")

@csrf_exempt
def front_activity_type(request,type):
    Activity_type_info = Activity_model.objects.filter(Activity_type=type,state='1')
    Activity_type_data = {"Activity_type_details": Activity_type_info}

    return HttpResponse(json.dumps({i. Activity_Id: str(i. Activity_Name) for i in Activity_type_data["Activity_type_details"]}),
                        content_type="application/json")
@csrf_exempt
def front_people_type(request,Act_name):
    A = Activity_model.objects.filter(Q(state='0')|Q( Activity_type='MISC'))
    A_data = {"A-type": A}
    m=[str(j.Activity_Name) for j in A_data["A-type"]]
    ##print("m===",m);
    detail_type_info = detail_model.objects.filter(Act_name=Act_name)
    detail_type_data = {"detail_type_details": detail_type_info}
   # print("type=",type(detail_type_data))
    d=[str(i.emp_name) for i in detail_type_data["detail_type_details"]]
    ##print("d==",d)
    name = {}
    dict={}
    l = detail_model.objects.filter().exclude(Act_name__in=m).values('emp_name').annotate(acnt=Count('emp_name'))

    ##print("test==", l)
    l_data = {"l-type": l}
    ##print("l_data", l_data["l-type"])
    # cnt=[str(j.emp_name):str(j.acnt) for j in l_data["l-type"]]

    for j in l_data["l-type"]:
        print(j["acnt"], j["emp_name"])

        name[str(j["emp_name"])] = str(j["acnt"])
    ##print ("name=====",name)

    for j in d:
        flag=0
        for i, k in name.items():
            if j==i:
                dict[j]=k;
                flag=1
        if flag==0:
           dict[j]='0'
    ##print ("dict=",dict)


    return HttpResponse(json.dumps(dict),
                        content_type="application/json")



@csrf_exempt
def Get_activity_type1(request):
    Activity_type_info = Activity_model.objects.filter(Activity_type='NON-NFV')
    Activity_type_data = {"Activity_type_details": Activity_type_info}

    return HttpResponse(json.dumps({i. Activity_Id: str(i. Activity_Name) for i in Activity_type_data["Activity_type_details"]}),
                        content_type="application/json")
@csrf_exempt
def Get_activity_type2(request):
    Activity_type_info = Activity_model.objects.filter(Activity_type='MISC')
    Activity_type_data = {"Activity_type_details": Activity_type_info}

    return HttpResponse(json.dumps({i. Activity_Id: str(i. Activity_Name) for i in Activity_type_data["Activity_type_details"]}),
                        content_type="application/json")


def people_detail(request,people_name):
    f=people_detail_form
    global global_people_name
    global_people_name=people_name
    #print("i m in before if block");
    #print("people_name=",people_name);
    #print("request",request.method);
    if request.method=="GET":
        #print("i m n method")
        People_info = People_model.objects.filter(name=people_name)
        #print("people=", People_info)
        People_data ={"People_details": People_info}
        return render(request,'people_detail.html',People_data)
    else:
        f = people_detail_form(request.POST)
        #print ("i m here ")
        #print("f=",f.errors)
        if f.is_valid():
            #print("i m in form valid");
            name = request.POST.get('name', '')
            v = request.POST.get('vacation_plan', '')
            visa = request.POST.get('visa_status', '')
            remove_list=request.POST.getlist('selectto','')
            #print("remove=",remove_list)
            if global_people_name!=name:
                print("i m at update name")
                model1=detail_model.objects.filter(emp_name=global_people_name).update(emp_name=name)
                people_name=name

           #People_info = detail_model.objects.filter(emp_name="rohit")
           # print("people=", People_info)
            #People_data = {"People_details": People_info}
            ##model_data=[str(i.Act_name) for i in People_data["People_details"]]
           # print("model=",model_data)
            for i in remove_list:
                detail_info = detail_model.objects.filter(emp_name=people_name,Act_name=i)
               # print ("detail_info",detail_info.values())
                if detail_info !=None :
                   # print("i m at detail_info")
                    model1=detail_model.objects.filter(emp_name=people_name, Act_name=i)
                    #print("model1=",model1.values())
                    model1.delete()
            add_list = request.POST.getlist('selectfrom', '')
           # print("add_list=",add_list)
            for j in add_list:
                People_info = detail_model.objects.filter(emp_name=people_name,Act_name=j)
                #print("People_info",People_info.values())
                if People_info:
                    pass
                else:
                    if j!="Remove-Activity":
                        #print ("i m in elseeeeeeeeeeeee")
                        model2=detail_model(emp_name=people_name,Act_name=j)
                        model2.save()
           # People_act = detail_model.objects.filter(emp_name='rohit',Act_name='xyz').delete()
            People_del = People_model.objects.filter(name=global_people_name).delete()
           # print ("people_act=",People_act)
            #print("visa=", visa);
            #print('vacation=', v);
            model = People_model(name=name, vacation_plan=v, visa_status=visa)
            model.save()
            #print("out of box");
        #return render(request, 'project.html', {'form': f})
        return redirect('/home')

@csrf_exempt
def Remove_Activity_people_detail(request):
    Activity_type_info =detail_model.objects.filter(emp_name=global_people_name)
   # print("act=",Activity_type_info)
    Activity_type_data = {"Activity_type_details": Activity_type_info}

    return HttpResponse(json.dumps({i.id: str(i. Act_name) for i in Activity_type_data["Activity_type_details"]}),
                        content_type="application/json")


@csrf_exempt
def Add_Activity_people_detail(request):
    d=detail_model.objects.filter(emp_name=global_people_name)
    d_data={"d-type":d}
    k=[str(j.Act_name) for j in d_data["d-type"] ]
    #print ("k=",k)
    Activity_type_info =Activity_model.objects.filter().exclude(Activity_Name__in= k)
    #print("act=",Activity_type_info)
    Activity_type_data = {"Activity_type_details": Activity_type_info}

    return HttpResponse(json.dumps({i.Activity_Id: str(i. Activity_Name) for i in Activity_type_data["Activity_type_details"]}),
                        content_type="application/json")

def Activity_detail(request,Activity_name):
    f = Activity_detail_form
    global global_Activity_name
    global_Activity_name = Activity_name
   # print("i m in before if block");
    #print("request", request.method);
    if request.method == "GET":
        #print("i m n method")
        Activity_info = Activity_model.objects.filter(Activity_Name=Activity_name)
        #print("activity=", Activity_info)
        Activity_data = {"Activity_details": Activity_info}
        return render(request, 'Activity_detail.html', Activity_data)
    else:
        f = Activity_detail_form(request.POST)
       # print("i m here ")
        #print("f=", f.errors)
        if f.is_valid():
           # print("i m in form valid");
            name = request.POST.get('Activity_Name', '')
            type = request.POST.get('Activity_type', '')
            customer_name = request.POST.get('customer', '')
            description = request.POST.get('Description', '')
            s=request.POST.get('Activity_state',"off")
            #print("state=",s)
            if s=="on":
                state="1"
            else:
                state="0"
            if 'Activity_state' in request.POST:
               print("actvity_state=",state)
            else:
                print ("i m at false")
                print("actvity_state=", state)

            remove_list = request.POST.getlist('selectto', '')
            #print("remove=", remove_list)

            # People_info = detail_model.objects.filter(emp_name="rohit")
            # print("people=", People_info)
            # People_data = {"People_details": People_info}
            ##model_data=[str(i.Act_name) for i in People_data["People_details"]]
            # print("model=",model_data)
            if global_Activity_name!=name:
                detail_info = detail_model.objects.filter(Act_name=global_Activity_name).update(Act_name=name)
                Activity_name=name

            for i in remove_list:
                detail_info = detail_model.objects.filter(emp_name=i, Act_name=Activity_name)
                #print("detail_info", detail_info.values())
                if detail_info != None:
                    #print("i m at detail_info")
                    model1 = detail_model.objects.filter(emp_name=i, Act_name=Activity_name)
                    #print("model1=", model1.values())
                    model1.delete()
            add_list = request.POST.getlist('selectfrom', '')
            #print("add_list=", add_list)
            for j in add_list:
                People_info = detail_model.objects.filter(emp_name=j, Act_name=Activity_name)
                #print("People_info", People_info.values())
                if People_info:
                    pass
                else:
                    if j != "Remove-People":
                        #print("i m in elseeeeeeeeeeeee")
                        model2 = detail_model(emp_name=j, Act_name=Activity_name)
                        model2.save()
                        # People_act = detail_model.objects.filter(emp_name='rohit',Act_name='xyz').delete()
            Activity_del = Activity_model.objects.filter(Activity_Name=global_Activity_name).delete()
            # print ("people_act=",People_act)
           # print("visa=", visa);
            #print('vacation=', v);
            model =  model=Activity_model(Activity_Name=name,Activity_type=type,Customer_name=customer_name,Description=description,state=state)
            model.save()
            #print("out of box");
        # return render(request, 'project.html', {'form': f})
        return redirect('/home')


@csrf_exempt
def Remove_people_detail(request):
    pepole_type_info =detail_model.objects.filter(Act_name=global_Activity_name)
    #print("people=",pepole_type_info)
    people_type_data = {"people_type_details": pepole_type_info}

    return HttpResponse(json.dumps({i.id: str(i. emp_name) for i in people_type_data["people_type_details"]}),
                        content_type="application/json")
@csrf_exempt
def Add_people_detail(request):
    d=detail_model.objects.filter(Act_name=global_Activity_name)
    d_data={"d-type":d}
    k=[str(j.emp_name) for j in d_data["d-type"] ]
    #print ("k=",k)
    people_type_info =People_model.objects.filter().exclude(name__in= k)
    #print("people=",people_type_info)
    people_type_data = {"people_type_details": people_type_info}

    return HttpResponse(json.dumps({i.Id: str(i. name) for i in people_type_data["people_type_details"]}),
                        content_type="application/json")


@csrf_exempt
def delete_people_detail(request,name):
    d=detail_model.objects.filter(emp_name=name).delete()
    #print("i m here")
    p=People_model.objects.filter(name=name).delete()
    return HttpResponse()


@csrf_exempt
def delete_activity_detail(request,act_name):
    d=detail_model.objects.filter(Act_name=act_name).delete()
    #print("i m here")
    p=Activity_model.objects.filter(Activity_Name=act_name).delete()
    return HttpResponse()


