Title: Java Language Notes
Date: 2016-01-16 10:20
Category: Java


## History
Java was developed by a team led by James Gosling at Sun Microsystems. Originally called Oak, it was designed in 1991 for use in embedded chips in consumer electronic appliances. In 1995, renamed Java, it was redesigned for developing Internet applications.


## Syntax

```Java
/*
File: Welcome.java
*/
public class Welcome {
  public static void main(String[] args) {
    // Display message Welcome to Java! to the console
    System.out.println("Welcome to Java!");
  }
}
```
* Every java program must have at least one class
* The program is executed from the `main` method
* Every statement in Java ends with a semicolon
* // starts line comment
* /* */ for block comment
* {} in a program forms a `block`, `class block`, `method block`
* Java is case sensitive
* java classes are grouped into `packages`


```
import javax.swing.JOptionPane;

public class WelcomeInMessageDialogBox {
  public static void main(String[] args) {
    JOptionPane.showMessageDialog(null, "Welcome to Java!");
  }
}
```

### Import
The import statement simply tells the compiler where to locate the classes. The information for the classes in an imported package is not read in at compile time or runtime unless the class is used in the program.

* specific import and wildcard import

```
import javax.swing.JOptionPane;
```

```
import javax.swing.*;
```

All the classes in the `java.lang` package are **implicitly** imported in every java program.

`System` is in the `java.lang` package.



### How to run

* Compile java source code to java bytecode first
* java bytecode runs on Java Virtual Machine (JVM)

## Date types

### primitive data types

* integers
* floating point numbers
* characters
* Boolean types

```
public class ComputeArea {
  double radius;
  double area;
  
  radius = 20;
  area = radius * radius * 3.14159;
  
  System.out.println("The area for the circle of radius " +
    radius + " is " + area);
  }
}
```
+ is also string concatenation operator, if on of the operands is nonstring, the nonstring value is converted into a string and concatenated with the other sring.
 
### read input

```
Scanner input = new Scanner(System.in);
```

Methods of `Scanner` objects:

* nextByte()
* nextShort()
* nextInt()
* nextLong()
* nextFloat()
* netDouble()
* next()      reads a string that ends before a whitespace character
* nextLine()

```
import java.util.Scanner;

public class ComputeAreaWithConsoleInput {
  public static void main(String[] args) {
  Scanner input = new Scanner(System.in);
  
  System.out.print("Enter a number for radius: ");
  
  double radius = input.nextDouble();
  
  double area = radius * radius * 3.14159;
  
  System.out.println("The area for the circle of radius " +
    radius + " is " + area);
  }
}
```

## Identifiers

* letters, digits, underscores and dollar signs is allowed in identifier
* starts with _, $ or digit
* case sensitive


## Variables

variable declarations

```
int i, j, k;
int i = 1;
int i = j = k = 1;
int count;
double radius;
double interestRate;
```

## Constants

``` 
final double PI = 3.14159;
```

## Numeric Data Types

* byte
* short
* int
* long
* float
* double

### Numeric literals
An integer literal is assumed to be of the `int` type, to denote an integer literal of `long` type: 121211412L

* 01234  octal integer
* 0xf87 or 0XF78 hexadecimal integer

By default floating-point literal is treated as a `double` type value, to make a nubmer of float: 100.2F, double: 200.2D


### Character Data Type

```
char letter = 'A';  //"A" is a string, and 'A' is a character;
char numChar = '4';
```

## Unicode and ASCII 

Mapping a character to its binary representaion is called `encoding`

## String

``` 
String message = "Welcome to Java";
```

### Javadoc

```
/**

*/
``` 

## Converting String to numbers

```
int a = Integer.parseInt(intStr);
double b = Double.parseDouble(str);
```

# Flow Control

```
if (radius < 0) {
  System.out.println("Bad input");
} else {
  area = radius * radius * PI;
  System.out.println("Area is " + area);
}
```

## boolean type

* true
* false

```
boolean lightsOn = true;
```


## comparsion operators

* `<`
* `<=`
* `>`
* `>=`
* `==`
* `!=`

## if statement

```
if (i > 0) {
  System.out.println("is is positive");
}
```
## if else statement

```
if (boolean-expression) {
  statements;
}
else {
  statements;
}
```

## nested if 

```
if (i > k) {
  if (j > k) {
    statements;
  }
} 
else {
  statements;
}
```
## logical operators

* `!`
* `&&`
* `||`
* `^`

## switch

```
switch (status) {
  case 0: statements;
          break;
  case 1: statements;
          break;
  default: statements;
}
```

## Conditional expression

```
y = (x>0)? 1: -1;
```

## while loop

``` 
while (loop-condition) {
  stateements;
}
```
 

## do-while loop

