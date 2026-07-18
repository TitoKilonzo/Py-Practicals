       IDENTIFICATION DIVISION.
       PROGRAM-ID. STUDENT.
       AUTHOR. KILONZO.
       DATE-WRITTEN. 2026-07-02.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. GnuCOBOL.
       OBJECT-COMPUTER. GnuCOBOL.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  WS-STUDENT-NAME.
           05  WS-FIRST-NAME        PIC X(12).
           05  WS-SURNAME           PIC X(12).
           05  FILLER               PIC X(06).

       01  WS-STUDENT-ID            PIC 9(08).
       01  FILLER                   PIC X(02).

       01  WS-SUBJECT-MARKS.
           05  WS-MARK-1            PIC 9(03).
           05  WS-MARK-2            PIC 9(03).
           05  WS-MARK-3            PIC 9(03).
           05  WS-MARK-4            PIC 9(03).
           05  FILLER               PIC X(08).

       01  WS-TOTAL-MARKS           PIC 9(03).
       01  FILLER                   PIC X(07).

       01  WS-AVERAGE-MARK          PIC 9(03)V9(02).
       01  FILLER                   PIC X(05).

       01  WS-GRADE                 PIC X(01).
       01  FILLER                   PIC X(09).

       01  WS-REG-DATE              PIC 9(08).
       01  FILLER                   PIC X(02).

       01  WS-AVERAGE-DISPLAY       PIC ZZ9.99.
       01  FILLER                   PIC X(04).

       01  WS-STUDENT-COUNT         PIC 9(03) VALUE ZERO.
       01  FILLER                   PIC X(07).

       PROCEDURE DIVISION.

       MAIN-LOGIC.
           STOP RUN.
