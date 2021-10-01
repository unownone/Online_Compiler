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
    if language =='python':
        with open(f'codes/python/{id}.py','w') as file:
            file.write(code)
        return runPython(id,args=arguments)
    elif language =='cpp':
        with open(f'codes/cpp/{id}.cpp','w') as file:
            file.write(code)
        return runCpp(id,args=arguments)
    elif language =='c':
        with open(f'codes/c/{id}.c','w') as file:
            file.write(code)
        return runC(id,args=arguments)
    elif language =='java':
        with open(f'codes/java/{id}.java','w') as file:
            file.write(code)
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
