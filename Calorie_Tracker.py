import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

CAL_GOAL = 2000
PROTEIN_GOAL = 150
FAT_GOAL = 100
CARBS_GOAL = 500

today = []

done = False
while not done:
    print("""
    1. Add new food
    2. Visualize Progress
    3. Exit
    """)
    ch = input("Choose an option ==> ")

    if ch == "1":
        print("Adding new food!")
        name = input("Name ==> ")
        calories = int(input("Calories ==> "))
        protein = int(input("Protein ==> "))
        fat = int(input("Fat ==> "))
        carbs = int(input("Carbs ==> "))
        food = Food(name, calories, protein, fat, carbs)
        today.append(food)
        print("Added a new food!")
    
    elif ch == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fat_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)
        
        fig, axes = plt.subplots(2, 2, figsize=(9, 6))
        
        # Plotting macronutrients distribution
        labels = ['Protein', 'Fats', 'Carbohydrates']
        sizes = [protein_sum, fat_sum, carbs_sum]
        explode = (0.1, 0.1, 0.1)  
        axes[0, 0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
        axes[0, 0].set_title("Macronutrients Distribution")
        
        # progress
        bars = axes[0, 1].bar(np.arange(len(labels)), [protein_sum, fat_sum, carbs_sum], width=0.4, label='Consumed')
        goal_bars = axes[0, 1].bar(np.arange(len(labels)) + 0.4, [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4, label='Goal')
        axes[0, 1].set_title("Macronutrients Progress")
        axes[0, 1].set_xticks(np.arange(len(labels)) + 0.2)
        axes[0, 1].set_xticklabels(labels)
        axes[0, 1].legend()
        
        # calories goal progress
        labels = ['Calories', 'Remaining']
        sizes = [calorie_sum, CAL_GOAL - calorie_sum]
        axes[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=['lightcoral', 'lightskyblue'])
        axes[1, 0].set_title("Calories Goal Progress")
        
        # calories goal over time
        axes[1, 1].plot(np.cumsum([food.calories for food in today]), label="Calories Eaten", marker='o', linestyle='-')
        axes[1, 1].plot([CAL_GOAL] * len(today), label="Calorie Goal", linestyle='--')
        axes[1, 1].legend()
        axes[1, 1].set_title("Calories Goal Over Time")
        axes[1, 1].set_xlabel("Days")
        axes[1, 1].set_ylabel("Calories")
        
        fig.tight_layout()
        plt.show()
    
    elif ch == "3":
        done = True
    
    else:
        print("Invalid Choice")