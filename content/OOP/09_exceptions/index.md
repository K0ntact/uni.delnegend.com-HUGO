---
title: 09. Exceptions
draft: false
---

{{<toc>}}

# What is Exception?
- Exception is an indication of&nbsp;<c-red>problem<c-red>&nbsp;that arises during the execution of a program.
- Exception happens in case of:
  - Designing errors.
  - Programming errors.
  - Data errors.
  - System errors.
  - ...

## Example: open file

{{<highlight Java "linenos=table">}}
import java.io.PrintWriter;
import java.io.File;

class FileWriter {
  public static void write(String path, String content) {
    File file = new File(path);
    PrintWriter out = new PrintWriter(file); // open file to write

    out.println(content);
    out.close();
  }
}
{{</highlight>}}

```bash
-> javac FileWriter.java
FileWriter.java:7:error: unsupported exception FileNotFoundException;
must be caught or declared to be thrown
  PrintWriter out = new PrintWriter(file); # compile-time error

1 error
```

## Example: invalid input

{{<highlight Java "linenos=table">}}
import java.util.*;
public class TestException {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Numerator: ");
    int numerator = scanner.nextInt(); // what happens if input isn't integer
    System.out.println("Denominator: ");
    int denominator = scanner.nextInt(); // what happens if input isn't integer

    int result = numerator/denominator;
    System.out.println("\nResult: " + result);
  }
}
{{</highlight>}}

```bash
-> javac TestException.java
-> java TestException
Numerator: abc
Exception in thread "main" java.util.InputMismatchException # runtime error by invalid integer input "abc"
      at java.util.Scanner.throwFor(Unknown source)
      at java.util.Scanner.next(Unknown source)
      at java.util.Scanner.nextInt(Unknown source)
      at java.util.Scanner.nextInt(Unknown source)
      at TestException.main(TestException.java:9)
```

## Example: divide by zero

{{<highlight Java "linenos=table">}}
import java.util.*;
public class TestException {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Numerator: ");
    int numerator = scanner.nextInt();
    System.out.println("Denominator: ");
    int denominator = scanner.nextInt();

    int result = numerator/denominator; // what happens if denominator is zero
    System.out.println("\nResult: " + result);
  }
}
{{</highlight>}}

```bash
-> javac TestException.java
-> java TestException
Numerator: 10
Denominator: 0
Exception in thread "main" java.lang.ArithmeticException: / by zero # runtime error by divide by zero
      at TestException.main(TestException.java:10)
```

# Throwing Exceptions
- Exception is thrown to an&nbsp;<c-red>object<c-red>&nbsp;that contains information about the error.
- <c-red>**throws**<c-red>&nbsp;clause - specifies types of exceptions a method may throw
- Thrown exceptions can be:
  - in method's body, or
  - from method's header

```java
class Fraction {
  private int numerator, denominator;
  public Fraction(int n, int d) throws ArithmeticException { // declare what type of exception the method might throw
    if (d == 0) {
      throw new ArithmeticException("Denominator cannot be zero"); // an ArithmeticException object is created and thrown in method's body
    }
    numerator = n;
    denominator = d;
  }
}

public class TestException {
  public static void main(String[] args) {
    try {
      Fraction f = new Fraction(10, 0); // an ArithmeticException object is thrown from method's header
    } catch (ArithmeticException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

# Throw point
```java
import java.util.*;
public class TestException {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Numerator: ");
    int numerator = scanner.nextInt();
    //...
  }
}
```
---
```bash
-> javac TestException.java
-> java TestException
Numerator: abc
Exception in thread "main" java.util.InputMismatchException
      at java.util.Scanner.throwFor(Unknown source) # throw point
      at java.util.Scanner.next(Unknown source)
      at java.util.Scanner.nextInt(Unknown source)
      at java.util.Scanner.nextInt(Unknown source)
      at TestException.main(TestException.java:9)
```

# Catching exceptions
- Syntax:
  ```java
  try {
    // throw an exception
  } catch (TypeOfException e) {
    // handle the exception
  }
  ```
- Seperate the code that describes what you want to do (<c-red>program logic</c-red>) from the code that is executed when things go wrong (<c-red>error handling</c-red>)
  - try block - program logic: encloses code that might throw an exception and the code that should not be executed if an exception occur.
  - catch block - error handling: catches and handles exceptions
- A **catch** block can catch:
  - Exception of the declared type:
    ```java
    catch (IOException e) {
      // catch exceptions of type IOException
    }
    ```
  - Exception of subclass of the declared type:
    ```java
    catch (IOException e) {
      // catch exceptions of type FileNotFoundException
      // or EOFException...
    }
    ```
- Uncaught exception: an exception that occurrs when no **catch** block matches.

# How try and catch work?

![](01_try_catch.png)

![](02_try_catch.png)

# Finally block

{{<columns>}}

- <c-red>Optional</c-red>&nbsp; is a try statement.
- Placed after&nbsp;<c-red>last</c-red>&nbsp;catch block.
- Always executed, regardless of whether an exception is thrown or not, except when application exits (e.g. using&nbsp;<c-red>System.exit()</c-red>).
- Often contains resouce-release code (e.g. closing files, network connections, database connections, etc.)

<--->

```java
try {
  //...
} catch (ExceptionType1 e) {
  //...
} catch (ExceptionType2 e) {
  //...
} finally {
  //...
}
```

{{</columns>}}

# How finally block works?

![](03_try_catch_finally.png)

## Eample: finally block

{{<highlight Java "linenos=table">}}
public class TestFinallyBlock {
  public static void main(String[] args) {
    try {
      int[] myNumbers = {1, 2, 3};
      System.out.println(myNumbers[10]);
    } catch (Exception e) {
      System.out.println("Something went wrong.");
    } finally {
      System.out.println("The 'try catch' is finished.");
    }
  }
}
{{</highlight>}}

```bash
-> javac TestFinallyBlock.java
-> java TestFinallyBlock
Something went wrong.
The 'try catch' is finished.
```

# Java Exception Hierarchy

![](04_exception_hierarchy.png)

# Handling exceptions
- The goal is to resolve exceptions so that the program can continue to run or terminate gracefully.
- Handling exception enables programmers to write code that is more robust and reliable.

# Exception handling methods
Three choices to put to a method:
- catch and handle:&nbsp;<c-red>try and catch blocks</c-red>.
- pass it on to the methods's caller:&nbsp;<c-red>throws exceptions</c-red>.
- catch, handle, then pass it on:&nbsp;<c-red>re-thrown exceptions</c-red>.

# Rethrowing exceptiosn
- Exeptions can be re-thrown when a catch block decides that:
  - it cannot process the exception, or
  - it can process the exception only partially.
- Example:
  ```java
  try {
    //...
  } catch (ExceptionType1 e) {
    //...
  } catch (ExceptionType2 e) {
    System.out.println(e.getMessage());
    throw e;
  }
  ```

# Tracing exceptions
- Can use `printStackTrace()` method to trace back to the point where the exception was thrown.

{{<highlight Java "linenos=table">}}
public class TestFinallyBlock {
  public static void main(String[] args) {
    try {
      String a = null;
      System.out.println("a is " + a.toLowerCase());
    } catch (NullPointerException e) {
      System.out.println("Something went wrong.");
      e.printStackTrace();
    } finally {
      System.out.println("The 'try catch' is finished.");
    }
  }
}
{{</highlight>}}
```bash
-> javac TestFinallyBlock.java
-> java TestFinallyBlock
Something went wrong.
java.lang.NullPointerException
      at TestFinallyBlock.main(TestFinallyBlock.java:6)
The 'try catch' is finished.
```