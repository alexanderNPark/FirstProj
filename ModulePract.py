
#from math import pi
from first.Module1Created import *
from fileinput import *
b=promptNumber();
list1 = [1,2,b];
print("Before:",address(list1));
c = promptNumber();
list1.append(c);
print("After:",address(list1));
fileName = r"c:\pyCharm_WS\first\testFile.txt";
file = open(fileName,'a');
i=130;
end =10
print(list(range(end)))
for i in range(end):
    if(i>5):
        file.write("\n");
        i=i+i*end;
    file.write(str(i)+" ");
file.close();










