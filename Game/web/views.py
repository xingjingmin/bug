from django.shortcuts import render,get_object_or_404
from .models import Student,State
from .forms import StudentForm,StateForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage
# Create your views here.

def index(request):
    all_list=Student.objects.all()
    paginator=Paginator(all_list,2)#
    page_num=request.GET.get('page',default='1')
    try:
        page=paginator.page(page_num)
        page_list = page.object_list
    except PageNotAnInteger:
        page=paginator.page(1)
        page_list = page.object_list
    except EmptyPage as e:
        print('EmptyPage:{}'.format(e))
        page=paginator.page(paginator.num_pages)
        page_list = page.object_list
        if int(page_num)>paginator.num_pages:
            page=paginator.page(paginator.num_pages)
            page_list = page.object_list
        else:
            page=paginator.page(1)
            page_list = page.object_list
    if int(page_num)<6:
        if paginator.num_pages<=10:
            dis_range=range(1,paginator.num_pages+1)
        else:
            dis_range=range(1,11)
    elif (page_num>=6) and (page_num<=paginator.num_pages-5):
        dis_range=range(paginator.num_pages-9,paginator.num_pages+1)

    name_list=[choice[1] for choice in Student.Name]
    return render(request,'web/index.html',context={'page_list':page_list,'page':page,'name_list':name_list,'dis_range':dis_range})

def Modfy(request,student_id):
    student=get_object_or_404(Student,pk=student_id)
    state=student.state_set.get(username=student)
    if request.method == 'POST':
        form=StudentForm(instance=student,data=request.POST)
        sform=StateForm(instance=state,data=request.POST)
        if form.is_valid():
            s=form.save(commit=False)
            form.save()
            a= sform.save(commit=False)
            a.username=s
            a.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form=StudentForm(instance=student)
        sform=StateForm(instance=state)
        return render(request,'web/modfy.html',{'form':form,'sform':sform,'student':student})

def Add(request):
    if request.method=='POST':
        st=StudentForm(request.POST)
        sa=StateForm(request.POST)
        if st.is_valid()and sa.is_valid():

            form=st.save(commit=False)#
            st.save()
            dform=sa.save(commit=False)
            dform.username=form
            sa.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        st=StudentForm()
        sa=StateForm()
    return render(request,'web/add.html',{'st':st,'sa':sa})

def Dele(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))

