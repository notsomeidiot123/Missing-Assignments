
from studentvue import StudentVue
import os
import time


path = input("Enter the path of the file you want to place your data in: ")

user = input("Enter your ID No: ")

passw = input("Enter your password: ")
start_time = time.time();
print("Extracting data from studentvue...");
sv = StudentVue(user, passw, "https://md-mcps-psv.edupoint.com/")

f = open(path, "w");
# f.write(str(sv.get_gradebook()["Gradebook"]["Courses"]["Course"]));

gradebook = sv.get_gradebook();

print("Done... Processing\n");

os.system("cls");
# for key, value in sv.get_student_info()["StudentInfo"].items():
#     if(key == "FormattedName" or key == "Gender " or key == "PermID"):
#         print(value["$"]);
string = ""
i: int = 0;
# try:
for key in gradebook["Gradebook"]["Courses"]["Course"]:
    print(key["@Period"])
    for keyy, value in key["Marks"]["Mark"]["Assignments"].items():
        if("Assignment" in keyy):
            for asign in key["Marks"]["Mark"]["Assignments"]["Assignment"]:
                if("Missing" in str(asign["@Notes"])):
                    print("Missing")
                    # string += "Period: " + key["@Period"] + "\n" + "\t Name:" + key["@Measure"] + "\n\t Points:" + key["@Points"]
                    string += str.format("Period: {}\n\t Name: {}\n\t Points: {}\n", key["@Period"], asign["@Measure"], asign["@Points"])
                    # f.write(string)
# except:
#     print("Error")
f.write(string);
print(f"Time: {round(time.time()-start_time, 2)} seconds")
print("The data has been placed into the file "+path)
input("Press enter to close");