array_size = 5
stack_size = 7
top = -1
stack = []

def createArray(stack):
    array = []
    stack.append(array)
    return stack


def push(stack, id):
    global top
    global stack_size
    global array_size
    
    if (top==-1):
        stack = createArray(stack)
        stack[top+1].append(id)
        top += 1
        return stack
    else:
        print(stack)
        if (len(stack[top]) < array_size):
            stack[top].append(id)
            stack[top] = QuickSort(stack[top])
            return stack
        else:
            if (top != stack_size-1):
                stack = createArray(stack)
                stack[top+1].append(id)
                top += 1
                return stack
            else:
                print("Stack is full")

    

def pop(stack):
    global top
    if (top==-1):
        print("Stack is empty")
    else:
        stack[top].pop()
        if (len(stack[top]) == 0):
            stack.pop()
            top -= 1
            return stack

def QuickSort(arr):

    elements = len(arr)
    
    if elements < 2:
        return arr
    
    current_position = 0 
    type_of_element = type(arr[0])

    if (type_of_element == int):
        for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    else:
        for i in range(1, elements): 
         if ord(arr[i]) <= ord(arr[0]):
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp


    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = QuickSort(arr[0:current_position]) 
    right = QuickSort(arr[current_position+1:elements]) 

    arr = left + [arr[current_position]] + right 
    
    return arr

def Search(stack, id):
    for i in range(len(stack)-1, -1, -1):
        if (id > stack[i][-1]):
            continue
        else: 
            if (id in stack[i]):
                return True
    return False
def getStack(stack):
    return stack
def display(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("\n")

# push(stack, 2)
# # display(stack)
# push(stack, 8)
# # display(stack)
# push(stack, 5)
# # display(stack)
# push(stack, 10)
# # display(stack)
# push(stack, 1)
# # display(stack)
# push(stack, 15)
# # display(stack)
# push(stack, 11)
# # display(stack)
# pop(stack)
# # display(stack)
# pop(stack)
# display(stack)
# print(Search(stack, 8))


# push(stack, "a")
# display(stack)
# push(stack, "z")
# display(stack)
# push(stack, "c")
# display(stack)
# push(stack, "t")
# display(stack)
# push(stack, "y")
# display(stack)
# push(stack, "h")
# display(stack)
# pop(stack)
# display(stack)
# pop(stack)
# display(stack)




