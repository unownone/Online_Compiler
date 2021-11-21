from subprocess import Popen,PIPE
import time
#########Provides helper functions to compile and return
#########different codes , can be hotplugged with performance 
#########metrics and other things
#########Pass the filename with arguments if any as a string 
######### The Argument needs to be in a string with multiline input 
######### being separated by an \n or newline escape character
import os
def main(code,language,id,arguments=None):
    if language =='Python':
        path = 'codes/python/'
        if not os.path.exists(path): os.makedirs(path)

        with open(path+str(id)+'.py','w') as file:
            file.write(code)
            time.sleep(1)
        return runPython(id,args=arguments)
    elif language =='C++':
        path = 'codes/cpp/'
        if not os.path.exists(path): os.makedirs(path)

        with open(path+str(id)+'.cpp','w') as file:
            file.write(code)
            time.sleep(1)
        return runCpp(id,args=arguments)
    elif language =='C':
        path = f'codes/c/'
        if not os.path.exists(path): os.makedirs(path)

        with open(path+str(id)+'.c','w') as file:
            file.write(code)
            time.sleep(1)
        return runC(id,args=arguments)
    elif language =='Java':
        path = f'codes/java/'
        if not os.path.exists(path): os.makedirs(path)
        with open(path+str(id)+'.java','w') as file:
            file.write(code)
            time.sleep(1)
        return runJava(id,args=arguments)


def runPython(filename,args=''):
    process = Popen(['python','codes/python/'+filename+'.py'],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')

def runJava(filename,args=''):
    process = Popen(['javac','codes/java/'+filename+'.java'],stdin=PIPE,stdout=PIPE)
    process = Popen(['java','codes/java/'+filename+'.java'],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')

def runCpp(filename,args=''):
    process = Popen(['g++',f'codes/cpp/{filename}.cpp','-o',f'codes/cpp/{filename}'],stdin=PIPE,stdout=PIPE)
    out = f'./codes/cpp/{filename}'
    time.sleep(1)
    process = Popen([out],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')

def runC(filename,args=''):
    process = Popen(['gcc',f'codes/c/{filename}.c','-o',f'codes/c/{filename}'],stdin=PIPE,stdout=PIPE)
    out = f'./codes/c/{filename}'
    time.sleep(1)
    process = Popen([out],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')
