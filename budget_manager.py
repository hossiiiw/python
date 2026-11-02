def budget_manager(initials_budget):
  budget = initials_budget

  def manage(action , amount=0):
    nonlocal budget

    if action == "add" :
      budget += amount
      print(f"you add {amount} to budget \nyour budget is : {budget}")
    elif action == "spend":
      if budget < amount :
        print(f"your budget is not enough \nyou have {budget} but you want {amount}")
      else :
        budget -= amount
        print(f"you spend : {amount} and your budget is : {budget}")
    elif action == "get":
      print(f"your budget is : {budget}")

    else:
      print("unvalid operation")
      return

  return manage


my_budget = budget_manager(1000)

my_budget("add" , 4000)
my_budget("spend" , 3000)
my_budget("get")
my_budget("spend" , 4000)

