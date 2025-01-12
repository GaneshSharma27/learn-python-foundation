# ------------------ Garbage collection ------------------
# Garbage collection is the process of automatically freeing up the memory
# by removing objects that are no longer used/referenced
# Python does this automatically, most of the time, so you don't need to worry about it


def createCycle():
    x = []          # creating an object x
    x.append(x)     # object x refering to itself, object x won't be freed automatically when function is returned
# this'll cause memory to be held onto until Python's garbage collector is invoked

createCycle()

# Making an object eligible for garbage collection
y = []
y.append(1)
y.append(2)
del y
print()

# -------------- Automatic garbage collection --------------
import gc
print("Garbage collection thresholds:", gc.get_threshold())     # threshold value is 700
# (number of allocations - number of deallocations) > threshold value ----> automatic garbage collector will run
print()

# -------------- Manual garbage collection --------------
# nice idea for handling memory being consumed by reference cycles
# Manual garbage collection allows you to trigger this process explicitly incase you want to clear up memory
# import gc         # already imported above
collected = gc.collect()        # `gc.collect()` scans objects that are unreachable & deletes them
print(f"Garbage collector: collected {collected} objects")      # `gc.collect()` also returns the number of unreachable objects
# that were collected and deleted

# Automatic garbage collection won't break reference cycle as it'll think that it's still in use
# Thus manual garbage collection helps in this, it breaks reference cycle and clears everything up

