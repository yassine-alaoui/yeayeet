class Recipe:

	def	__init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
		if not name:
			print("Error\nName is empty")
			exit(1)
		self.name = name
		if not isinstance(name, str):
			print("Error\nName is not str")
			exit(1)
		if not cooking_lvl:
			print("Error\nCooking_lvl is empty")
			exit(1)
		self.cooking_lvl = cooking_lvl
		if not isinstance(Cooking_lvl, int):
			print("Error\nCooking_lvl is not int")
			exit(1)
		if not cooking_time:
			print("Error\nCooking_time is empty")
			exit(1)
		self.cooking_time = cooking_time
		if not isinstance(cooking_time, int):
			print("Error\nCooking_time is not int")
			exit(1)
		if not ingredients:
			print("Error\nIngredients is empty")
			exit(1)
		self.ingredients = ingredients
		if not isinstance(ingredients, list):
			print("Error\nIngredients is not list")
			exit(1)
		if not recipe_type:
			print("Error\rRecipe_type is empty")
			exit(1)
		self.recipe_type = recipe_type
		if not isinstance(recipe_type, str):
			print("Error\nRecipe_type is not str")
			exit(1)
		self.description = description
		if not isinstance(description, str):
			print("Error\nDescription is not str")
			exit(1)
	
	def __str__(self):
		txt = "The recipe is {}\nThe cooking_lvl {}\nThe cooking_time {}\nThe ingredients".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients)
		return txt

rec = Recipe("namzzze", 2,2)
print(rec)