import requests

def recipe_search(ingredient, cuisineType, mealType):
    # create the url depending on the input - to run the code need to enter the app_id and app_key
    app_id = #'a7a2b7d3'
    app_key = #'79bce97d4c2ecdbf692c3e9680cfd7fc'
    api_request = 'https://api.edamam.com/search?app_id={}&app_key={}'.format(
    app_id, app_key)
    if ingredient:
        api_request += '&q={}'.format(ingredient)
    if cuisineType:
        api_request += '&cuisineType={}'.format(cuisineType)
    if mealType:
        api_request += '&mealType={}'.format(mealType)
    # request hits from api
    result = requests.get(api_request)
    data = result.json()
    return data['hits']

def recipe_sort(to_sort):
    # sort the results by health labels (dietary requirements)
    recipes_by_cuisine_and_diet = {}
    for recipe in to_sort:
        dietary_needs = recipe["recipe"]["healthLabels"]
        for need in dietary_needs:
            if need not in recipes_by_cuisine_and_diet:
                recipes_by_cuisine_and_diet[need] = [recipe]
            else:
                recipes_by_cuisine_and_diet[need].append(recipe)

    return recipes_by_cuisine_and_diet

def run():
    # get the input required to run the function
    ingredient = input('Enter an ingredient: ')
    cuisineType = input('Enter a cuisine type or press enter to skip: ')
    mealType = input('Enter a meal type (ie. breakfast, lunch, dinner, snack) or press enter to skip: ')
    results = recipe_search(ingredient, cuisineType, mealType)
    sorted_results = recipe_sort(results)

    # print the results out nicely
    for need, recipes in sorted_results.items():
        print(f"  {need}:")
        for recipe in recipes:
            print(f"    {recipe['recipe']['label']}")
            print(f"    {recipe['recipe']['url']}")
            print()

run()