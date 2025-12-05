import copy

def CopyCurrentObject(obj):
    return copy.copy(obj)

def RecursiveCopyObject(obj):
    return copy.deepcopy(obj)

def AddForEachElement(collection, value_to_add):
    for i, item in enumerate(collection):
        if isinstance(item, (int, float)):
            collection[i] = item + value_to_add
        elif isinstance(item, list):
            AddForEachElement(item, value_to_add)
        else:
            try:
                collection[i] = item + value_to_add
            except TypeError:
                # skip or handle other types
                pass
    return collection



if __name__ == "__main__":
    print("\nCHANGING ONLY THE COPIES:")
    print("\n\nSingular Object")
    obj = 123
    copied_obj = CopyCurrentObject(obj)
    copied_obj += 1
    deepcopied_obj = RecursiveCopyObject(obj)
    deepcopied_obj += 2
    print("\n\tOriginal :", obj)
    print("\n\tCopied + 1 :", copied_obj ,"\t\tSince it is a simple Object")
    print("\n\tRecursive Copied + 2 :", deepcopied_obj, "\t\tA recursive copy does exactly the same as a Copy")

    print("\n\nList Object")
    pointer_element = [3,4]
    obj_list = [1, 2, pointer_element, 5]
    copied_list = CopyCurrentObject(obj_list)
    AddForEachElement(copied_list, 1)
    deepcopied_list = RecursiveCopyObject(obj_list)
    AddForEachElement(deepcopied_list, 2)
    print("\n\tOriginal :", obj_list)
    print("\n\tCopied + 1 :", copied_list, "\t\tYou can notice this one didn't change the pointed variable")
    print("\n\tRecursive Copied + 2 :", deepcopied_list, "\t\tThis one changed the pointed variable")
    print("\n\nDESC:")
    print("\n\t Copy will only copy the given pointer to another memory location,\n\tbut the objects that that pointer point to are still the same.\n\tUse Recursive Copy to copy those too.\n\n")

