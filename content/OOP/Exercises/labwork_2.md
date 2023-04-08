---
title: "Lab Session 2: Objects and Classes"
draft: false
---

{{<toc-tree>}}

# Exercise 1: NameCard
{{<columns>}}
Write a Java class "NameCard" and a Java tester class "NameCardTestDrive" to present the corresponding NameCard design:
- Apply the "Encapsulation" concept in your classes
- The tester class should print out the instance NameCard values
<--->
![](../NameCard.webp)
{{</columns>}}

{{<expand "Solution">}}
`NameCard.java`
```java
public class NameCard {
    private String name;
    private String email;
    private String phone;
    public NameCard(String name, String email, String phone) {
        this.name = name;
        this.email = email;
        this.phone = phone;
    }
    public String getName() {
        return name;
    }
    public String getEmail() {
        return email;
    }
    public String getPhone() {
        return phone;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String toString() {
        return "Name: " + name + ", Email: " + email + ", Phone: " + phone;
    }
}
```
`NameCardTestDrive.java`
```java
public class NameCardTestDrive {
  public static void main(String[] args) {
    NameCard nc = new NameCard("John", "abc@xyz.123", "0123456789");
    System.out.println(nc);
  }
}
```
{{</expand>}}

# Exercise 2: Cow
{{<columns>}}
Write a Java class "Cow" and a Java tester class "CowTestDrive" to implement the OOP class design: "Cow"
- Apply the "Encapsulation" concept in your classes
- The `moo()` method should print out the text "Moo...!"
- The tester class should:
  - Make a Cow object
  - Set the age of the Cow to 4
  - Call the `moo()` method
<--->
| Cow             |
|-----------------|
| - name: String  |
| - breed: String |
| - age: int      |
| ---             |
| - moo()         |
{{</columns>}}

{{<expand "Solution">}}
`Cow.java`
```java
public class Cow {
  private String name;
  private String breed;
  private int age;

  public Cow(String name, String breed, int age) {
    this.name = name;
    this.breed = breed;
    this.age = age;
  }

  public String toString() {
    return "Cow [name=" + name + ", breed=" + breed + ", age=" + age + "]";
  }
  public void moo() {
    System.out.println("Moo...!");
  }
}
```
`CowTestDrive.java`
```java
public class CowTestDrive {
  public static void main(String[] args) {
    Cow cow = new Cow("Betsy", "Holstein", 4);
    System.out.println(cow);
    cow.moo();
  }
}
```
{{</expand>}}

# Exercise 3: Vector
{{<columns>}}
Write a Java class "Vector" and a Java tester class "VectorTestDrive" to implement the OOP class design: "Vector".
- Apply "Encapsulation" concept in your classes
- In your tester class "VectorTestDrive":
  - Create and print out information of 2 vectors
  - Calculate and print out the addition, subtraction and multiplication of the two created vectors
<--->
| Vector                   |
|--------------------------|
| - x: int                 |
| - y: int                 |
| ---                      |
| - add(Vector other)      |
| - subtract(Vector other) |
| - multiply(Vector other) |
{{</columns>}}

{{<expand "Solution">}}
`Vector.java`
```java
public class Vector {
  private int x;
  private int y;

  public Vector(int x, int y) {
    this.x = x;
    this.y = y;
  }
  public Vector add(Vector v) {
    int new_x = this.x + v.x;
    int new_y = this.y + v.y;
    return new Vector(new_x, new_y);
  }

  public Vector subtract(Vector v) {
    int new_x = this.x - v.x;
    int new_y = this.y - v.y;
    return new Vector(new_x, new_y);
  }

  public Vector multiply(Vector v) {
    int new_x = this.x * v.x;
    int new_y = this.y * v.y;
    return new Vector(new_x, new_y);
  }
  public String toString() {
    return "(" + x + ", " + y + ")";
  }
}
```

`VectorTestDrive.java`
```java
public class VectorTestDrive {
  public static void main(String[] args) {
    Vector vector_1 = new Vector(1, 2);
    Vector vector_2 = new Vector(3, 4);
    System.out.println("Vector 1: " + vector_1 + " | Vector 2: " + vector_2);
    System.out.println("Vector 1 + Vector 2 = " + vector_1.add(vector_2));
    System.out.println("Vector 1 - Vector 2 = " + vector_1.subtract(vector_2));
    System.out.println("Vector 1 * Vector 2 = " + vector_1.multiply(vector_2));
  }
}
```
{{</expand>}}

