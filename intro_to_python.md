# Python exercises
Sophia Stoll, assigned 08.11.2024

## 1

```python
print ("Hello World!")

my_text = "Hello World!"
print(my_text)
```

## 2

```python
glass_of_water = 5
glass_of_water = glass_of_water + 1
print("I drank" glass_of_water "glasses of water today.")
```

## 3

```python
men_stepped_on_the_moon = 12
print(men_stepped_on_the_moon)

my_reason_for_coding = "science"
print(my_reason_for_coding)


global_mean_sea_level_2018 = 21
global_mean_sea_level_2018 = 21.00
print(global_mean_sea_level_2018)

```

## 9
### 9a
```python
str = "It's always darkest before dawn."
print(str)
```

### 9b
```python
ans = str[0]+str[1]+str[-1]
print(ans)
```

### 9c
```python
str="It's always darkest before dawn."
str.replace(".", "!")
print(str)
```

## 10
### 10a
```python
lst=[11, 10, 12, 101, 99, 1000, 999]
answer_1 = len(lst)
print(answer_1)
```

### 10b
```python
msg="Be yourself, everyone else is taken."
msg_length = len(msg)
print(msg_length)
```

### 10c
```python
dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
ans_1 = len(dict)
print(ans_1)
```

## 11
### 11a
```python
lst=[11, 100, 99, 1000, 999]
lst.sort()
print(lst)
```

### 11b
```python
lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
lst.sort()
print(lst)
```

### 11c
```python
lst=[11, 100, 99, 1000, 999]
lst.sort(reverse = True)
print(lst)
```

## 12
### 12a
```python
lst=[11, 100, 99, 1000, 999]
popped_item = lst.pop(-1)
print(popped_item)
print(lst)
```

### 12b
not using .index
```python
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
item = lst.pop(-2)
print(lst, item)
```

### 12c
```python
GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}

italy_gdp = GDP_2018.pop("Italy")

print(GDP_2018)
print("Italy:", italy_gdp, "trillion USD")

```

