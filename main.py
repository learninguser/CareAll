from ElderFolk import ElderFolk
from YoungFolk import YoungFolk
from profile import User

elder1 = ElderFolk('e1', "Giridhar", 65, "seeker")
elder1.setFunds(10000)

elder2 = ElderFolk('e2', "Sridhar", 75, "seeker")
elder2.setFunds(10000)

elder3 = ElderFolk('e3', "Suresh", 60, "seeker")
elder3.setFunds(10000)

elder4 = ElderFolk('e4', "Naresh", 66, "seeker")
elder4.setFunds(10000)

elder5 = ElderFolk('e5', "Mohan", 71, "seeker")
elder5.setFunds(10000)

# elder6 = ElderFolk('e6', "Mohan Giridhar", 65, "seeker")
# elder6.setFunds(10000)

# elder7 = ElderFolk('e7', "Sunil Sridhar", 75, "seeker")
# elder7.setFunds(10000)

# elder8 = ElderFolk('e8', "Rao Suresh", 60, "seeker")
# elder8.setFunds(10000)

# elder9 = ElderFolk('e9', "Krishna Naresh", 66, "seeker")
# elder9.setFunds(10000)

# elder10 = ElderFolk('e10', "Suresh Mohan", 71, "seeker")
# elder10.setFunds(10000)

# elder11 = ElderFolk('e11', "Antony Giridhar", 65, "seeker")
# elder11.setFunds(10000)

# elder12 = ElderFolk('e12', "Mahesh Sridhar", 75, "seeker")
# elder12.setFunds(10000)

# elder13 = ElderFolk('e13', "Surendra", 60, "seeker")
# elder13.setFunds(10000)

# elder14 = ElderFolk('e14', "Nani", 66, "seeker")
# elder14.setFunds(10000)

# elder15 = ElderFolk('e15', "Mohit", 71, "seeker")
# elder15.setFunds(10000)

young1 = YoungFolk('y1','Pavan',27,'provider')
young2 = YoungFolk('y2','Harika',23,'provider')
young3 = YoungFolk('y3','Swetcha',20,'provider')
young4 = YoungFolk('y4','Krishna',24,'provider')
young5 = YoungFolk('y5','Sunil',27,'provider')

young1.register("abc@gmail.com","123456789")
young1.login("abc@gmail.com","123456789")

# elder1.setAvailabilty(False)
elder5.setAvailabilty(False)
# elder8.setAvailabilty(False)
# elder14.setAvailabilty(False)

res = young1.applyForService(elder2)
if res:
    elder2.setApproveFolk(True)
    if not young1.setOlideTakenCareOf(elder2):
        young1.setSalary(1000)
        elder2.setFunds(-1000)
        elder2.setAvailabilty(False)

res = young1.applyForService(elder1)
if res:
    elder1.setApproveFolk(True)
    if not young1.setOlideTakenCareOf(elder1):
        young1.setSalary(1000)
        elder1.setFunds(-1000)
        elder1.setAvailabilty(False)

res = young1.applyForService(elder3)
if res:
    elder3.setApproveFolk(True)
    if not young1.setOlideTakenCareOf(elder3):
        young1.setSalary(1000)
        elder3.setFunds(-1000)
        elder3.setAvailabilty(False)

res = young1.applyForService(elder5)
if res:
    elder5.setApproveFolk(True)
    if not young1.setOlideTakenCareOf(elder5):
        young1.setSalary(1000)
        elder5.setFunds(-1000)
        elder5.setAvailabilty(False)

res = young1.applyForService(elder4)
if res:
    elder4.setApproveFolk(True)
    if not young1.setOlideTakenCareOf(elder4):
        young1.setSalary(1000)
        elder4.setFunds(-1000)
        elder4.setAvailabilty(False)

print(young1.getOlideTakenCareof())
print(young1.getSalary())

res = young2.applyForService(elder4)
if res:
    elder4.setApproveFolk(True)
    if not young2.setOlideTakenCareOf(elder4):
        young2.setSalary(1000)
        elder4.setFunds(-1000)
        elder4.setAvailabilty(False)

print(young2.getOlideTakenCareof())
print(young2.getSalary())