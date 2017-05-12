from geopy.distance import vincenty
from ExamCreation.models import Exam, Center, ExamSlot, Vacant,City
from UserRegistration.models import StudentRequest,CenterAllocated


def AddCenter(center_name, city_name, state_name, lat, long, cap, exam_info):
    '''Add a center for given exam

    exam_info: name of the exam from Exam Table
    '''
    temp_id = Exam.objects.get(name=exam_info)
    temp_id.center_set.create(name=center_name, city=city_name, state=state_name, latitude=lat, longitude=long,
                              capicity=cap)


def GetDistance(lat1, lng1, lat2, lng2):
    source = (lat1, lng1)
    destination = (lat2, lng2)
    return vincenty(source, destination).kilometers


def GetCenterList(city_name, lat1, lng1):
    max_distance = 5
    tmp_center = Center.objects.filter(city__iexact=city_name)
    while max_distance <= 60:
        tmp_list = []
        for center in tmp_center:
            tmp_distance = GetDistance(center.latitude, center.longitude, lat1, lng1)
            center.distance = tmp_distance
            if center.distance <= max_distance:
                tmp_list.append(center)

        if tmp_list:
            return sorted(tmp_list, key=lambda x: x.distance)
        else:
            max_distance += 5


def AllocateCenter(tmpslotid, city_name, lat1, lng1):
    center_list = GetCenterList(city_name, lat1, lng1)
    for center in center_list:
        try:
            tmp_center = Vacant.objects.filter(slotid=tmpslotid).filter(centerid=center)[0]
            print(tmp_center)
            if tmp_center.avl_seats > 0:
                tmp_center.avl_seats -= 1
                tmp_center.save()
                return tmp_center.centerid
        except:
            pass
    return -1



def AllocateCenterUpdate(tmpslotid,city_name,lat,lng):
    '''Get the list of all available centers in the city'''
    vacant_list = GetVacantCentersList(tmpslotid,city_name)
    '''Allocate a center based on locateion'''
    allocated_center =  GetAvlCenter(vacant_list,lat,lng)
    '''Update the total avl_seats in at a given centers'''
    status = UpdateCenterDetails(tmpslotid,allocated_center)
    return allocated_center



def GetVacantCentersList(tmpslotid,city_name):
    tmp_query_set = Center.objects.filter(city__name__iexact=city_name)
    vacant_center_list =[]
    for i in tmp_query_set:
        try:
            tmp_center = Vacant.objects.filter(slotid=tmpslotid).filter(centerid=i)[0]
            if tmp_center.avl_seats > 0:
                vacant_center_list.append(tmp_center)
        except:
            pass

    return vacant_center_list

def GetAvlCenter(vacant_center_list, student_lat, student_lng):
    max_distance = 5
    while max_distance < 50:
        centers_within_radius = []
        for i in vacant_center_list:
            '''calculate distance for each center in the list'''
            tmp_distance = GetDistance(i.centerid.latitude, i.centerid.longitude, student_lat, student_lng)
            i.centerid.distance = tmp_distance
            if tmp_distance <= max_distance:
                centers_within_radius.append(i.centerid)

        if centers_within_radius:
            allocated_center = sorted(centers_within_radius, key=lambda x: x.distance)[0]
            return allocated_center
        else:
            max_distance += 5



def UpdateCenterDetails(tmpslotid,center):
    try:
        tmp_ref =  Vacant.objects.filter(slotid=tmpslotid).filter(centerid=center)[0]
        tmp_ref.avl_seats -= 1
        tmp_ref.save()
        return 0
    except:
        return 0
def SetLatLng(tempcityobject,tempstudent):
    if tempstudent.latitude == 0 and tempstudent.longitude == 0:
        tempstudent.longitude = tempcityobject.def_long
        tempstudent.latitude =  tempcityobject.def_lat
        tempstudent.save()

    else:
        pass


def StartStudentAllocation(examname):
    student_list =  StudentRequest.objects.filter(slotid__examid__name=examname).filter(allocated=False)
    student_list = student_list.reverse()

    for tempstudent in student_list:
        city_list =  tempstudent.city.split()
        for tempcity in city_list:
            tempcityobject = City.objects.get(name=tempcity)
            SetLatLng(tempcityobject,tempstudent)
            status =  TmpAllocation(i=tempstudent,examname=tempstudent.slotid.examid ,slotid=tempstudent.slotid,
                     city=tempcityobject.name,long=tempstudent.longitude,lat=tempstudent.latitude)
            if status:
                return

        if status is not True:
                print("no center allocated")









def TmpAllocation(i,examname,slotid,city,long,lat):
    center =  AllocateCenterUpdate(slotid,city,long,lat)
    if center:
        CenterAllocated.objects.create(examname=examname,admitno=i,centerid=center)
        i.allocated = True
        i.save()
        return True

    else:
        return False





