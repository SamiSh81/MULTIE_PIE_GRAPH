import numpy as np
import matplotlib.pyplot as plt

# PIE (1)
name_sales_person=np.array(["PETER","HANS","LISA","NERMIN","MANOIL"])
sales_rate=np.array([22.5,31.7,20.3,25.2,23.1])
plt.subplot(2,2,1)
plt.style.use("bmh")
plt.title("SALES_PERSON",color="red")
plt.pie(
    sales_rate,labels=name_sales_person,explode=[0,0.1,0,0,0.1],radius=1,
    colors=["red","blue","yellow","pink","green"],rotatelabels=0,startangle=1,
    labeldistance=1.1,autopct="%1.0f%%",shadow=1
)

# PIE (2)
the_stages=np.array(["FIRST-STAGE","SECOND-STAGE","THIRD-STAGE","FOURTH-STAGE","FIFTH-STAG","SIXTH-STAGE","SIVENTH-STAGE"])
the_success_rate=np.array([8,7.5,6,7.3,5,9,9.7])
plt.subplot(2,2,2)
plt.title("THE_SUCCESS_RATE",color="green")
plt.pie(
    the_success_rate,labels=the_stages,explode=[0.1,0,0.1,0,0.1,0,0],
    labeldistance=1.2,radius=1,
    colors=["red","green","blue","yellow","gray","brown","pink"],
    startangle=1,rotatelabels=False,autopct="%1.0f%%",shadow=1,counterclock=0
)

# PLOT (3)
directions=np.array(["NORTH","SOUTH","WEST","EAST"])
average_school=np.array([13,20,33,11.5])
plt.subplot(2,2,3)
plt.pie(average_school,labels=directions,labeldistance=1.1,
    explode=[0.1,0.2,0,0],radius=1,startangle=1,
    colors=["red","gray","yellow","pink"],rotatelabels=False,counterclock=1,shadow=1,
    autopct="%1.0f%%")
plt.title("AVERAGE_SCHOOL",color="blue")

# PIE (4)
name_country=["GERMANY","GRACE","ASTERIA","FRANCE","HOLLAND"]
num_student=[220,90,100,177,165]
plt.subplot(2,2,4)
plt.title("INTERNATIONAL_STUDENTS",color="orange")
plt.pie(
    num_student,labels=name_country,labeldistance=1.1,
    explode=[0,0,0,0,0],radius=1,startangle=1,
    colors=["green","brown","yellow","blue","pink"],
    rotatelabels=False,    autopct="%1.0f%%"
)

plt.show()
