       IDENTIFICATION DIVISION.
       PROGRAM-ID. BONUSCALC.
       AUTHOR. TITO-KINYAMBU.
       DATE-WRITTEN. 2026-07-08.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. GnuCOBOL.
       OBJECT-COMPUTER. GnuCOBOL.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  WS-EMPLOYEE-NAME         PIC X(20).

       01  WS-DEPT-CODE             PIC XX.
           88  DEPT-SALES           VALUE "SL".
           88  DEPT-IT              VALUE "IT".
           88  DEPT-HR              VALUE "HR".
           88  DEPT-FINANCE         VALUE "FN".

       01  WS-PERFORMANCE-RATING    PIC 9.
           88  VALID-RATING         VALUES 1 THRU 5.
           88  LOW-PERFORMER        VALUES 1 2.
           88  AVERAGE-PERFORMER    VALUE 3.
           88  HIGH-PERFORMER       VALUES 4 5.

       01  WS-YEARS-SERVICE         PIC 99.
           88  JUNIOR-TENURE        VALUES 0 1.
           88  MID-TENURE           VALUES 2 THRU 4.
           88  SENIOR-TENURE        VALUES 5 THRU 99.

       01  WS-BASE-SALARY           PIC 9(6)V99.
       01  WS-BONUS-PERCENT         PIC V99.
       01  WS-BONUS-AMOUNT          PIC 9(6)V99.
       01  WS-BONUS-TIER            PIC X(8).

       01  WS-PERFORMANCE-DESC      PIC X(17).
       01  WS-TENURE-DESC           PIC X(13).

       01  WS-YEARS-DISPLAY         PIC Z9.
       01  WS-PERCENT-WHOLE         PIC 99.
       01  WS-SALARY-DISPLAY        PIC ZZZ,ZZ9.99.
       01  WS-BONUS-DISPLAY         PIC ZZZ,ZZ9.99.

       01  WS-SEPARATOR             PIC X(40) VALUE ALL "-".

       PROCEDURE DIVISION.

       MAIN-LOGIC.
           DISPLAY " "
           DISPLAY "Enter Employee Name: "
           ACCEPT WS-EMPLOYEE-NAME

           DISPLAY "Enter Department Code (SL/IT/HR/FN): "
           ACCEPT WS-DEPT-CODE

           DISPLAY "Enter Performance Rating (1-5): "
           ACCEPT WS-PERFORMANCE-RATING

           DISPLAY "Enter Years of Service: "
           ACCEPT WS-YEARS-SERVICE

           DISPLAY "Enter Base Salary: "
           ACCEPT WS-BASE-SALARY

           MOVE WS-YEARS-SERVICE TO WS-YEARS-DISPLAY

           DISPLAY " "
           DISPLAY WS-SEPARATOR
           DISPLAY "Employee Name    : " WS-EMPLOYEE-NAME
           DISPLAY WS-SEPARATOR

           IF DEPT-SALES OR DEPT-IT OR DEPT-HR OR DEPT-FINANCE
               CONTINUE
           ELSE
               DISPLAY "ERROR: Department code " WS-DEPT-CODE
                   " is not recognized."
               DISPLAY "No bonus was calculated."
               DISPLAY WS-SEPARATOR
               STOP RUN
           END-IF

           IF VALID-RATING
               CONTINUE
           ELSE
               DISPLAY "ERROR: Performance rating "
                   WS-PERFORMANCE-RATING " is not valid (must be 1-5)."
               DISPLAY "No bonus was calculated."
               DISPLAY WS-SEPARATOR
               STOP RUN
           END-IF

           EVALUATE TRUE
               WHEN LOW-PERFORMER
                   MOVE "Low Performer" TO WS-PERFORMANCE-DESC
               WHEN AVERAGE-PERFORMER
                   MOVE "Average Performer" TO WS-PERFORMANCE-DESC
               WHEN HIGH-PERFORMER
                   MOVE "High Performer" TO WS-PERFORMANCE-DESC
           END-EVALUATE

           EVALUATE TRUE
               WHEN JUNIOR-TENURE
                   MOVE "Junior Tenure" TO WS-TENURE-DESC
               WHEN MID-TENURE
                   MOVE "Mid Tenure" TO WS-TENURE-DESC
               WHEN SENIOR-TENURE
                   MOVE "Senior Tenure" TO WS-TENURE-DESC
           END-EVALUATE

           EVALUATE TRUE ALSO TRUE
               WHEN LOW-PERFORMER ALSO JUNIOR-TENURE
               WHEN LOW-PERFORMER ALSO MID-TENURE
               WHEN AVERAGE-PERFORMER ALSO JUNIOR-TENURE
                   MOVE "BRONZE" TO WS-BONUS-TIER
                   MOVE 0.05 TO WS-BONUS-PERCENT
               WHEN LOW-PERFORMER ALSO SENIOR-TENURE
               WHEN AVERAGE-PERFORMER ALSO MID-TENURE
               WHEN HIGH-PERFORMER ALSO JUNIOR-TENURE
                   MOVE "SILVER" TO WS-BONUS-TIER
                   MOVE 0.10 TO WS-BONUS-PERCENT
               WHEN AVERAGE-PERFORMER ALSO SENIOR-TENURE
               WHEN HIGH-PERFORMER ALSO MID-TENURE
                   MOVE "GOLD" TO WS-BONUS-TIER
                   MOVE 0.15 TO WS-BONUS-PERCENT
               WHEN HIGH-PERFORMER ALSO SENIOR-TENURE
                   MOVE "PLATINUM" TO WS-BONUS-TIER
                   MOVE 0.20 TO WS-BONUS-PERCENT
           END-EVALUATE

           COMPUTE WS-BONUS-AMOUNT ROUNDED =
               WS-BASE-SALARY * WS-BONUS-PERCENT

           COMPUTE WS-PERCENT-WHOLE = WS-BONUS-PERCENT * 100

           MOVE WS-BASE-SALARY TO WS-SALARY-DISPLAY
           MOVE WS-BONUS-AMOUNT TO WS-BONUS-DISPLAY

           DISPLAY "Department       : " WS-DEPT-CODE
           DISPLAY "Performance      : " WS-PERFORMANCE-RATING " ("
               FUNCTION TRIM(WS-PERFORMANCE-DESC) ")"
           DISPLAY "Years of Service : " FUNCTION TRIM(WS-YEARS-DISPLAY)
               " (" FUNCTION TRIM(WS-TENURE-DESC) ")"
           DISPLAY WS-SEPARATOR
           DISPLAY "Bonus Tier       : " WS-BONUS-TIER
           DISPLAY "Bonus Percent    : " WS-PERCENT-WHOLE "%"
           DISPLAY "Base Salary      : " WS-SALARY-DISPLAY
           DISPLAY "Bonus Amount     : " WS-BONUS-DISPLAY
           DISPLAY WS-SEPARATOR
           DISPLAY " "

           STOP RUN.