# Exercise 4: ShoppingCart
{{<columns>}}
Write a Java class "ShoppingCart" and a Java tester class "ShoppingCartTestDrive" to implement the OOP class design: "ShoppingCart".
- Apply "Encapsulation" concept in your classes
- Implement three methods `addToCart()`, `removeFromCart()`, `checkOut()` and print demo results to the screen
<--->
| ShoppingCart                  |
|-------------------------------|
| - cartContents: String[]      |
| ---                           |
| - addToCart(String item)      |
| - removeFromCart(String item) |
| - checkOut()                  |
{{</columns>}}

{{<expand "Solution">}}
`ShoppingCart.java`
```java
import java.util.ArrayList;

public class ShoppingCart {
  private ArrayList<String> cartContents = new ArrayList<String>();
  public void addToCart(String item) {
    cartContents.add(item);
  }
  public void removeFromCart(String item) {
    cartContents.remove(item);
  }
  public void checkOut() {
    System.out.println("==> Checking out " + cartContents.size() + " items.");
    for (int i = 0; i < cartContents.size(); i++) {
      System.out.println(cartContents.get(i));
    }
  }
}
```
`ShoppingCartTestDrive.java`
```java
public class ShoppingCartTestDrive {
  public static void main(String[] args) {
    ShoppingCart cart = new ShoppingCart();
    cart.addToCart("Shoes");
    cart.addToCart("Hat");
    cart.addToCart("Socks");
    cart.checkOut();
    cart.removeFromCart("Hat");
    cart.checkOut();
  }
}
```
{{</expand>}}

# Exercise 5: Button
{{<columns>}}
Write a Java class "Button" and a Java tester class "ButtonTestDrive" to implement the class design: "Button".
- Apply "Encapsulation" concept in your classes
- Implement four methods `setColor()`, `setLabel()`, `dePress()`, `unDepress()` and print demo results to the screen
<--->
| Button               |
|----------------------|
| - label: String      |
| - color: String      |
| ---                  |
| - setColor(String c) |
| - setLabel(String l) |
| - dePress()          |
| - unDepress()        |
{{</columns>}}

{{<expand "Solution">}}
`Button.java`
```java
public class Button {
  private String label;
  private String color;

  public void setColor(String color) {
    this.color = color;
  }
  public void setLabel(String label) {
    this.label = label;
  }
  public void dePress() {
    System.out.println("Button depressed");
  }
  public void unDepress() {
    System.out.println("Button un-depressed");
  }
}
```
`ButtonTestDrive.java`
```java
public class ButtonTestDrive {
  public static void main(String[] args) {
    Button b = new Button();
    b.setColor("blue");
    b.setLabel("light switch");
    b.dePress();
    b.unDepress();
  }
}
```
{{</expand>}}

# Exercise 6: Automobile
The following codes implement the OOP class design: "Automobile". However, these codes have some problems with OOP principles. Try to run these codes, then find the problems and fix them as much as possible.

{{<columns>}}
```java
class Automobile {
  // These variables are
  // - Not private: anyone can access them
  // - Static: they are shared by all instances of the class

  static double fuel;
  static double speed;
  static String license;

  // These methods are
  // - Not public: they can only be accessed by other methods in the class

  static void init(double f, double s, String l) {
    fuel = f;
    speed = s;
    license = l;
  }

  static void accelerate(double v) {
    if (fuel > 0) speed += v;
  }
  static void decelerate(double v) {
    if (fuel <= 0) speed -= v;
  }

  public static void main(String args[]) {
    init(4.5,34,"29JAD");
    accelerate(4);
    decelerate(5);
  }
}
```
<--->
| Automobile                   |
|------------------------------|
| - fuel: double               |
| - speed: double              |
| - license: String            |
| ---                          |
| - accelerate(double v): void |
| - decelerate(double v): void |
{{</columns>}}

{{<expand "Solution">}}
`Automobile.java`
```java
public class Automobile {
  private double fuel;
  private double speed;
  private String license;

  public void init(double fuel, double speed, String license) {
    this.fuel = fuel;
    this.speed = speed;
    this.license = license;
  }

  public void accelerate(double amount) {
    if (amount > 0 && fuel > 0) {
      speed += amount;
    }
  }
  public void decelerate(double amount) {
    if (amount > 0 && fuel <= 0) {
      speed -= amount;
    }
  }
  public String toString() {
    return "Fuel: " + fuel + " Speed: " + speed + " License: " + license;
  }
}
```
`AutomobileTestDrive.java`
```java
public class AutomobileTestDrive {
  public static void main(String[] args) {
    Automobile a = new Automobile();
    a.init(10, 0, "ABC123");
    a.accelerate(10);
    System.out.println(a);
    a.decelerate(10);
    System.out.println(a);
  }
}
```
{{</expand>}}