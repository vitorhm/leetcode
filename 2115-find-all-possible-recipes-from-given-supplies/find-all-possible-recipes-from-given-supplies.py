class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        already_saw = set()
        recipes_map = {}

        for i in range(len(recipes)):
            recipes_map[recipes[i]] = ingredients[i]

        recipes_made = set()

        def find_ingredient(recipe: str, ingredients: List[str]) -> bool:
            if recipe in recipes_made:
                return True

            if recipe in already_saw:
                return False

            already_saw.add(recipe)

            for ingredient in ingredients:
                if ingredient in recipes:
                    have_all = find_ingredient(ingredient, recipes_map[ingredient])
                    if have_all:
                        recipes_made.add(ingredient)
                    else:
                        return False
                elif ingredient not in supplies:
                    return False

            return True

        for r in range(len(recipes)):
            recipe = recipes[r]
            ingredient_arr = ingredients[r]

            if find_ingredient(recipe, ingredient_arr):
                recipes_made.add(recipe)

        return list(recipes_made)