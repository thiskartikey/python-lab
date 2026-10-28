task_list = []

while True:
    print("\n--- TASK SCHEDULER ---")
    print("1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    option = input("Enter your choice: ").strip()

    # Add a new task
    if option == "1":
        title = input("Enter task name: ")
        urgency = input("Enter priority (high/low): ").strip().lower()
        is_ready = input("Is the task ready? (yes/no): ").strip().lower()
        task_list.append([title, urgency, is_ready])
        print("Task added successfully.")

    # Execute runnable tasks using lazy evaluation
    elif option == "2":
        if not task_list:
            print("No tasks in the queue.")
            continue

        print("\nRunning tasks...")
        pending_list = []
        for task in task_list:
            t_name, t_priority, t_ready = task[0], task[1], task[2]

            # Short-circuit / lazy evaluation with AND / OR
            if (t_ready == "yes" and t_priority == "high") or (t_ready == "yes" and t_priority == "low"):
                print("Executing:", t_name)
            elif t_ready != "yes":
                print("Skipping:", t_name, "- Task is not ready.")
                pending_list.append(task)
            else:
                print("Skipping:", t_name)

        task_list = pending_list

    # Show pending tasks
    elif option == "3":
        if not task_list:
            print("No tasks in the queue.")
        else:
            print("\nPending Tasks:")
            for item in task_list:
                print("Task:", item[0], "| Priority:", item[1], "| Ready:", item[2])

    # Exit scheduler
    elif option == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice. Please try again.")
