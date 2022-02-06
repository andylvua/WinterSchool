# WinterSchool
**This is a repository for university winter school projects with Zenoviy Veres**

> Contributed: [Oles Pasirskyi](https://github.com/wertylu)
## Fish Shop. Lesson 1-3

> Fish Shop classes diagram. Created with [diagrams.net](https://www.diagrams.net/) using UML language.
>
>![](FishShop.drawio.png)

**To find project code, please see [FishShop.py](FishShop.py) file.**
> :warning: This program requires ```inflect``` module installation. Installation instructions is provided below.
> 
> To check actual working version for this module please see [required_modules.txt](required_modules.txt).
> 
> Remember, you could always use ```pip install -r required_modules.txt``` to automatically install required version of all modules that are used in project.

<br /> 
<br /> 

**Manual ```Inflect``` module installation:**
> :exclamation: Installing to your IDE. If you want to install it systemwide or just having some troubles please visit [docs.python.org](https://docs.python.org/3/installing/index.html)
>
> 
> In your environmental terminal type **```pip install inflect==<version>```**.
> 
> Notice, sometimes, you'll need to use ```pip3``` instead of ```pip```.


<br /> 
<br /> 

**Pay attention, that you can set your desired sorting order and sorting key at the end of the program.**
``` python
    FishShop.sorting_reverse = True 
```
_**True**_ stands for a decreasing order sort, _**False**_ stands for an increasing order sort.
``` python
    FishShop.sorting_key = "name" 
```
**Here**, please enter what will be the sorting key.

<br /> 

> :warning: The only allowed values for **sorting_key** are **_name_**, **_price_** and **_weight_**. 
> 
> Otherwise, the program will raise **ValueError**.

## Clouds. Lesson 4

> Cloud structure diagram. Represents simple explanation of how servers work and how they are managed.
>
>![](Cloud.drawio.png)

## Homework #1. Film studio
> Film studio management program structure diagram (variant 33). Created with [diagrams.net](https://www.diagrams.net/) for homework assignment.
>
>![](/Homework/HomeWork.drawio.png)
