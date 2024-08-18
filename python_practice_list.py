print('Q.1')
print()
names = ['Ali', 'Sara', 'Ahmed', 'Fatima']
for name in names:
    print(name)
print('#' * 100)
print()

print('Q.2')
print()
names = ['Ali', 'Sara', 'Ahmed', 'Fatima']
for name in names:
    print(f"Hello {name}, how are you today?")
print('#' * 100)
print()

print('Q.3')
print()
transportations = ['motorcycle', 'car', 'bicycle']
for transportation in transportations:
    print(f"I would like to own a Honda {transportation}.")
print('#' * 100)
print()

print('Q.4')
print()
guests = ['Albert Einstein', 'Marie Curie', 'Ada Lovelace']
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place!")

print('#' * 100)
print()

print('Q.5')
guests = ['Albert Einstein', 'Marie Curie', 'Ada Lovelace']
print(f"Unfortunately, {guests[1]} can't make it to dinner.")
guests[1] = 'Isaac Newton'
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner at my place!")
print('#' * 100)
print()

print('Q.6')
print()
guests = ['Albert Einstein', 'Isaac Newton', 'Ada Lovelace']
print("Great news! We found a bigger table for dinner.")
guests.insert(0, 'Nikola Tesla')
guests.insert(2, 'Galileo Galilei')
guests.append('Charles Darwin')
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place!")
print('#' * 100)
print()

print('Q.7')
print()
guests = ['Nikola Tesla', 'Albert Einstein', 'Galileo Galilei', 'Isaac Newton', 'Ada Lovelace', 'Charles Darwin']
print("Unfortunately, I can only invite two people to dinner.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")
del guests[0]
del guests[0]
print(guests)
print('#' * 100)
print()

print('Q.8')
print()
places = ['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome']
print("Original list:", places)
print("Alphabetical order:", sorted(places))
print("Original list again:", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Original list again:", places)
places.reverse()
print("Reversed list:", places)
places.reverse()
print("Original order restored:", places)
places.sort()
print("Alphabetically sorted list:", places)
places.sort(reverse=True)
print("Reverse alphabetically sorted list:", places)
print('#' * 100)
print()

print('Q.9')
print()
rivers = ['Nile', 'Amazon', 'Yangtze', 'Mississippi']
print("Original list:", rivers)
print("Sorted list:", sorted(rivers))
rivers.reverse()
print("Reversed list:", rivers)
rivers.sort()
print("Alphabetically sorted list:", rivers)
rivers.sort(reverse=True)
print("Reverse alphabetically sorted list:", rivers)
print('#' * 100)
print()

print('Q.10')
print()
mountains = ['Everest', 'K2', 'Kilimanjaro']
print(mountains[2]) 
print('#' * 100)