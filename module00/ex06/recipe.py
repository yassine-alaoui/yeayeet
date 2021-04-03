MENU = """
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
"""

Cookbook = {
	"sandwich" : {
		"ingredients" : ["khobz", "mayoniz", "ton"],
		"meal" : "to be taken seriously",
		"prep_time" : 5
	},
	"cake" : {
		"ingredients" : ['flour', 'sugar', 'eggs'],
		"meal" : "To be eaten for dessert.",
		"prep_time" : 60
	},
	"salad" : {
		"ingredients" : ["khyar", "khizo", "fried btata", "zit l3od", "manyonizz"],
		"meal" : "to be taken before sleep(12AM)",
		"prep_time" : 7
	}
}

def	delete_meal():
	meal_name = input("Please enter the recipe's name to delete:\n>> ")
	if not Cookbook.get(meal_name):
		print("What are you talking about ??")
	else:
		Cookbook.pop(meal_name)
		print("The recipe %s has been deleted" % meal_name)


def	add_meal():
	meal_name = input("Please enter the recipe's name to add:\n>> ")
	if Cookbook.get(meal_name):
		print("I already know how to cook that")
	else:
		Cookbook[meal_name] = {"ingredients" : [],"meal" : "", "prep_time" : 0}
		Cookbook[meal_name]["ingredients"] = input("Enter the ingredients separated by ','\n>> ").split(",")
		Cookbook[meal_name]["meal"] = input("Enter the type of meal\n>> ")
	
		while Cookbook[meal_name]["prep_time"] <= 0:
			Cookbook[meal_name]["prep_time"] = input("entre the time to prepare the meal\n>> ")
			Cookbook[meal_name]["prep_time"] = int(Cookbook[meal_name]["prep_time"]) if Cookbook[meal_name]["prep_time"].isdigit() else 0
		print("The recipe %s is added to the cookbook" % meal_name)

def print_meal():
	meal_name = input("Please enter the recipe's name to get its details:\n>> ")
	meal = Cookbook.get(meal_name)
	if not meal:
		print("I don't know how to make %s ^^" % meal_name)
	else:
		print ("Recipe for %s:" % meal_name)
		print ("Ingredients list: %s" % str(meal["ingredients"]))
		print (meal["meal"])
		print ("Takes %d minutes of cooking." % meal["prep_time"])

def	print_cookbook():
	print("I Can show you how to cook : %s" % [meal for meal in Cookbook])


def exitCookbook():
	print("Cookbook closed.")
	exit(0)


functions = {1 : add_meal, 2 : delete_meal, 3 : print_meal, 4 : print_cookbook, 5:exitCookbook}
print(MENU)
while 1:
	read = input(">> ")
	if read.isdigit() and functions.get(int(read)):
		functions.get(int(read))()
		#print(MENU)
	else:
		print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")

		