```
do {
  statements;
} while (condition);
```

## for loop

```
for (i = 0; i < 99; i++) {
  statements;
}
```

## for-each loop
```
for (double u: myList) { 
  System.out.println(u);
}
```



### Formatting console output


`System.out.printf(format, item1, item2, ..., item_k_);`


* `%b` boolean value
* `%c` char
* `%d` integar
* `%f` floating
* `%e` scientfic notation
* `%s` string

### Width and precison

* `%5c` Output the character and add four spaces before the character item
* `%10.2f` Output the floating item with width at least 10 including a decimal point


# Methods


```
public static int sum(int i1, int i2) {
  int sum = 0;
  for (int i = i1; i <= i2; i++) {
    sum += i;
  }
  
  return sum; // method return something back
}

// void method does not returning value
public static void main(String[] args) {
  System.out.println("System from 1 to 10 is" + sum(1, 10));
}
```

A call to void method must be a statement

## prarameters

pass by value

## OverLoading

two methods have the same name but different parameter lists within one class, can not overload methods with just different return type

```
public static int max(int a, int b) {
  if (a > b) {
    return a;
  }
  else {
    return b;
  }
}

// max(int, double) will also invoke this one
public static double max(double a, double b) {
  if (a > b) {
    return a;
  }
  else {
    return b;
  }
}
```

## Scope of variable

### local varialbe

* variable scope begains from its declaration
* parameter is a local variable
* varialbe declared in for loop has its scope in the entire loop


# Data Structure
## Array

```
double[] numbers = new double[20];
numbers[0] = 2.0;
//
// array initilizer 
double[] myList = {1.9, 2.9, 3.4, 3.5};
```

the declaration of an array variable does not allocate any space in memory for the array. It creates only a storage location for the refer- ence to an array.

array size can not be changed after created, and when an array is created, its elements are assigned the default value of `0` for the numeric primitive data types, `\u0000` for char types, and `false` for boolean types.

## Array coping
In Java, you can use assignment statements to copy primitive data type variables, but not arrays.

```
 list2 = list1;
 // list1 and list2 reference to the same array
```

* Use a loop to copy individual elements one by one.
* Use the static arraycopy method in the System class.
* Use the clone method to copy arrays

## passing array as argument

array is pass-by-sharing


## Variable-Length Arguemnt list

Only one variable-length parameter may be specified in a method, and this parameter must be the last parameter.

You can pass an array or a variable number of arguments to a variable-length parameter.

```
public static void printMax(double... numbers) {
  double result = nubmers[0];
}
```

## java.util.Arrays

```
// Sort the whole array
double[] numbers = {6.0, 4.4, 1.9, 2.9, 3.4, 3.5}; 
java.util.Arrays.sort(numbers); 
//
char[] chars = {'a', 'A', '4', 'F', 'D', 'P'}; 
// Sort part of the array
java.util.Arrays.sort(chars, 1, 3); 
```

## 2-dimensional array

```
// normal array:
double[][] matrix;
//raged array:
int[][] triangleArray = new int[5][] ; 
triangleArray[0] = new int[5]; 
triangleArray[1] = new int[4]; 
triangleArray[2] = new int[3]; 
triangleArray[3] = new int[2]; 
triangleArray[4] = new int[1];
```

# OOP

**state** of object

**behavior** of object

```
class Circle {
  //attribute
  double radius = 1.0;
  
  // constructor
  Circle() {
  }
  
  //contructor
  Circlr(double newRadius) {
    radius = newRadius;
  }
  
  //method
  double getArea() {
    return radius * radius * 3.14;
  }
}
```


You can put the two classes into one file, but only one class in the file can be a public class. Furthermore, the public class must have the same name as the file name.

* A constructor must have the same name as the class itself.
* Constructors do not have a return type—not even void.
* Constructors are invoked using the new operator when an object is created.

```
//TV.java
public class TV {
  int channel = 1;
  int VolumeLevel = 1;
  boolean on = false;
  
  public TV(){
  }
  
  public void turnOn() {
    on = ture; // instance variable is refered directly here
  }
  
  public void turnOff() {
    on = false;
  }
  
  public void setChannel(int newChannel) {
    if (on && newChannel >= 1 && newChannel <= 120)
      channel = newChannel;
  }
  
  public void setVolume(int new VolumeLevel) {
    if (on && newVolumeLevel >=1 && newVolumeLevel <=7)
      volumeLevel = newVolumeLevel;
  }
  
  public void channelUp() {
    if 
  
}
```

Objects are accessed via object reference variables, which contain references to the objects.

a class is a `reference type`
dot operator

## Constructor


# Exceptions



# Libraries





<!-- Highlight syntax for Mou.app, insert at the bottom of the markdown document  -->

<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>