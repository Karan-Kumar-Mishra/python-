#namespacing
memory=2000
def AddMemory():
    global memory
    memory=memory+1

print(memory)
AddMemory()
print(memory)
