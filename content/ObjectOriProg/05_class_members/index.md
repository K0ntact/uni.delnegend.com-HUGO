---
title: 05. Class members
draft: false
---

{{<toc>}}

# 1. Class methods
- Examples:

  ```java
  double x = Math.round(3.14);
  int y = Math.abs(-5);
  ```

- Methods in the Math class don't use any instance variable value. So they don;t need to know about a specific Math&nbsp;<c-red>object</c-red>. All we need is the Math&nbsp;<c-red>class</c-red>.
- Math functions were written as&nbsp;<c-red>class</c-red> methods, or&nbsp;<c-red>static</c-red>&nbsp;methods.
- A class method (static method) is one that runs *without any instance of the class*.

# 2. Instance methods vs. class methods

{{<columns>}}
Instance (regular) methods

```java
class Cow {
  String name;
  public String greeting() {
    return ("Hi, I am " + name);
  }
}
```

- Behavior of the instance method *greeting()* is affected by instance variable *name*.
- Instance method is called using a *reference variable*\
  s =&nbsp;<c-red>cow1</c-red>.greeting();

<--->

Class (static) methods

```java
class Math {
  public static double round(double x) {
    return Math.floor(x + 0.5);
  }
}
```

- Static method *round()* doesn't use any instance variable value.
- Static method is called using the class name\
  x = &nbsp;<c-red>Math</c-red>.round(3.14);
{{</columns>}}

# 3. Using class methods
- Class (static) methods can't use:
  - instance variables
  - instance methods

```java
public class Duck {
  private int size;
  public static void main(String[] args) {
    Duck d = new Duck();
    System.out.println("Size of the duck is " + size);
  }
}
```
---
```bash
-> java javac Duck.java
Duck.java:6: error: non-static variable size cannot be referenced from a static context
    System.out.println("Size of the duck is " + size);
1 error
-> java
```
---
```java
public class Duck {
  private int size;
  public static void main(String[] args) {
    Duck d = new Duck();
    setSize(10);
  }
  public void setSize(int s) {
    if (s > 0) size = s;
  }
}
```
---
```bash
-> java javac Duck.java
Duck.java:6: error: non-static method setSize(int) cannot be referenced from a static context
    setSize(10);
    ^
1 error
-> java
```

## Correct code

```java
public class Duck {
  private int size;
  public void setSize(int s) {
    if (s > 0) size = s;
  }
  public static void main(String[] args) {
    Duck d = new Duck();
    d.setSize(10); // the instance object d must be specified
    System.out.println("Size of the duck is " + d.size);
  }
}
```

## Better code

- The program is put in a seperate class:
  - Class Duck should define Duck objects only
  - Different programs can use the same Duck class
```java
public class Duck {
  private int size;
  public void setSize(int s) {...}
}
```
---
```java
public class DuckProgram {
  public static void main(String[] args) {
    Duck d = new Duck();
    d.setSize(10);
    System.out.println("Size of the duck is " + d.size);
  }
}
```

# 4. Class variables
- A class (static) variable belongs to the class, not any object.
- Need just one copy, but shared among all class instances.
```java
public class Duck {
  private int size;
  public static int count = 0; // each duck has its own size, but all ducks share the same attribute "count"
  public Duck() {
    count++;
  }
}
```

# 5. Class variables vs instance variables

{{<columns>}}
Class/static variables
- belong to a class
- need just one copy, but shared among all instances of the class
- initialized before any objects of the class
<--->
Instance variables
- belong to an instance
- each instance has its own copy
- initialized when the owner object is created
{{</columns>}}

```java
public class Duck {
  private int size = 0;
  public static int count = 0;
  public Duck() {
    count++;
    size++;
  }
}
```

# 6. Using class (static) variables
- Class (static) variables can be used by:
  - static methods
  - instance methods

{{<columns>}}
```java
public class Duck {
  private int size;
  public static int count = 0;
  public void incCount() {
    count++;
  }
}
```
<--->
```java
public class DuckTestDrive {
  public static void main(String[] args) {
    Duck d = new Duck();
    d.incCount();
    System.out.println(d.count);
    d.incCount();
    System.out.println(Duck.count);
  }
}
```
{{</columns>}}

```bash
-> java javac DuckTestDrive.java
-> java DuckTestDrive
1 // static variable count is called by instance object d
2 // static variable count is called by class name Duck
```