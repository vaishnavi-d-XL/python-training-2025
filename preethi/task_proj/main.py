from task import add_task,remove_task,display_task
def main():
    print("Task manager App")
    display_task()
    print(add_task("Develop"))
    print(add_task("Write Unit Test"))
    print(add_task("Deploy"))
    display_task()
    print(remove_task(0))
    display_task()
    print(remove_task(0))
    display_task()
    print(remove_task(0))
    display_task()
    print(remove_task(0))
if __name__=="__main__":
    main()



