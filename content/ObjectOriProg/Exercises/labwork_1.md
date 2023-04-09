---
title: "Lab Session 1: Basic Java"
draft: false
---

{{<toc>}}

# Part 1: Install Java Development Environment

- Download and Install [Java JDK](http://www.oracle.com/technetwork/java/javase/downloads/)
- Download and install Editor/IDE:
  - [Notepad++](https://notepad-plus-plus.org/)
  - [Visual Studio Code](https://code.visualstudio.com/)
  - [Sublime Text](https://www.sublimetext.com/)
  - [JetBrains IntelliJ IDEA](https://www.jetbrains.com/idea/)
  - [Eclipse](https://www.eclipse.org/)
- Compile and run the "HelloWorld" program. The following is the Java source code:

```java
public class HelloWorld {
    public static void main (String[] args) {
        System.out.println("Hello World");
    }
}
```

# Part 2: Practice Java exercises
- Visit the website: [introcs.cs.princeton.edu/java/11hello/](https://introcs.cs.princeton.edu/java/11hello/) to do your labwork 1.

## Task 1
Read and do the subsection "1.1. Your First Java Program: Hello World" in the website above.

{{<expand "Solution">}}
- `HelloWorld.java`
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World");
    }
}
```
{{</expand>}}

## Task 2
Do all the Exercises and Web Exercises of the "subsection 1.1." above.

{{<expand "Solution">}}
### Exercise

#### Exercise 1
Write a program `TenHelloWorld.java` that prints "Hello, World" ten times.

```java
public class TenHelloWorld {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.println("Hello, World");
        }
    }
}
```

#### Exercise 5
Modify `UseArgument.java` to make a program UseThree.java that takes three names as command-line arguments and prints a proper sentence with the names in the reverse of the order given, so that, for example, java UseThree Alice Bob Carol prints Hi Carol, Bob, and Alice.

```java
public class UseThree {
    public static void main(String[] args) {
        System.out.println("Hi " + args[2] + ", " + args[1] + ", and " + args[0]);
    }
}
```
---

### Web Exercise

#### Exercise 1
Write a program `HelloWorldMultilingual.java` that prints "Hello World!" in as many as human languages as you can.

```java
public class HelloWorldMultilingual {
  public static void main(String[] args) {
    System.out.println("Hello World!");
    System.out.println("Bonjour le monde!");
    System.out.println("Xin chào thế giới!");
  }
}
```

#### Exercise 2
Write a program `Initials.java` that prints your initials using nine rows of asterisks like the one below.

```
**        ***    **********      **             *             **
**      ***      **        **     **           ***           **
**    ***        **         **     **         ** **         **
**  ***          **          **     **       **   **       **
*****            **          **      **     **     **     **
**  ***          **          **       **   **       **   **
**    ***        **         **         ** **         ** **
**      ***      **        **           ***           ***
**        ***    **********              *             *
```

```java
public class Initials {
  public static void main(String[] args) {
    System.out.println("**        ***    **********      **             *             **");
    System.out.println("**      ***      **        **     **           ***           **");
    System.out.println("**    ***        **         **     **         ** **         **");
    System.out.println("**  ***          **          **     **       **   **       **");
    System.out.println("*****            **          **      **     **     **     **");
    System.out.println("**  ***          **          **       **   **       **   **");
    System.out.println("**    ***        **         **         ** **         ** **");
    System.out.println("**      ***      **        **           ***           ***");
    System.out.println("**        ***    **********              *             *");
  }
}
```

#### Exercise 3
```java
public class HelloWorld {
    public static void main(String[] args) {
        // Prints "Hello, World" in the terminal window.
        System.out.println("Hello, World");
    }
}
```
Describe what happens if, in `HelloWorld.java`, you omit
- `main`: compile error: <identifier> expected
- `String`: compile error: ',', ')' or '[' expected
- `HelloWorld`: compile error: <identifier> expected
- `System.out`: compile error: illegal start of expression
- `println`: compile error: <identifier> expected

#### Exercise 4
Describe what happens if, in `HelloWorld.java`, you omit
- the `;`: compile error: ';' expected
- the first `"`: compile error: unclosed string literal
- the second `"`: compile error: unclosed string literal
- the first `{`: compile error: class, interface, enum, or record expected
- the second `{`: compile error: reached end of file while parsing
- the first `}`: compile error: class, interface, enum, or record expected
- the second `}`: compile error: reached end of file while parsing

#### Exercise 5
Describe what happens if, in `HelloWorld.java`, you misspell (by, say, omitting the second letter)
- `main`: compile error: Main method not found in class HelloWorld, please define the main method as:\
   public static void main(String[] args)\
   or a JavaFX application class must extend javafx.application.Application
- `String`: compile error: cannot find symbol
- `HelloWorld`: class Hlloworld is public, should be declared in a file named Hlloworld.java
- `System.out`: compile error: package Sstem does not exist
- `println`: compile error: cannot find symbol

#### Exercise 6
I typed in the following program. It compiles fine, but when I execute it, I get the error `java.lang.NoSuchMethodError: main`. What am I doing wrong?

```java
public class Hello {
   public static void main() {
      System.out.println("Doesn't execute");
   }
}
```
The `String[] args` is missing in the `main` method.

{{</expand>}}

## Task 3
Read and do the subsection "1.2. Built-in Types of Data" in the website above.

## Task 4
Do all the Exercises of the "subsection 1.2." above.

{{<expand "Solution">}}
### Exercise 1
Suppose that `a` and `b` are `int` values. What does the following sequence of statements do?
```java
int t = a;
b = t;
a = b;
```
`a` and `b` are swapped.

### Exercise 4
Suppose that `a` and `b` are `int` values. Simplify the following expression: `(!(a < b) && !(a > b))`

`a == b`

### Exercise 5
The `exclusive or` operator `^` for boolean operands is defined to be `true` if they are different, `false` if they are the same. Give a truth table for this function.

|   a   |   b   | a ^ b |
| :---: | :---: | :---: |
| true  | true  | false |
| true  | false | true  |
| false | true  | true  |
| false | false | false |

### Exercise 6
Why does `10/3` give `3` and not `3.33333333`?

Because we're dividing two integers, so Java "thinks" the result should be an integer. If we want a floating-point result, represent one of the operands as a floating-point number.

### Exercise 7
What do each of the following print?
- `System.out.println(2 + "bc")`: `2bc` (int + string = string concatenation)
- `System.out.println(2 + 3 + "bc")`: `5bc` (first `2 + 3` is evaluated, then the result is concatenated with `"bc"`)
- `System.out.println((2+3) + "bc")`: `5bc` (parentheses force the evaluation of `2 + 3` first)
- `System.out.println("bc" + (2+3))`: `bc5` (like above)
- `System.out.println("bc" + 2 + 3)`: `bc23` (like the first one, "bc" is concatenated with `2` to produce a string, then `3` is concatenated with that string)

### Exercise 8
Explain how to use `Quadratic.java` to find the square root of a number.
```java
public class Quadratic {

    public static void main(String[] args) {
        double b = Double.parseDouble(args[0]);
        double c = Double.parseDouble(args[1]);

        double discriminant = b*b - 4.0*c;
        double sqroot =  Math.sqrt(discriminant);

        double root1 = (-b + sqroot) / 2.0;
        double root2 = (-b - sqroot) / 2.0;

        System.out.println(root1);
        System.out.println(root2);
    }
}
```
We can use `Quadratic.java` to find the square root of a number by passing the number as the first argument and `0` as the second argument. For example, to find the square root of `2`, we can run `java Quadratic 2 0`.

### Exercise 16
A physics student gets unexpected results when using the code
```java
double force = G * mass1 * mass2 / r * r;
```
to compute values according to the formula $F = \frac{G_1_2}{r^2}$. Explain the problem and correct the code.

The problem is that on a linear line of code, the equation is evaluated from left to right, one by one. So the last part of the above code is equivalent to divide the whole last part with `r`, then multiply the result with `r`. We can add a pair of parentheses to force the evaluation of the `r * r` part first, like this:
```java
double force = G * mass1 * mass2 / (r * r);
```

### Exercise 18
Write a program `Distance.java` that takes two integer command-line arguments x and y and prints the Euclidean distance from the point `(x, y)` to the origin `(0, 0)`.

```java
public class Distance {
    public static void main(String[] args) {
        int x = Integer.parseInt(args[0]);
        int y = Integer.parseInt(args[1]);

        double distance = Math.sqrt(x * x + y * y);

        System.out.println(distance);
    }
}
```

### Exercise 20
Write a program `SumOfTwoDice.java` that prints the sum of two random integers between 1 and 6 (such as you might get when rolling dice).

```java
public class SumOfTwoDice {
    public static void main(String[] args) {
        int die1 = (int) (Math.random() * 6) + 1;
        int die2 = (int) (Math.random() * 6) + 1;

        System.out.println(die1 + die2);
    }
}
```

### Exercise 21
Write a program `SumOfSines.java` that takes a double command-line argument t (in degrees) and prints the value of $sin(2t) + sin(3t)$.

```java
public class SumOfSines {
    public static void main(String[] args) {
        double t = Double.parseDouble(args[0]);

        double result = Math.sin(2 * t) + Math.sin(3 * t);

        System.out.println(result);
    }
}
```

### Exercise 23
Write a program `SpringSeason.java` that takes two int values m and d from the command line and prints true if day d of month m is between March 20 (m = 3, d =20) and June 20 (m = 6, d = 20), false otherwise.

```java
public class SpringSeason {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int d = Integer.parseInt(args[1]);

        boolean result = (m == 3 && d >= 20) || (m == 4) || (m == 5) || (m == 6 && d <= 20);

        System.out.println(result);
    }
}
```
{{</expand>}}

## Task 5
Read and do the subsection "1.3. Conditions and Loops" in the website above.

## Task 6
Do all the Exercises of the "subsection 1.3."

{{<expand "Solution">}}
### Exercise 1
Write a program `AllEqual.java` that takes three integer command-line arguments and prints equal if all three are equal, and not equal otherwise.

```java
public class AllEqual {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        if (a == b && b == c) {
            System.out.println("equal");
        } else {
            System.out.println("not equal");
        }
    }
}
```

### Exercise 6
Write a program `RollLoadedDie.java` that prints the result of rolling a loaded die such that the probability of getting a 1, 2, 3, 4, or 5 is 1/8 and the probability of getting a 6 is 3/8.

```java
public class RollLoadedDie {
    public static void main(String[] args) {
        double r = Math.random();
        if (r < 1.0 / 8.0) {
            System.out.println(1);
        } else if (r < 2.0 / 8.0) {
            System.out.println(2);
        } else if (r < 3.0 / 8.0) {
            System.out.println(3);
        } else if (r < 4.0 / 8.0) {
            System.out.println(4);
        } else if (r < 5.0 / 8.0) {
            System.out.println(5);
        } else if (r < 8.0 / 8.0) {
            System.out.println(6);
        }
    }
}
```

### Exercise 8
Rewrite `TenHellos.java` to make a program Hellos.java that takes the number of lines to print as a command-line argument. You may assume that the argument is less than 1000. Hint: consider using i % 10 and i % 100 to determine whether to use "st", "nd", "rd", or "th" for printing the ith Hello.

```java
public class Hellos {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        for (int i = 1; i <= n; i++) {
            System.out.print(i);
            if (i % 10 == 1 && i % 100 != 11) {
                System.out.print("st");
            } else if (i % 10 == 2 && i % 100 != 12) {
                System.out.print("nd");
            } else if (i % 10 == 3 && i % 100 != 13) {
                System.out.print("rd");
            } else {
                System.out.print("th");
            }
            System.out.println(" Hello");
        }
    }
}
```

### Exercise 9
Write a program `FivePerLine.java` that, using one for loop and one if statement, prints the integers from 1000 to 2000 with five integers per line. Hint: use the % operator.

```java
public class FivePerLine {
    public static void main(String[] args) {
        for (int i = 1000; i <= 2000; i++) {
            System.out.print(i);
            if (i % 5 == 0) {
                System.out.println();
            } else {
                System.out.print(" ");
            }
        }
    }
}
```

### Exercise 12
Write a program `FunctionGrowth.java` that prints a table of the values of ln n, n, n ln n, n2, n3, and 2n for n = 16, 32, 64, ..., 2048. Use tabs ('\t' characters) to line up columns.

```java
public class FunctionGrowth {
    public static void main(String[] args) {
        System.out.println("ln n\tn\tn ln n\tn^2\tn^3\t2^n");
        for (int i = 16; i <= 2048; i *= 2) {
            System.out.printf("%.2f\t%d\t%.2f\t%d\t%d\t%d\n", Math.log(i), i, i * Math.log(i), i * i, i * i * i, (int) Math.pow(2, i));
        }
    }
}
```

### Exercise 13
What is the value of m and n after executing the following code?
```java
int n = 123456789;
int m = 0;
while (n != 0) {
   m = (10 * m) + (n % 10);
   n = n / 10;
}
```
Answer: m = 987654321, n = 0

### Exercise 14
What does the following code print out?
```java
int f = 0, g = 1;
for (int i = 0; i <= 15; i++) {
   System.out.println(f);
   f = f + g;
   g = f - g;
}
```
Answer:
```
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
```

### Exercise 18
Unlike the harmonic numbers, the sum 1/1 + 1/4 + 1/9 + 1/16 + ... + 1/n2 does converge to a constant as n grows to infinity. (Indeed, the constant is π2 / 6, so this formula can be used to estimate the value of π.) Which of the following for loops computes this sum? Assume that n is an int initialized to 1000000 and sum is a double initialized to 0.

a)
```java
for (int i = 1; i <= n; i++)
  sum = sum + 1 / (i * i);
```
b)
```java
for (int i = 1; i <= n; i++)
  sum = sum + 1.0 / i * i;
```
c)
```java
for (int i = 1; i <= n; i++)
  sum = sum + 1.0 / (i * i);
```
d)
```java
for (int i = 1; i <= n; i++)
  sum = sum + 1 / (1.0 * i * i);
```

Answer: c)

### Exercise 21
Modify `Binary.java` to get a program Modify `Kary.java` that takes a second command-line argument K and converts the first argument to base K. Assume the base is between 2 and 16. For bases greater than 10, use the letters A through F to represent the digits 10 through 15, respectively.

```java
public class Kary {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int k = Integer.parseInt(args[1]);
        String s = "";
        while (n > 0) {
            int r = n % k;
            if (r < 10) {
                s = r + s;
            } else {
                s = (char) ('A' + r - 10) + s;
            }
            n = n / k;
        }
        System.out.println(s);
    }
}
```

### Exercise 22
Write a program code fragment that puts the binary representation of a positive integer n into a String variable s.

```java
int n = 123456789;
String s = "";
while (n > 0) {
    s = (n % 2) + s;
    n = n / 2;
}
```
{{</expand>}}