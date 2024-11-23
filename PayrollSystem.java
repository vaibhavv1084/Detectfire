import java.util.Scanner;

class Employee {
    String name;
    int id;
    double baseSalary;
    double overtimeRate;
    double leaveBalance;

    Employee(String name, int id, double baseSalary, double overtimeRate, double leaveBalance) {
        this.name = name;
        this.id = id;
        this.baseSalary = baseSalary;
        this.overtimeRate = overtimeRate;
        this.leaveBalance = leaveBalance;
    }

    double calculateMonthlySalary(double overtimeHours, double salaryLoss) {
        double overtimePay = overtimeHours * overtimeRate;
        double monthlySalary = baseSalary + overtimePay - salaryLoss;
        return monthlySalary;
    }
}

public class PayrollSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Employee Data Entry
        System.out.println("Enter employee details:");
        System.out.print("Name: ");
        String name = scanner.nextLine();
        System.out.print("ID: ");
        int id = scanner.nextInt();
        System.out.print("Base Salary: ");
        double baseSalary = scanner.nextDouble();
        System.out.print("Overtime Rate: ");
        double overtimeRate = scanner.nextDouble();
        System.out.print("Initial Leave Balance: ");
        double leaveBalance = scanner.nextDouble();
        Employee employee = new Employee(name, id, baseSalary, overtimeRate, leaveBalance);

        // Leave Management
        System.out.print("Enter number of leave days requested: ");
        double leaveDaysRequested = scanner.nextDouble();
        double salaryLoss = 0;
        if (leaveDaysRequested > employee.leaveBalance) {
            System.out.print("Enter salary loss per day for additional leave days: ");
            double salaryLossPerDay = scanner.nextDouble();
            salaryLoss = (leaveDaysRequested - employee.leaveBalance) * salaryLossPerDay;
        }
        System.out.println("Salary loss for requested leave: $" + salaryLoss);

        // Overtime Recording
        System.out.print("Enter number of overtime hours worked: ");
        double overtimeHours = scanner.nextDouble();

        // Salary Calculation
        double monthlySalary = employee.calculateMonthlySalary(overtimeHours, salaryLoss);
        System.out.println("Monthly Salary: $" + monthlySalary);

        scanner.close();
    }
}

