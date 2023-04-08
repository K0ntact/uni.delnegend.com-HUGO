---
title: "Lab Session 4: Inheritance and Polymorphism"
draft: false
---

{{<toc>}}

# Task 1
{{<columns>}}
Design and Implement the following multi-level inheritance structure:
- Object class is the parent class of all classes in Java
- Shape class is an abstract class and is a child of Object class. Shape class contains two regular methods and one abstract method 
  - Regular method `calArea()`: return the area of the shape
  - Regular method `calVolume()`: return the volume of the shape
  - Abstract method `getName()`: return the name of the shape
- Point is a regular class and is a child of Shape class.
  - A point is defined by two coordinates (x & y)
  - Point class inherits/overrides regular methods of Shape class and implements abstract method of Shape class
- Circle is a regular class and is a child of Point class
  - A circle is defined by two coordinates (x & y) of the center and radius r
  - Circle class inherits/overrides regular methods of Shape/Point class and implements abstract methods of Shape/Point class
- Cylinder is a regular class and is a child of Circle class
  - A cylinder is defined by two coordinates (x & y) of the center, radius r and height h
  - Cylinder class inherits/overrides regular methods of Shape/Point/Circle class and implements abstract methods of Shape/Point/Circle class
<--->
![](../inheritance.webp)
{{</columns>}}

{{<expand "Solution">}}
`pkg\Object.java`
```java
package pkg;

public class Object {
  abstract class Shape {
    public double calArea() {
      return 0;
    }

    public double calVolume() {
      return 0;
    }
    abstract public String getName();
  }

  public class Point extends Shape {
    public double x;
    public double y;

    public Point(double x, double y) {
      this.x = x;
      this.y = y;
    }

    public double getX() {
      return x;
    }

    public double getY() {
      return y;
    }

    public double calArea() {
      return 0;
    }

    public double calVolume() {
      return 0;
    }

    public String getName() {
      return "Point";
    }
  }

  public class Circle extends Point {
    public double r;

    public Circle(double x, double y, double r) {
      super(x, y);
      this.r = r;
    }

    public double getR() {
      return r;
    }

    public double calArea() {
      return Math.round(Math.PI * r * r * 100.0) / 100.0;
    }

    public double calVolume() {
      return 0;
    }

    public String getName() {
      return "Circle";
    }
  }

  public class Cylinder extends Circle {
    private double h;

    public Cylinder(double x, double y, double r, double h) {
      super(x, y, r);
      this.h = h;
    }

    public double getH() {
      return h;
    }

    public double calArea() {
      return Math.round(2 * Math.PI * r * (r + h) * 100.0) / 100.0;
    }

    public double calVolume() {
      return Math.round(Math.PI * r * r * h * 100.0) / 100.0;
    }

    public String getName() {
      return "Cylinder";
    }
  }
}
```
{{</expand>}}

# Task 2
Develop a "ShapeTestDrive" Java program to check the inheritance relationship of Point, Circle, Cylinder with the Shape class.
- Use polymorphism concept to create an array of objects "Point, Circle and Cylinder"
- Browse created polymorphic array to perform the four following operations for each element of the array:
  - Get name of the object to see if it is a Point or a Circle or a Cylinder
  - Calculate the area of the object
  - Calculate the volume of the object
  - Display name, area and volume of each object to the screen

{{<expand "Solution">}}
`ShapeTestDrive.java`
```java
import pkg.Object;

public class ShapeTestDrive {
    public static void main(String[] args) {
        Object.Point point = new Object().new Point(1, 2);
        Object.Circle circle = new Object().new Circle(1, 2, 3);
        Object.Cylinder cylinder = new Object().new Cylinder(1, 2, 3, 4);
        System.out.println("Point: " + point.getName() + ", area: " + point.calArea() + ", volume: " + point.calVolume());
        System.out.println("Circle: " + circle.getName() + ", area: " + circle.calArea() + ", volume: " + circle.calVolume());
        System.out.println("Cylinder: " + cylinder.getName() + ", area: " + cylinder.calArea() + ", volume: " + cylinder.calVolume());
    }
}
```
{{</expand>}}

# Task 3
Re-do the task 1 and 2 but using Interface instead of abstract classes as much as possible.

{{<expand "Solution">}}
`pkg\ObjectInterface.java`
```java
package pkg;

public class ObjectInterface {
  abstract interface Shape {
    public double calArea();
    public double calVolume();
    public String getName();
  }
  public class Point implements Shape {
    public double x;
    public double y;
    public Point(double x, double y) {
      this.x = x;
      this.y = y;
    }
    public double getX() {
      return x;
    }
    public double getY() {
      return y;
    }
    public double calArea() {
      return 0;
    }
    public double calVolume() {
      return 0;
    }
    public String getName() {
      return "Point";
    }
  }
  public class Circle extends Point {
    public double r;
    public Circle(double x, double y, double r) {
      super(x, y);
      this.r = r;
    }
    public double getR() {
      return r;
    }
    public double calArea() {
      return Math.round(Math.PI * r * r * 100.0) / 100.0;
    }
    public double calVolume() {
      return 0;
    }
    public String getName() {
      return "Circle";
    }
  }
  public class Cylinder extends Circle {
    public double h;
    public Cylinder(double x, double y, double r, double h) {
      super(x, y, r);
      this.h = h;
    }
    public double getH() {
      return h;
    }
    public double calArea() {
      return Math.round(2 * Math.PI * r * (r + h) * 100.0) / 100.0;
    }
    public double calVolume() {
      return Math.round(Math.PI * r * r * h * 100.0) / 100.0;
    }
    public String getName() {
      return "Cylinder";
    }
  }
}
```
`ShapeInterfaceTestDrive.java`
```java
import pkg.ObjectInterface;

public class ShapeInterfaceTestDrive {
  public static void main(String[] args) {
    ObjectInterface.Point point = new ObjectInterface().new Point(1, 2);
    ObjectInterface.Circle circle = new ObjectInterface().new Circle(1, 2, 3);
    ObjectInterface.Cylinder cylinder = new ObjectInterface().new Cylinder(1, 2, 3, 4);
    System.out.println("Point: " + point.getName() + ", area: " + point.calArea() + ", volume: " + point.calVolume());
    System.out.println("Circle: " + circle.getName() + ", area: " + circle.calArea() + ", volume: " + circle.calVolume());
    System.out.println("Cylinder: " + cylinder.getName() + ", area: " + cylinder.calArea() + ", volume: " + cylinder.calVolume());
  }
}
```
{{</expand>}}
