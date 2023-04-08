---
title: "Lab Session 3: Input/Output"
draft: false
---

{{<toc>}}

# Part 1
Continue to visit the website [introcs.cs.princeton.edu/java/14array/](https://introcs.cs.princeton.edu/java/14array/) to do your labwork 3.

## Task 1
Read and do the subsection "1.4. Arrays" in the website above.

## Task 2
Do all the Exercises of the "subsection 1.4."

{{<expand "Solution">}}
### Exercise 2
Describe and explain what happens when you try to compile a program `HugeArray.java` with the following statement:
```java
int n = 1000;
int[] a = new int[n*n*n*n];
```
Solution:
```java
public class HugeArray {
    public static void main(String[] args) {
        int n = 1000;
        int[] a = new int[n*n*n*n];
    }
}
```

### Exercise 4
Write a code fragment that reverses the order of values in a one-dimensional string array. Do not create another array to hold the result.
```java
public class ReverseArray {
    public static void main(String[] args) {
        String[] a = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j" };
        for (int i = 0; i < a.length / 2; i++) {
            String temp = a[i];
            a[i] = a[a.length - i - 1];
            a[a.length - i - 1] = temp;
        }
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
    }
}
```

### Exercise 5
What is wrong with the following code fragment?
```java
int[] a;
for (int i = 0; i < 10; i++)
   a[i] = i * i;
```
- The array is not initialized.

### Exercise 9
What does the following code fragment print?
```java
int[] a = { 1, 2, 3 };
int[] b = { 1, 2, 3 };
System.out.println(a == b);
```
- `False` because arrays are reference types and `==` compares references, which is the memory address of the array, not the actual values in the array.

### Exercise 10:
Write a program `Deal.java` that takes an integer command-line argument n and prints n poker hands (five cards each) from a shuffled deck, separated by blank lines.
```java
public class Deal {
    public static void main(String[] args) {
        if (args.length != 1 || Integer.parseInt(args[0]) <= 0) {
            throw new IllegalArgumentException("Usage: java Deal <a positive integer>");
        }
        int n = Integer.parseInt(args[0]);
        String[] suit = {"Clubs", "Diamonds", "Hearts", "Spades"};
        String[] rank = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
        String[] deck = new String[52];
        for (int i = 0; i < 52; i++) {
            deck[i] = rank[i % 13] + " of " + suit[i / 13];
        }
        for (int i = 0; i < 52; i++) {
            int r = i + (int) (Math.random() * (52 - i));
            String temp = deck[r];
            deck[r] = deck[i];
            deck[i] = temp;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.println(deck[i * 5 + j]);
            }
            System.out.println();
        }
    }
}
```

### Exercise 11:
Write a program `HowMany.java` that takes a variable number of command-line arguments and prints how many there are.
```java
public class HowMany {
    public static void main(String[] args) {
        System.out.println("There are " + args.length + " arguments.");
    }
}
```

### Exercise 12:
Write a program `DiscreteDistribution.java` that takes a variable number of integer command-line arguments and prints the integer i with probability proportional to the ith command-line argument.
```java
public class DiscreteDistribution {
    public static void main(String[] args) {
        if (args.length != 1 || !args[0].matches("[1-9][0-9]*")) {
            System.out.println("Usage: java Test <positive integer>");
            System.exit(1);
        }
        int n = args.length;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(args[i]);
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += a[i];
        }
        double[] b = new double[n];
        for (int i = 0; i < n; i++) {
            b[i] = (double) a[i] / sum;
        }
        double[] c = new double[n];
        c[0] = b[0];
        for (int i = 1; i < n; i++) {
            c[i] = c[i - 1] + b[i];
        }
        double r = Math.random();
        for (int i = 0; i < n; i++) {
            if (r < c[i]) {
                System.out.println(i);
                break;
            }
        }
    }
}
```

### Exercise 14:
Write a code fragment `Transpose.java` to transpose a square two-dimensional array in place without creating a second array.
```java
public class Transpose {
    public static void main(String[] args) {
        int[][] a = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        System.out.println("Original matrix:");
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Transpose matrix:");
        for (int i = 0; i < a.length; i++) {
            for (int j = i + 1; j < a[i].length; j++) {
                int temp = a[i][j];
                a[i][j] = a[j][i];
                a[j][i] = temp;
            }
        }
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```
{{</expand>}}

## Task 3
Read and do the subsection "1.5. Input and Output" in the website above.

## Task 4
Do all the Exercises of the "subsection 1.5."

{{<expand "Solution">}}
### Exercise 1:
Write a program `MaxMin.java` that reads in integers (as many as the user enters) from standard input and prints out the maximum and minimum values
```java
import java.util.Scanner;
public class MaxMin {
  public static void main(String[] args) {
    int[] array = getInput();
    int max = array[0];
    int min = array[0];
    for (int i = 0; i < array.length; i++) {
      if (array[i] > max) {
        max = array[i];
      }
      if (array[i] < min) {
        min = array[i];
      }
    }
    System.out.println("The max is " + max);
    System.out.println("The min is " + min);
  }
  private static int[] getInput() {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter the number of values: ");
    int size = input.nextInt();
    int[] array = new int[size];
    System.out.print("Enter the values: ");
    for (int i = 0; i < array.length; i++) {
      array[i] = input.nextInt();
    }
    input.close();
    return array;
  }
}
```

### Exercise 3:
Write a program `Stats.java` that takes an integer command-line argument n, reads n floating-point numbers from standard input, and prints their mean (average value) and sample standard deviation (square root of the sum of the squares of their differences from the average, divided by n−1).
```java
public class Stats {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        double[] a = new double[n];
        for (int i = 0; i < n; i++) {
            a[i] = StdIn.readDouble();
        }
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += a[i];
        }
        double mean = sum / n;
        double sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum2 += (a[i] - mean) * (a[i] - mean);
        }
        double std = Math.sqrt(sum2 / (n - 1));
        System.out.println("mean = " + mean);
        System.out.println("std dev = " + std);
    }
}
```

### Exercise 5:
Write a program `LongestRun.java` that reads in a sequence of integers and prints out both the integer that appears in a longest consecutive run and the length of the run. For example, if the input is 1 2 2 1 5 1 1 7 7 7 7 1 1, then your program should print Longest run: 4 consecutive 7s.
```java
public class LongestRun {
    public static void main(String[] args) {
        int max = 0;
        int maxNum = 0;
        int count = 1;
        int prev = StdIn.readInt();
        while (!StdIn.isEmpty()) {
            int n = StdIn.readInt();
            if (n == prev) {
                count++;
            } else {
                if (count > max) {
                    max = count;
                    maxNum = prev;
                }
                count = 1;
            }
            prev = n;
        }
        if (count > max) {
            max = count;
            maxNum = prev;
        }
        System.out.println("Longest run: " + max + " consecutive " + maxNum + "s");
    }
}
```

### Exercise 11:
Write a program `WordCount.java` that reads in text from standard input and prints out the number of words in the text. For the purpose of this exercise, a word is a sequence of non-whitespace characters that is surrounded by whitespace.
```java
public class WordCount {
    public static void main(String[] args) {
        int count = 0;
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            count++;
        }
        System.out.println(count);
    }
}
```

### Exercise 15:
Write a program `Closest.java` that takes three floating-point command-line arguments x,y,z, reads from standard input a sequence of point coordinates (xi,yi,zi), and prints the coordinates of the point closest to (x,y,z). Recall that the square of the distance between (x,y,z) and (xi,yi,zi) is (x−xi)2+(y−yi)2+(z−zi)2. For efficiency, do not use Math.sqrt() or Math.pow().
```java
public class Closest {
    public static void main(String[] args) {
        double x = Double.parseDouble(args[0]);
        double y = Double.parseDouble(args[1]);
        double z = Double.parseDouble(args[2]);
        double min = Double.MAX_VALUE;
        double minx = 0;
        double miny = 0;
        double minz = 0;
        while (!StdIn.isEmpty()) {
            double xi = StdIn.readDouble();
            double yi = StdIn.readDouble();
            double zi = StdIn.readDouble();
            double dist = (x - xi) * (x - xi) + (y - yi) * (y - yi) + (z - zi) * (z - zi);
            if (dist < min) {
                min = dist;
                minx = xi;
                miny = yi;
                minz = zi;
            }
        }
        System.out.println(minx + " " + miny + " " + minz);
    }
}
```

### Exercise 16:
Given the positions and masses of a sequence of objects, write a program to compute their center-of-mass or centroid. The centroid is the average position of the n objects, weighted by mass. If the positions and masses are given by (xi, yi, mi), then the centroid (x, y, m) is given by:
```
m  = m1 + m2 + ... + mn
x  = (m1x1 +  ... + mnxn) / m
y  = (m1y1 +  ... + mnyn) / m
```
Write a program `Centroid.java` that reads in a sequence of positions and masses (xi, yi, mi) from standard input and prints out their center of mass (x, y, m). Hint: model your program after `Average.java`.
```java
public class Centroid {
    public static void main(String[] args) {
        double m = 0;
        double x = 0;
        double y = 0;
        while (!StdIn.isEmpty()) {
            double xi = StdIn.readDouble();
            double yi = StdIn.readDouble();
            double mi = StdIn.readDouble();
            m += mi;
            x += mi * xi;
            y += mi * yi;
        }
        x /= m;
        y /= m;
        System.out.println(x + " " + y + " " + m);
    }
}
```

### Exercise 17:
Write a program `Checkerboard.java` that takes a command-line argument n and plots an n-by-n checkerboard with red and black squares. Color the lower-left square red.
```java
import java.awt.Color;
public class Checkerboard {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        StdDraw.setXscale(0, n);
        StdDraw.setYscale(0, n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((i + j) % 2 == 0) {
                    StdDraw.setPenColor(StdDraw.RED);
                } else {
                    StdDraw.setPenColor(StdDraw.BLACK);
                }
                StdDraw.filledSquare(i + 0.5, j + 0.5, 0.5);
            }
        }
    }
}
```

### Exercise 21:
Write a program `Rose.java` that takes a command-line argument n and plots a rose with n petals (if n is odd) or 2n petals (if n is even) by plotting the polar coordinates (r, θ) of the function r = sin(n × θ) for θ ranging from 0 to 2π radians. Below is the desired output for n = 4, 7, and 8.
```java
import java.awt.Color;
public class Rose {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        StdDraw.setXscale(-1, 1);
        StdDraw.setYscale(-1, 1);
        StdDraw.setPenRadius(0.005);
        StdDraw.setPenColor(Color.BLACK);
        StdDraw.circle(0, 0, 1);
        StdDraw.setPenRadius(0.002);
        for (int i = 0; i < 360; i++) {
            double theta = i * Math.PI / 180;
            double r = Math.sin(n * theta);
            double x = r * Math.cos(theta);
            double y = r * Math.sin(theta);
            StdDraw.point(x, y);
        }
    }
}
```

### Exercise 22:
Write a program `Banner.java` that takes a string s from the command line and display it in banner style on the screen, moving from left to right and wrapping back to the beginning of the string as the end is reached. Add a second command-line argument to control the speed.
```java
public class Banner {
    public static void main(String[] args) {
        String s = args[0];
        int n = s.length();
        int speed = Integer.parseInt(args[1]);
        while (true) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < i; j++) {
                    System.out.print(" ");
                }
                System.out.println(s);
                StdDraw.pause(speed);
                StdDraw.clear();
            }
        }
    }
}
```

### Exercise 26:
Write a program `Circles.java` that draws filled circles of random size at random positions in the unit square, producing images like those below. Your program should take four command-line arguments: the number of circles, the probability that each circle is black, the minimum radius, and the maximum radius.
```java
import java.awt.Color;
public class Circles {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        double p = Double.parseDouble(args[1]);
        double min = Double.parseDouble(args[2]);
        double max = Double.parseDouble(args[3]);
        StdDraw.setXscale(0, 1);
        StdDraw.setYscale(0, 1);
        for (int i = 0; i < n; i++) {
            double x = Math.random();
            double y = Math.random();
            double r = min + Math.random() * (max - min);
            if (Math.random() < p) {
                StdDraw.setPenColor(StdDraw.BLACK);
            } else {
                StdDraw.setPenColor(StdDraw.WHITE);
            }
            StdDraw.filledCircle(x, y, r);
        }
    }
}
```
{{</expand>}}

# Part 2
Write a Java program to manage the employee information of a company as follows:

- Information of each employee is entered from keyboard, including:
  - Employee ID
  - Employee full name
  - Employee department
  - Basic salary
  - Extra salary
- Number of employees (n) is entered from keyboard
- Information of n employees are saved in a text file named: `employees.txt`
- Information about total income of each employee is read from the `employees.txt` file and calculated by the formula:
  - `income = basic_salary + extra_salary * 2.5`
- Print out to the screen the following information of n employees:
  - Employee ID
  - Employee full name
  - Employee department
  - Employee income

{{<expand "Solution">}}
`Employee.java`
```java
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class Employee {
  private String ID;
  private String name;
  private String department;
  private double basic_salary;
  private double extra_salary;

  public Employee(String ID, String name, String department, double basic_salary, double extra_salary) {
    this.ID = ID;
    this.name = name;
    this.department = department;
    this.basic_salary = basic_salary;
    this.extra_salary = extra_salary;
  }

  public String getID() {
    return ID;
  }

  public String getName() {
    return name;
  }

  public String getDepartment() {
    return department;
  }

  public double getBasic_salary() {
    return basic_salary;
  }

  public double getExtra_salary() {
    return extra_salary;
  }

  public String toString() {
    String lineID = "Employee ID: " + ID;
    String lineName = "Employee full name: " + name;
    String lineDepartment = "Employee department: " + department;
    String lineSalary = "Basic salary: " + basic_salary;
    String lineExtraSalary = "Extra salary: " + extra_salary;
    return lineID + "\r\n" + lineName + "\r\n" + lineDepartment + "\r\n" + lineSalary + "\r\n" + lineExtraSalary + "\r\n--------------------";
  }

  public void writeToFile(String path) {
    try {
      FileWriter fileWriter = new FileWriter(path, true);
      BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
      bufferedWriter.write(this.toString());
      bufferedWriter.newLine();
      bufferedWriter.close();
      fileWriter.close();
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }
}
```

`Company.java`
```java
import java.util.Scanner;
import java.io.*;

public class Company {
  public static void main(String[] args) {
    clearScreen();
    Scanner input = new Scanner(System.in);
    int choice = 0;
    while (true) {
      System.out.println("Welcome to the company database! Enter the number of your choice:");
      System.out.println("1. Add employee");
      System.out.println("2. Show employee");
      System.out.println("3. Exit");
      System.out.print("Your choice: ");
      choice = input.nextInt();
      switch (choice) {
        case 1:
          System.out.print("\nHow many employees do you want to add? ");
          int num = 0;
          while (true) {
            try {
              num = input.nextInt();
              break;
            } catch (Exception e) {
              System.out.print("Please enter an integer: ");
              input.nextLine();
            }
          }
          for (int i = 0; i < num; i++) {
            System.out.println("==> Employee " + (i + 1) + ":");
            System.out.print("Employee ID: ");
            String ID = input.next();
            System.out.print("Employee full name: ");
            String name = input.next();
            System.out.print("Employee department: ");
            String department = input.next();
            System.out.print("Basic salary: ");
            double basic_salary = 0;
            while (true) {
              try {
                basic_salary = input.nextDouble();
                if (basic_salary <= 0) {
                  throw new Exception("Basic salary must be larger than 0!");
                }
                break;
              } catch (Exception e) {
                System.out.println("Error: basic salary must be a number larger than 0!");
                System.out.print("Basic salary: ");
              }
            }
            System.out.print("Extra salary: ");
            double extra_salary = 0;
            while (true) {
              try {
                extra_salary = input.nextDouble();
                if (extra_salary <= 0) {
                  throw new Exception("Extra salary must be larger than 0!");
                }
                break;
              } catch (Exception e) {
                System.out.println("Error: extra salary must be a number larger than 0!");
                System.out.print("Extra salary: ");
              }
            }
            Employee employee = new Employee(ID, name, department, basic_salary, extra_salary);
            employee.writeToFile("employee.txt");
          }
          clearScreen();
          break;
        case 2:
          clearScreen();
          showEmployee();
          System.out.println();
          break;
        case 3:
          input.close();
          System.exit(0);
          break;
        default:
          System.out.println("Invalid choice!");
          break;
      }
    }
  }

  private static void showEmployee() {
    try {
      FileReader fileReader = new FileReader("./employee.txt");
      BufferedReader bufferedReader = new BufferedReader(fileReader);
      String line = bufferedReader.readLine();
      while (line != null) {
        if (line.startsWith("Basic salary")) {
          String[] salary = line.split(": ");
          double basic_salary = Double.parseDouble(salary[1]);
          line = bufferedReader.readLine();
          String[] extra_salary = line.split(": ");
          double extra_salary_value = Double.parseDouble(extra_salary[1]);
          System.out.println("Income: " + (basic_salary + extra_salary_value * 2.5));
          line = bufferedReader.readLine();
        } else {
          System.out.println(line);
          line = bufferedReader.readLine();
        }
      }
      bufferedReader.close();
      fileReader.close();
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  private static void clearScreen() {
    System.out.print("\033[H\033[2J");
    System.out.flush();
  }
}
```
{{</expand>}}